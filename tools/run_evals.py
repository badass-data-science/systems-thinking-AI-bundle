#!/usr/bin/env python3
"""Run the bundle's evals against a model with and without the skill, and grade blind.

Uses the `claude` CLI in headless mode (`claude -p`), so it needs a logged-in
Claude Code, not an API key. For each eval item:

1. The answering model gets the prompt alone, in two otherwise identical
   scratch folders: `with/` has the skill installed as a project skill,
   `without/` does not. Neither is told the skill exists, so the test also
   measures whether the skill gets loaded when it should.
2. A separate grading model sees the prompt, the item's `expected` points and
   `pitfalls`, and one answer. It is not told which condition produced it.
   It scores each expected point 0, 0.5 or 1 and flags each pitfall committed.

Usage:

    python3 run_evals.py WORK_DIR [--answer-model sonnet] [--grade-model opus]
                         [--jobs 6] [--only ID ...] [--eval-file NAME ...]
                         [--cond NAME=SKILL_DIR|none ...]

By default the conditions are `with` (the bundle) and `without` (no skill).
`--cond` replaces them, for example to compare two versions of SKILL.md:
`--cond new=../systems-thinking old=/path/to/old-copy without=none`. The
last condition is the baseline the others are compared with.

Results go to WORK_DIR/out/ (one JSON per answer and per grade, so a rerun
resumes) and a summary to WORK_DIR/summary.json and summary.md.
"""

from __future__ import annotations

import argparse
import json
import random
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_bundle as bb  # noqa: E402

COMMON = ["--setting-sources", "project", "--strict-mcp-config", "--no-session-persistence"]

GRADER_SYSTEM = """You grade answers to systems-thinking exercises against a rubric.
You will get the exercise, the rubric's expected points and pitfalls, and one answer.
Grade only what the answer says, not what it might have meant. Credit a point if the
answer makes it in substance, in any wording or terminology. Ignore length, style,
and any mention of tools, files or references the answer consulted.
Reply with JSON only, no prose and no code fence, in this shape:
{"points": [{"score": 0 | 0.5 | 1, "why": "<one short sentence>"}, ...one per expected point, in order],
 "pitfalls": [{"committed": true | false, "why": "<one short sentence>"}, ...one per pitfall, in order],
 "notes": "<one sentence: anything wrong or harmful in the answer the rubric doesn't cover, or empty>"}"""


def setup(work: Path, conds: dict[str, Path | None]) -> None:
    for name, skill_src in conds.items():
        (work / name).mkdir(parents=True, exist_ok=True)
        if skill_src is not None:
            skill = work / name / ".claude" / "skills" / skill_src.name
            if not skill.exists():
                shutil.copytree(skill_src, skill, ignore=shutil.ignore_patterns("evals"))
    (work / "grader").mkdir(parents=True, exist_ok=True)
    (work / "out").mkdir(parents=True, exist_ok=True)


def run_claude(cwd: Path, args: list[str], prompt: str) -> list[dict]:
    proc = subprocess.run(
        ["claude", "-p", "--output-format", "stream-json", "--verbose", *COMMON, *args],
        input=prompt, cwd=cwd, capture_output=True, text=True, timeout=900)
    events = []
    for line in proc.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    if not any(e.get("type") == "result" for e in events):
        raise RuntimeError(f"claude failed: {proc.stderr[-500:]}")
    return events


def tool_calls(events: list[dict]) -> list[str]:
    calls = []
    for e in events:
        if e.get("type") == "assistant":
            for block in e["message"].get("content", []):
                if block.get("type") == "tool_use":
                    inp = block.get("input", {})
                    calls.append(f'{block["name"]}:{inp.get("skill") or inp.get("file_path") or inp.get("pattern") or ""}')
    return calls


def answer(work: Path, item: dict, cond: str, model: str) -> dict:
    path = work / "out" / f"{item['id']}.{cond}.answer.json"
    if path.exists():
        return json.loads(path.read_text())
    events = run_claude(work / cond, ["--model", model, "--tools", "Read,Glob,Grep,Skill"], item["prompt"].strip())
    res = next(e for e in events if e.get("type") == "result")
    calls = tool_calls(events)
    out = {"id": item["id"], "cond": cond, "answer": res.get("result", ""), "cost": res.get("total_cost_usd", 0),
           "turns": res.get("num_turns"), "tool_calls": calls,
           "skill_loaded": any(c.startswith("Skill:") or "skills/" in c for c in calls)}
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    return out


def grade(work: Path, item: dict, ans: dict, model: str) -> dict:
    path = work / "out" / f"{item['id']}.{ans['cond']}.grade.json"
    if path.exists():
        return json.loads(path.read_text())
    pitfalls = item.get("pitfalls") or []
    msg = ("EXERCISE:\n" + item["prompt"].strip()
           + "\n\nEXPECTED POINTS:\n" + "\n".join(f"{i+1}. {p}" for i, p in enumerate(item["expected"]))
           + "\n\nPITFALLS:\n" + ("\n".join(f"{i+1}. {p}" for i, p in enumerate(pitfalls)) or "(none)")
           + "\n\nANSWER:\n" + ans["answer"])
    for attempt in range(3):
        events = run_claude(work / "grader", ["--model", model, "--tools", "", "--system-prompt", GRADER_SYSTEM], msg)
        res = next(e for e in events if e.get("type") == "result")
        text = res.get("result", "").strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        try:
            g = json.loads(text)
            if len(g["points"]) == len(item["expected"]) and len(g["pitfalls"]) == len(pitfalls):
                break
        except (json.JSONDecodeError, KeyError, TypeError):
            pass
    else:
        raise RuntimeError(f"grader gave unusable output for {item['id']}.{ans['cond']}: {text[:300]}")
    g.update(id=item["id"], cond=ans["cond"], cost=res.get("total_cost_usd", 0),
             score=sum(p["score"] for p in g["points"]) / len(g["points"]),
             pitfalls_committed=sum(p["committed"] for p in g["pitfalls"]))
    path.write_text(json.dumps(g, indent=1, ensure_ascii=False))
    return g


def summarize(work: Path, items: list[dict], conds: list[str]) -> None:
    base = conds[-1]
    rows = []
    for it in items:
        row = {"id": it["id"], "kind": it["kind"]}
        for cond in conds:
            a = json.loads((work / "out" / f"{it['id']}.{cond}.answer.json").read_text())
            g = json.loads((work / "out" / f"{it['id']}.{cond}.grade.json").read_text())
            row[cond] = {"score": g["score"], "pitfalls": g["pitfalls_committed"], "skill_loaded": a["skill_loaded"],
                         "cost": a["cost"] + g["cost"], "notes": g.get("notes", "")}
        rows.append(row)

    def mean(xs):
        return sum(xs) / len(xs) if xs else float("nan")

    def boot(diffs):
        rng = random.Random(0)
        bs = sorted(mean([rng.choice(diffs) for _ in diffs]) for _ in range(5000))
        return bs[124], bs[4874]

    n = len(rows)
    lines = [f"# Eval results: {', '.join(conds)}", "",
             "| | " + " | ".join(conds) + " |", "|---|" + "---|" * len(conds),
             "| Mean score | " + " | ".join(f"{mean([r[c]['score'] for r in rows]):.2f}" for c in conds) + " |",
             "| Pitfalls committed | " + " | ".join(str(sum(r[c]["pitfalls"] for r in rows)) for c in conds) + " |",
             "| Skill loaded | " + " | ".join(f"{sum(r[c]['skill_loaded'] for r in rows)} of {n}" for c in conds) + " |", ""]
    comparisons = {}
    for c in conds[:-1]:
        diffs = [r[c]["score"] - r[base]["score"] for r in rows]
        lo, hi = boot(diffs)
        better = sum(d > 0 for d in diffs); worse = sum(d < 0 for d in diffs)
        lines.append(f"- **{c} vs {base}:** mean difference {mean(diffs):+.2f} (95% paired bootstrap {lo:+.2f} to {hi:+.2f}); "
                     f"better on {better}, worse on {worse}, tied on {n - better - worse}.")
        split = {}
        for flag in (True, False):
            rs = [r for r in rows if r[c]["skill_loaded"] == flag]
            if rs:
                split["loaded" if flag else "not_loaded"] = {"n": len(rs), c: mean([r[c]["score"] for r in rs]),
                                                             base: mean([r[base]["score"] for r in rs])}
                lines.append(f"  - {'loaded' if flag else 'not loaded'} ({len(rs)} items): "
                             f"{mean([r[c]['score'] for r in rs]):.2f} vs {mean([r[base]['score'] for r in rs]):.2f}")
        comparisons[c] = {"mean_diff": mean(diffs), "ci95": [lo, hi], "better": better, "worse": worse, "split": split}
    lines += ["", "## By kind", "", "| Kind | n | " + " | ".join(conds) + " |", "|---|---|" + "---|" * len(conds)]
    for kind in sorted({r["kind"] for r in rows}):
        rs = [r for r in rows if r["kind"] == kind]
        lines.append(f"| {kind} | {len(rs)} | " + " | ".join(f"{mean([r[c]['score'] for r in rs]):.2f}" for c in conds) + " |")
    lines += ["", "## By item (score, and * if the skill was loaded)", "", "| Item | Kind | " + " | ".join(conds) + " |",
              "|---|---|" + "---|" * len(conds)]
    for r in rows:
        lines.append(f"| {r['id']} | {r['kind']} | " + " | ".join(
            f"{r[c]['score']:.2f}{'*' if r[c]['skill_loaded'] else ''}" for c in conds) + " |")
    cost = sum(r[c]["cost"] for r in rows for c in conds)
    lines.insert(2, f"{n} items. Cost ${cost:.2f} (including any reused runs).\n")
    summary = {"n": n, "conds": conds, "means": {c: mean([r[c]["score"] for r in rows]) for c in conds},
               "comparisons": comparisons, "cost_usd": cost, "rows": rows}
    (work / "summary.json").write_text(json.dumps(summary, indent=1, ensure_ascii=False))
    (work / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:14 + 3 * len(conds)]))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("work", type=Path)
    ap.add_argument("--bundle", type=Path, default=bb.DEFAULT_BUNDLE)
    ap.add_argument("--answer-model", default="sonnet")
    ap.add_argument("--grade-model", default="opus")
    ap.add_argument("--jobs", type=int, default=6)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--eval-file", nargs="*", help="only items from these eval files (names, e.g. archetypes.yaml)")
    ap.add_argument("--cond", nargs="*", help="NAME=SKILL_DIR or NAME=none; the last is the baseline")
    args = ap.parse_args()
    work, bundle = args.work.resolve(), args.bundle.resolve()
    specs = args.cond or [f"with={bundle}", "without=none"]
    conds = {}
    for spec in specs:
        name, _, src = spec.partition("=")
        conds[name] = None if src == "none" else Path(src).resolve()
    setup(work, conds)
    items = bb.check_evals(bundle, bb.load_cards(bundle, bb.Report()), bb.Report())
    if args.only:
        items = [e for e in items if e["id"] in args.only]
    if args.eval_file:
        items = [e for e in items if Path(e["_file"]).name in args.eval_file]

    def job(pair):
        item, cond = pair
        try:
            a = answer(work, item, cond, args.answer_model)
            grade(work, item, a, args.grade_model)
            print(f"done {item['id']} {cond}", flush=True)
        except Exception as exc:  # keep going; a rerun retries
            print(f"FAILED {item['id']} {cond}: {exc}", flush=True)

    with ThreadPoolExecutor(args.jobs) as pool:
        list(pool.map(job, [(i, c) for i in items for c in conds]))
    missing = [i["id"] for i in items for c in conds
               if not (work / "out" / f"{i['id']}.{c}.grade.json").exists()]
    if missing:
        sys.exit(f"{len(missing)} runs missing; rerun to retry: {sorted(set(missing))}")
    summarize(work, items, list(conds))


if __name__ == "__main__":
    main()
