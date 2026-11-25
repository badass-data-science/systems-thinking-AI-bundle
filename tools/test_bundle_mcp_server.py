#!/usr/bin/env python3
"""Tests for bundle_mcp_server.py: call each MCP tool as a plain function on the
real bundle, plant known errors in structures passed to check_loops, and hold
search and archetype matching to their current hit rates so a change that makes
ranking worse fails. Run with:

    python3 test_bundle_mcp_server.py

Needs pyyaml and mcp 2.x. Exits 1 if any check fails.
"""
import copy
import json
import sys
from pathlib import Path

import yaml

sys.argv = sys.argv[:1]  # the server reads an optional bundle path from argv at import
sys.path.insert(0, str(Path(__file__).resolve().parent))
import bundle_mcp_server as s  # noqa: E402

failures = 0


def expect(name, cond):
    global failures
    print(("ok   " if cond else "FAIL ") + name)
    failures += not cond


# Loading
expect("bundle loads without errors", not s._report.errors)
expect("176 cards and 115 evals loaded", (len(s.CARDS), len(s.EVALS)) == (176, 115))

# get_card
text = s.get_card("fixes-that-fail")
expect("get_card returns the card file", text.startswith("---\n") and "title: Fixes That Fail" in text)
expect("get_card on an unknown id says so", s.get_card("no-such-card").startswith("No card with id"))

# list_cards
rows = json.loads(s.list_cards())
expect("list_cards lists every card", len(rows) == len(s.CARDS))
arch = json.loads(s.list_cards("archetype"))
expect("list_cards filters by type", len(arch) == 11 and all(r["type"] == "archetype" for r in arch))
expect("list_cards on an unknown type is empty", json.loads(s.list_cards("nonsense")) == [])

# search_cards
res = json.loads(s.search_cards("catwoe"))
expect("search_cards says it is keyword ranking", "keyword" in res["note"])
expect("search_cards finds the CATWOE card", "catwoe" in [r["id"] for r in res["results"]])
res = json.loads(s.search_cards("loop", type="archetype", limit=4))["results"]
expect("search_cards honours type and limit", 0 < len(res) <= 4 and all(r["type"] == "archetype" for r in res))
expect("search_cards returns nothing for gibberish", json.loads(s.search_cards("zzqxv"))["results"] == [])
scores = [r["score"] for r in json.loads(s.search_cards("stock and flow"))["results"]]
expect("search_cards results are ranked", scores == sorted(scores, reverse=True))

# Searching each card's own title, with the exact-name bonus and without it (word
# weighting alone). Floors are today's rates: 176 and 173 first, of 176.
def title_search(exact_bonus=True):
    saved, s.EXACT = s.EXACT, (s.EXACT if exact_bonus else 0)
    first = top3 = 0
    for cid, c in s.CARDS.items():
        got = [r["id"] for r in json.loads(s.search_cards(c["title"], limit=3))["results"]]
        first += bool(got) and got[0] == cid
        top3 += cid in got
    s.EXACT = saved
    return first, top3


first, top3 = title_search()
expect(f"title search ranks the card first for all 176 cards (now {first})", first == 176)
first, top3 = title_search(exact_bonus=False)
expect(f"without the exact-name bonus, title search ranks the card first for >= 173 (now {first})", first >= 173)
expect(f"without the exact-name bonus, title search ranks the card in the top 3 for all 176 (now {top3})", top3 == 176)

top = lambda q: json.loads(s.search_cards(q, limit=1))["results"][0]["id"]  # noqa: E731
expect("search matches a title ignoring case and apostrophes",
       top("DONT REACT HARDER TO A LATE SIGNAL") == "dont-react-harder-to-late-signals")
expect("search matches a card id", top("fixes-that-fail") == "fixes-that-fail")
expect("search keeps two-letter words such as AI", top("AI system as a system") == "ai-system-as-a-system")
expect("search ranks a card first from part of its title", top("fixes fail") == "fixes-that-fail")
expect("search ranks a card first from its symptoms", top("quick fix makes it worse") == "fixes-that-fail")
expect("search counts a repeated query word once", s._score("loop loop", "feedback-loop") == s._score("loop", "feedback-loop"))

# related_cards
rel = json.loads(s.related_cards("fixes-that-fail"))
expect("related_cards lists outgoing edges",
       {"relation": "contrasts-with", "target": "st:shifting-the-burden", "title": "Shifting the Burden"} in rel["outgoing"])
expect("related_cards lists incoming edges", len(rel["incoming"]) > 0
       and all(e["source"].startswith("st:") for e in rel["incoming"]))
expect("related_cards on an unknown id says so", s.related_cards("no-such-card").startswith("No card with id"))

# match_archetype
m = json.loads(s.match_archetype("we keep applying the same quick fix and the underlying problem gets worse", limit=2))
expect("match_archetype returns the limit", len(m["candidates"]) == 2)
expect("match_archetype ranks Fixes That Fail first for its own symptoms", m["candidates"][0]["id"] == "fixes-that-fail")
expect("match_archetype lists every diagnostic question", len(m["all_diagnostic_questions"]) == 11)
expect("match_archetype points to the procedure", m["procedure"] == "diagnose-an-archetype")

# Recognition evals as a benchmark (as in bench_match_archetype.py): floors are today's rates.
archetypes = {c for c, v in s.CARDS.items() if v["type"] == "archetype"}
n = top1 = top3 = 0
for e in s.EVALS:
    want = [u for u in e["uses"] if u in archetypes]
    if e["kind"] != "recognize" or not want:
        continue
    n += 1
    got = [c["id"] for c in json.loads(s.match_archetype(e["prompt"], limit=3))["candidates"]]
    top1 += got[0] in want
    top3 += any(g in want for g in got)
expect(f"match_archetype top 1 on recognition evals >= 10 of 23 (now {top1} of {n})", n == 23 and top1 >= 10)
expect(f"match_archetype top 3 on recognition evals >= 15 of 23 (now {top3} of {n})", n == 23 and top3 >= 15)

# check_loops: every archetype card's own structure passes, as YAML and as JSON.
for cid in sorted(archetypes):
    st = s.CARDS[cid]["structure"]
    expect(f"check_loops passes {cid} (YAML)", s.check_loops(yaml.safe_dump(st)).startswith("OK:"))
expect("check_loops accepts JSON", s.check_loops(json.dumps(s.CARDS["escalation"]["structure"])).startswith("OK:"))

# check_loops: planted errors, starting from Fixes That Fail.
base = s.CARDS["fixes-that-fail"]["structure"]


def planted(change):
    st = copy.deepcopy(base)
    change(st)
    return s.check_loops(yaml.safe_dump(st))


def relabel(st):
    st["loops"][0]["type"] = "R"


def drop_link(st):
    st["links"] = [ln for ln in st["links"] if not (ln["from"] == "side effect" and ln["to"] == "underlying damage")]


def flip(st):
    st["links"][0]["polarity"] = "+"


def bad_polarity(st):
    st["links"][0]["polarity"] = "up"


def undeclared(st):
    st["variables"].remove("side effect")


def no_loops(st):
    st["loops"] = []


out = planted(relabel)
expect("check_loops reports a mislabeled loop", "loop B1 declared R" in out and not out.startswith("OK"))
expect("check_loops reports a loop that doesn't close",
       "loop R1 needs link side effect -> underlying damage" in planted(drop_link))
out = planted(flip)
expect("check_loops reports both loops a flipped link changes", "loop B1 declared B" in out and "loop R1 declared R" in out)
expect("check_loops reports a bad polarity", "has polarity 'up'" in planted(bad_polarity))
expect("check_loops reports an undeclared variable", "undeclared variable 'side effect'" in planted(undeclared))
expect("check_loops reports no loops", "no loops declared" in planted(no_loops))
expect("check_loops always adds the reminder", s.check_loops(yaml.safe_dump(base)).endswith("works where its links live."))

# check_loops: input that isn't a structure gets an answer, not an exception.
for bad in ["{: bad", "just a sentence", "[1, 2]", ""]:
    try:
        out = s.check_loops(bad)
        expect(f"check_loops answers {bad!r} without crashing", out.startswith("Couldn't") or "ERROR" in out)
    except Exception as exc:  # noqa: BLE001
        expect(f"check_loops answers {bad!r} without crashing ({type(exc).__name__}: {exc})", False)

# list_evals and get_eval
expect("list_evals lists every eval", len(json.loads(s.list_evals())) == 115)
rec = json.loads(s.list_evals("recognize"))
expect("list_evals filters by kind", rec and all(r["kind"] == "recognize" for r in rec))
eid = rec[0]["id"]
item = json.loads(s.get_eval(eid))
expect("get_eval hides the answer by default", "expected" not in item and "pitfalls" not in item and item["prompt"])
item = json.loads(s.get_eval(eid, include_answer=True))
expect("get_eval gives the answer on request", item["expected"] and "pitfalls" in item)
expect("get_eval on an unknown id says so", s.get_eval("no-such-eval").startswith("No eval with id"))

# The tools are registered with the MCP server under these names.
import asyncio  # noqa: E402

names = {t.name for t in asyncio.run(s.mcp.list_tools())}
expect("all eight tools are registered", names == {"search_cards", "get_card", "list_cards", "related_cards",
                                                     "match_archetype", "check_loops", "list_evals", "get_eval"})


# A real round trip: start the server over stdio as an MCP client would, list its
# tools and call two of them.
from mcp import ClientSession, StdioServerParameters  # noqa: E402
from mcp.client.stdio import stdio_client  # noqa: E402


async def round_trip():
    server = StdioServerParameters(command=sys.executable, args=[str(Path(s.__file__)), str(s.BUNDLE)])
    async with stdio_client(server) as (read, write), ClientSession(read, write) as session:
        await session.initialize()
        listed = {t.name for t in (await session.list_tools()).tools}
        card = (await session.call_tool("get_card", {"id": "fixes-that-fail"})).content[0].text
        loops = (await session.call_tool("check_loops", {"structure": yaml.safe_dump(base)})).content[0].text
        return listed, card, loops


try:
    listed, card, loops = asyncio.run(asyncio.wait_for(round_trip(), 60))
    expect("over stdio: the server lists all eight tools", listed == names)
    expect("over stdio: get_card returns the card", "title: Fixes That Fail" in card)
    expect("over stdio: check_loops runs", loops.startswith("OK:"))
except Exception as exc:  # noqa: BLE001
    expect(f"over stdio: the server starts and answers ({type(exc).__name__}: {exc})", False)

sys.exit(1 if failures else 0)
