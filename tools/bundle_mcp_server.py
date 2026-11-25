#!/usr/bin/env python3
"""A small MCP server over a book's AI bundle.

It works for any bundle that follows SCHEMA.md, so one server can serve every
book in the series. Run it over stdio:

    python3 bundle_mcp_server.py [BUNDLE_DIR]

BUNDLE_DIR defaults to ../systems-thinking. To use it from Claude Code:

    claude mcp add systems-thinking -- python3 /path/to/bundle_mcp_server.py /path/to/systems-thinking

Tools: search_cards, get_card, list_cards, related_cards, match_archetype,
check_loops, list_evals and get_eval. `check_loops` runs the bundle's own
trace-and-count validator on a structure the caller supplies, so an agent can
check a causal loop diagram it has drawn instead of labeling loops by feel.

Search and archetype matching are plain keyword scoring, not semantic search:
they rank candidates to read, and every result says so.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml
from mcp.server.fastmcp import FastMCP

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_bundle as bb  # noqa: E402

BUNDLE = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else bb.DEFAULT_BUNDLE

_report = bb.Report()
CARDS = bb.load_cards(BUNDLE, _report)
EVALS = bb.check_evals(BUNDLE, CARDS, _report)
GRAPH = bb.build_graph(CARDS)

STOP = set("a an the of to in on and or for is are be it this that with as by at from what which who how when do does not".split())


def _tokens(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z0-9]+", text.lower()) if t not in STOP and len(t) > 2]


def _card_text(c: dict) -> str:
    parts = [c.get("title", ""), " ".join(c.get("aliases") or []), c.get("summary", ""),
             str(c.get("when", "")), str(c.get("then", "")), str(c.get("diagnostic_question", "")), c["_body"]]
    return " ".join(parts)


INDEX = {cid: Counter(_tokens(_card_text(c))) for cid, c in CARDS.items()}
HEAD = {cid: set(_tokens(" ".join([c["title"], " ".join(c.get("aliases") or []), c["summary"]]))) for cid, c in CARDS.items()}


def _score(query: str, cid: str) -> float:
    q = _tokens(query)
    return sum(min(INDEX[cid][t], 3) + (3 if t in HEAD[cid] else 0) for t in q)


def _brief(c: dict) -> dict:
    return {"id": c["id"], "type": c["type"], "title": c["title"], "summary": c["summary"],
            "chapters": c["chapters"], "path": c["_path"]}


mcp = FastMCP("systems-thinking-bundle")


@mcp.tool()
def search_cards(query: str, type: str | None = None, limit: int = 8) -> str:
    """Keyword-search the bundle's cards. Optionally restrict to one type:
    concept, procedure, archetype, heuristic, case or tool. Returns ranked
    candidates with summaries; open the best ones with get_card."""
    pool = [cid for cid, c in CARDS.items() if type is None or c["type"] == type]
    ranked = sorted(pool, key=lambda cid: -_score(query, cid))
    hits = [dict(_brief(CARDS[cid]), score=_score(query, cid)) for cid in ranked[:limit] if _score(query, cid) > 0]
    return json.dumps({"note": "keyword ranking, not semantic search", "results": hits}, indent=1, ensure_ascii=False)


@mcp.tool()
def get_card(id: str) -> str:
    """Return one card in full (frontmatter and Markdown body) by its id."""
    c = CARDS.get(id)
    if not c:
        return f"No card with id {id!r}. Use search_cards or list_cards."
    return (BUNDLE / c["_path"]).read_text(encoding="utf-8")


@mcp.tool()
def list_cards(type: str | None = None) -> str:
    """List cards (id, title, summary), optionally of one type."""
    rows = [_brief(c) for c in sorted(CARDS.values(), key=lambda c: (c["type"], c["title"].lower()))
            if type is None or c["type"] == type]
    return json.dumps(rows, indent=1, ensure_ascii=False)


@mcp.tool()
def related_cards(id: str) -> str:
    """Return the typed edges into and out of a card, from the bundle graph."""
    node = f"st:{id}"
    if id not in CARDS:
        return f"No card with id {id!r}."
    out = [e for e in GRAPH["edges"] if e["source"] == node]
    inc = [e for e in GRAPH["edges"] if e["target"] == node]
    title = lambda n: CARDS[n[3:]]["title"] if n.startswith("st:") and n[3:] in CARDS else n  # noqa: E731
    return json.dumps({
        "outgoing": [{"relation": e["relation"], "target": e["target"], "title": title(e["target"])} for e in out],
        "incoming": [{"relation": e["relation"], "source": e["source"], "title": title(e["source"])} for e in inc],
    }, indent=1, ensure_ascii=False)


def _section(body: str, name: str) -> str:
    m = re.search(rf"^## {re.escape(name)}\s*$(.*?)(?=^## |\Z)", body, re.MULTILINE | re.DOTALL)
    return m.group(1) if m else ""


# Archetype matching scores only the parts of a card that describe what the
# archetype looks like from outside (title, aliases, diagnostic question, symptoms,
# summary), weighted by inverse document frequency across archetypes.
# The Misapplications and Distinguish-from sections are excluded because they
# name the neighbours' vocabulary on purpose.
import math  # noqa: E402

ARCH = {cid: c for cid, c in CARDS.items() if c["type"] == "archetype"}
ARCH_TEXT = {cid: Counter(_tokens(" ".join([
    c["title"], " ".join(c.get("aliases") or []), c["summary"], c["diagnostic_question"],
    _section(c["_body"], "Symptoms"),
]))) for cid, c in ARCH.items()}
_df = Counter(t for counts in ARCH_TEXT.values() for t in counts)
IDF = {t: math.log((1 + len(ARCH)) / (1 + d)) + 1 for t, d in _df.items()}


def _arch_score(text: str, cid: str) -> float:
    counts = ARCH_TEXT[cid]
    return round(sum(IDF.get(t, 0) * min(counts[t], 2) for t in set(_tokens(text))), 2)


@mcp.tool()
def match_archetype(situation: str, limit: int = 3) -> str:
    """Rank systems archetypes against a plain-language description of a
    recurring problem. Returns each candidate's diagnostic question and
    structure, plus every archetype's diagnostic question so none is skipped
    because the ranking missed it. A match is a hypothesis: confirm it by drawing the situation's
    actual links and running check_loops, and compare with the archetype's
    structure, before naming it."""
    ranked = sorted(ARCH, key=lambda cid: -_arch_score(situation, cid))[:limit]
    return json.dumps({
        "note": "keyword ranking; a hint, not a diagnosis. Ask each diagnostic question, then trace the real links.",
        "procedure": "diagnose-an-archetype",
        "candidates": [{
            "id": cid, "title": CARDS[cid]["title"], "score": _arch_score(situation, cid),
            "diagnostic_question": CARDS[cid]["diagnostic_question"],
            "structure": CARDS[cid]["structure"],
        } for cid in ranked],
        "all_diagnostic_questions": {cid: c["diagnostic_question"] for cid, c in sorted(ARCH.items())},
    }, indent=1, ensure_ascii=False)


@mcp.tool()
def check_loops(structure: str) -> str:
    """Check a causal loop diagram with the trace-and-count rule. Pass YAML or
    JSON with `variables` (names), `links` (each {from, to, polarity: "+" or
    "-", optional delay, optional exogenous: true}) and `loops` (each {id,
    type: R or B, path: [variables in order]}). Reports loops that don't close
    and loops whose declared type doesn't match their count of minus links.
    Passing means each loop closes and is labeled correctly, not that the
    diagram is true or that it is the archetype you have in mind."""
    try:
        st = yaml.safe_load(structure)
    except yaml.YAMLError as exc:
        return f"Couldn't parse structure: {exc}"
    rep = bb.Report()
    bb.check_structure({"_path": "input", "structure": st}, rep)
    lines = rep.errors + rep.warnings
    if not rep.errors:
        lines.insert(0, "OK: every loop closes and matches its declared type.")
    lines.append("Reminder: consistent isn't true. Read each loop aloud to someone who works where its links live.")
    return "\n".join(lines)


@mcp.tool()
def list_evals(kind: str | None = None) -> str:
    """List eval items (id, kind, the start of the prompt). Kinds: recognize,
    apply, discriminate, critique, procedure."""
    rows = [{"id": e["id"], "kind": e["kind"], "file": e["_file"], "prompt": " ".join(e["prompt"].split())[:160]}
            for e in EVALS if kind is None or e["kind"] == kind]
    return json.dumps(rows, indent=1, ensure_ascii=False)


@mcp.tool()
def get_eval(id: str, include_answer: bool = False) -> str:
    """Return one eval item. By default only the prompt and the cards it
    draws on; set include_answer to get the expected points and pitfalls,
    for grading."""
    for e in EVALS:
        if e["id"] == id:
            out = {"id": e["id"], "kind": e["kind"], "prompt": e["prompt"], "uses": e["uses"]}
            if include_answer:
                out["expected"] = e["expected"]
                out["pitfalls"] = e.get("pitfalls", [])
            return json.dumps(out, indent=1, ensure_ascii=False)
    return f"No eval with id {id!r}."


if __name__ == "__main__":
    mcp.run()
