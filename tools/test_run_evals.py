#!/usr/bin/env python3
"""Offline tests for run_evals.py. Nothing here calls a model: a stand-in
`claude` script on PATH plays both the answering model and the grader, so the
whole pipeline (setup, answering, grading with retries, resuming, and the
summary statistics) runs in a few seconds without a login. Run with:

    python3 test_run_evals.py

Needs pyyaml. Exits 1 if any check fails.
"""
import contextlib
import io
import json
import os
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_evals as rv  # noqa: E402

failures = 0


def expect(name, cond):
    global failures
    print(("ok   " if cond else "FAIL ") + name)
    failures += not cond


# A stand-in for `claude -p --output-format stream-json`. As the answering model
# it loads the skill when the working folder has one; as the grader (called
# with --system-prompt) it gives every point 1 when the answer used the skill
# and 0.5 otherwise. FAKE_CLAUDE_MODE changes its behaviour for single tests.
FAKE = r'''#!/usr/bin/env python3
import json, os, re, sys
from pathlib import Path
args, prompt = sys.argv[1:], sys.stdin.read()
mode = os.environ.get("FAKE_CLAUDE_MODE", "")
log = os.environ.get("FAKE_CLAUDE_LOG")
if log:
    with open(log, "a") as f:
        f.write(json.dumps({"args": args, "cwd": os.getcwd()}) + "\n")
if mode == "crash":
    sys.stderr.write("not logged in")
    sys.exit(1)
def emit(e):
    print(json.dumps(e))
print("a line that isn't JSON")
if "--system-prompt" in args:
    section = lambda name: re.search(name + r":\n(.*?)(?:\n\n[A-Z]+[A-Z ]*:|\Z)", prompt, re.S).group(1)
    n_points = len(re.findall(r"^\d+\. ", section("EXPECTED POINTS"), re.M))
    pits = section("PITFALLS")
    n_pits = 0 if pits.strip() == "(none)" else len(re.findall(r"^\d+\. ", pits, re.M))
    score = 1 if "USED THE SKILL" in prompt else 0.5
    g = {"points": [{"score": score, "why": "x"}] * n_points,
         "pitfalls": [{"committed": score < 1, "why": "x"}] * n_pits, "notes": ""}
    text = "```json\n" + json.dumps(g) + "\n```"
    if mode == "bad-grade":
        text = "I think this answer is quite good."
    emit({"type": "result", "result": text, "total_cost_usd": 0.02})
else:
    skilled = Path(".claude/skills").is_dir()
    if skilled:
        emit({"type": "assistant", "message": {"content": [
            {"type": "text", "text": "Let me check."},
            {"type": "tool_use", "name": "Skill", "input": {"skill": "systems-thinking"}}]}})
    emit({"type": "result", "result": "USED THE SKILL" if skilled else "plain answer",
          "total_cost_usd": 0.1, "num_turns": 3})
'''

with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    bindir = tmp / "bin"
    bindir.mkdir()
    fake = bindir / "claude"
    fake.write_text(FAKE)
    fake.chmod(fake.stat().st_mode | stat.S_IEXEC)
    os.environ["PATH"] = f"{bindir}{os.pathsep}{os.environ['PATH']}"
    log = tmp / "calls.jsonl"
    os.environ["FAKE_CLAUDE_LOG"] = str(log)

    # tool_calls
    events = [
        {"type": "system"},
        {"type": "assistant", "message": {"content": [
            {"type": "text", "text": "hi"},
            {"type": "tool_use", "name": "Skill", "input": {"skill": "systems-thinking"}},
            {"type": "tool_use", "name": "Read", "input": {"file_path": "skills/x/SKILL.md"}},
            {"type": "tool_use", "name": "Grep", "input": {"pattern": "loop"}},
            {"type": "tool_use", "name": "Glob", "input": {}}]}},
        {"type": "user", "message": {"content": [{"type": "tool_use", "name": "Ignored", "input": {}}]}},
    ]
    expect("tool_calls lists the assistant's tool calls only",
           rv.tool_calls(events) == ["Skill:systems-thinking", "Read:skills/x/SKILL.md", "Grep:loop", "Glob:"])
    expect("tool_calls on no events is empty", rv.tool_calls([]) == [])

    # run_claude
    ev = rv.run_claude(tmp, [], "hello")
    expect("run_claude skips lines that aren't JSON and returns the events", ev[-1]["type"] == "result")
    os.environ["FAKE_CLAUDE_MODE"] = "crash"
    try:
        rv.run_claude(tmp, [], "hello")
        expect("run_claude raises when claude gives no result", False)
    except RuntimeError as exc:
        expect("run_claude raises when claude gives no result, with its stderr", "not logged in" in str(exc))
    del os.environ["FAKE_CLAUDE_MODE"]

    # setup
    skill_src = tmp / "systems-thinking"
    (skill_src / "evals").mkdir(parents=True)
    (skill_src / "SKILL.md").write_text("x")
    (skill_src / "evals" / "secret.yaml").write_text("answers")
    work = tmp / "work"
    rv.setup(work, {"with": skill_src, "without": None})
    installed = work / "with" / ".claude" / "skills" / "systems-thinking"
    expect("setup installs the skill in the `with` folder", (installed / "SKILL.md").exists())
    expect("setup leaves the evals (and their answers) out of the installed skill", not (installed / "evals").exists())
    expect("setup gives `without` no skill", (work / "without").is_dir() and not (work / "without" / ".claude").exists())
    expect("setup makes the grader and out folders", (work / "grader").is_dir() and (work / "out").is_dir())

    # answer and grade
    item = {"id": "t-1", "kind": "apply", "prompt": "  What happens?  \n",
            "expected": ["point one", "point two", "point three"], "pitfalls": ["pitfall one"]}
    a = rv.answer(work, item, "with", "sonnet")
    expect("answer records the answer, cost and turns",
           (a["answer"], a["cost"], a["turns"]) == ("USED THE SKILL", 0.1, 3))
    expect("answer records that the skill was loaded", a["skill_loaded"] and a["tool_calls"] == ["Skill:systems-thinking"])
    b = rv.answer(work, item, "without", "sonnet")
    expect("answer records that the skill wasn't loaded", not b["skill_loaded"] and b["tool_calls"] == [])
    calls = [json.loads(line) for line in log.read_text().splitlines()]
    expect("answer runs in the condition's own folder", calls[-2]["cwd"] == str(work / "with"))
    expect("answer passes the model and the read-only tools",
           calls[-1]["args"][-4:] == ["--model", "sonnet", "--tools", "Read,Glob,Grep,Skill"])
    n_calls = len(calls)
    rv.answer(work, item, "with", "sonnet")
    expect("answer reuses a saved answer instead of calling claude again", len(log.read_text().splitlines()) == n_calls)

    g = rv.grade(work, item, a, "opus")
    expect("grade strips a code fence and scores the answer", g["score"] == 1 and g["pitfalls_committed"] == 0)
    g = rv.grade(work, item, b, "opus")
    expect("grade averages the points and counts pitfalls", g["score"] == 0.5 and g["pitfalls_committed"] == 1)
    calls = [json.loads(line) for line in log.read_text().splitlines()]
    expect("grade runs blind in the grader folder with no tools", calls[-1]["cwd"] == str(work / "grader")
           and calls[-1]["args"][-6:-2] == ["--model", "opus", "--tools", ""])

    item2 = dict(item, id="t-2", pitfalls=[])
    os.environ["FAKE_CLAUDE_MODE"] = "bad-grade"
    n_calls = len(log.read_text().splitlines())
    try:
        rv.grade(work, item2, dict(a, id="t-2"), "opus")
        expect("grade raises after three unusable gradings", False)
    except RuntimeError as exc:
        expect("grade raises after three unusable gradings", "unusable output" in str(exc)
               and len(log.read_text().splitlines()) == n_calls + 3)
    del os.environ["FAKE_CLAUDE_MODE"]
    expect("grade saves nothing when grading failed", not (work / "out" / "t-2.with.grade.json").exists())
    g = rv.grade(work, item2, dict(a, id="t-2"), "opus")
    expect("grade handles an item with no pitfalls", g["score"] == 1 and g["pitfalls"] == [])

    # summarize, on hand-made results with known statistics
    sw = tmp / "sum"
    (sw / "out").mkdir(parents=True)
    table = [("a", "apply", 1.0, 0.5, True), ("b", "apply", 0.5, 0.5, False), ("c", "recognize", 0.0, 0.5, True)]
    for iid, kind, s_with, s_without, loaded in table:
        for cond, score, sl in (("with", s_with, loaded), ("without", s_without, False)):
            (sw / "out" / f"{iid}.{cond}.answer.json").write_text(json.dumps({"skill_loaded": sl, "cost": 0.25}))
            (sw / "out" / f"{iid}.{cond}.grade.json").write_text(json.dumps(
                {"score": score, "pitfalls_committed": int(score < 1), "cost": 0.25}))
    items = [{"id": iid, "kind": kind} for iid, kind, *_ in table]
    with contextlib.redirect_stdout(io.StringIO()):
        rv.summarize(sw, items, ["with", "without"])
    summ = json.loads((sw / "summary.json").read_text())
    md = (sw / "summary.md").read_text()
    c = summ["comparisons"]["with"]
    expect("summarize computes the means", summ["means"] == {"with": 0.5, "without": 0.5})
    expect("summarize counts better, worse and tied", (c["better"], c["worse"]) == (1, 1) and "tied on 1" in md)
    expect("summarize gives a bootstrap interval around the difference",
           c["mean_diff"] == 0 and -0.5 <= c["ci95"][0] <= 0 <= c["ci95"][1] <= 0.5)
    expect("summarize splits by whether the skill loaded",
           c["split"]["loaded"] == {"n": 2, "with": 0.5, "without": 0.5}
           and c["split"]["not_loaded"] == {"n": 1, "with": 0.5, "without": 0.5})
    expect("summarize totals the cost", summ["cost_usd"] == 3.0 and "Cost $3.00" in md)
    expect("summarize writes the tables", "| Skill loaded | 2 of 3 | 0 of 3 |" in md
           and "| recognize | 1 | 0.00 | 0.50 |" in md and "| a | apply | 1.00* | 0.50 |" in md)
    with contextlib.redirect_stdout(io.StringIO()):
        rv.summarize(sw, items, ["with", "without"])
    expect("summarize is repeatable (fixed bootstrap seed)", json.loads((sw / "summary.json").read_text()) == summ)

    # The whole command, end to end, on one real eval item.
    bundle = HERE.parent / "systems-thinking"
    first = rv.bb.check_evals(bundle, rv.bb.load_cards(bundle, rv.bb.Report()), rv.bb.Report())[0]["id"]
    e2e = tmp / "e2e"
    proc = subprocess.run([sys.executable, str(HERE / "run_evals.py"), str(e2e), "--only", first, "--jobs", "2"],
                          capture_output=True, text=True)
    expect(f"run_evals.py runs end to end on {first}", proc.returncode == 0)
    if proc.returncode == 0:
        summ = json.loads((e2e / "summary.json").read_text())
        row = summ["rows"][0]
        expect("end to end: with the skill loaded and scored higher",
               row["with"]["skill_loaded"] and not row["without"]["skill_loaded"]
               and row["with"]["score"] == 1 and row["without"]["score"] == 0.5)
    else:
        print(proc.stdout[-1000:], proc.stderr[-1000:])

sys.exit(1 if failures else 0)
