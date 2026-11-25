#!/usr/bin/env python3
"""Validate a book's AI bundle and generate its graph and index.

Usage (from anywhere):

    python3 build_bundle.py [BUNDLE_DIR]

BUNDLE_DIR defaults to ../systems-thinking relative to this script. The
script checks every card against SCHEMA.md, checks that every archetype's
loops close and have the polarity they claim, checks the eval set, and
writes graph.json, graph.ttl and INDEX.md into the bundle. It exits 1 on
any error, so it can gate a commit or CI run.
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DEFAULT_BUNDLE = HERE.parent / "systems-thinking"
SERIES_FILE = HERE.parent / "series-concepts.yaml"

TYPES = {
    "concept": "concepts",
    "procedure": "procedures",
    "archetype": "archetypes",
    "heuristic": "heuristics",
    "case": "cases",
    "tool": "tools",
}
COMMON_REQUIRED = ["id", "type", "title", "summary", "chapters"]
TYPE_REQUIRED = {
    "procedure": ["inputs", "outputs"],
    "archetype": ["diagnostic_question", "structure"],
    "heuristic": ["when", "then"],
    "case": ["source_example"],
    "tool": ["license"],
}
TYPE_SECTIONS = {
    "procedure": ["When to use", "Steps", "Checks", "Common mistakes"],
    "archetype": ["Signature", "Symptoms", "Interventions", "Misapplications", "Distinguish from"],
    "case": ["Situation", "Analysis", "Lesson"],
}
RELATIONS = {
    "requires", "specializes", "part-of", "contrasts-with", "uses", "produces",
    "diagnoses", "counters", "instance-of", "related",
}
SYMMETRIC = {"contrasts-with", "related"}
VALID_CHAPTERS = set(range(1, 27)) | set("ABCDE")
EVAL_KINDS = {"recognize", "apply", "discriminate", "critique", "procedure"}
EVAL_REQUIRED = ["id", "kind", "prompt", "expected", "uses"]

# The series' costume. These may appear only in `mnemonic` and `source_example`.
COSTUME = re.compile(
    r"\b(villain\w*|henchm[ae]n\w*|henchpe\w*|secret lab|lair\w*|doomsday|warhead\w*"
    r"|interpol|our heroine|rival supervillain|death ray|evil)\b",
    re.IGNORECASE,
)
COSTUME_OK_FIELDS = {"mnemonic", "source_example"}
# Optional: a folder holding the book's published code (for example a checkout of
# https://github.com/badass-data-science/books, folder systems-thinking-for-supervillains).
# When set, the build warns if code/ has drifted from it. Unset, the check is skipped.
CODE_SOURCE = Path(os.environ["BUNDLE_CODE_SOURCE"]).expanduser() if os.environ.get("BUNDLE_CODE_SOURCE") else None

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n(.*)\Z", re.DOTALL)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, where: str, msg: str) -> None:
        self.errors.append(f"ERROR   {where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"warning {where}: {msg}")


def load_cards(bundle: Path, rep: Report) -> dict[str, dict]:
    cards: dict[str, dict] = {}
    for type_name, folder in TYPES.items():
        for path in sorted((bundle / folder).glob("*.md")):
            rel = path.relative_to(bundle)
            m = FRONTMATTER.match(path.read_text(encoding="utf-8"))
            if not m:
                rep.error(str(rel), "no YAML frontmatter")
                continue
            try:
                meta = yaml.safe_load(m.group(1)) or {}
            except yaml.YAMLError as exc:
                rep.error(str(rel), f"bad YAML: {exc}")
                continue
            meta["_path"] = str(rel)
            meta["_body"] = m.group(2)
            cid = meta.get("id")
            if cid != path.stem:
                rep.error(str(rel), f"id {cid!r} doesn't match filename")
            if meta.get("type") != type_name:
                rep.error(str(rel), f"type {meta.get('type')!r} doesn't match folder {folder}/")
            if cid in cards:
                rep.error(str(rel), f"duplicate id (also {cards[cid]['_path']})")
            cards[path.stem] = meta
    return cards


def check_card(card: dict, cards: dict, series: set[str], rep: Report) -> None:
    where = card["_path"]
    ctype = card.get("type")
    for field in COMMON_REQUIRED + TYPE_REQUIRED.get(ctype, []):
        if card.get(field) in (None, "", []):
            rep.error(where, f"missing required field `{field}`")
    for ch in card.get("chapters") or []:
        if ch not in VALID_CHAPTERS:
            rep.error(where, f"unknown chapter {ch!r}")
    summary = card.get("summary") or ""
    if isinstance(summary, str) and summary.count(". ") > 1:
        rep.warn(where, "summary looks longer than one sentence")

    links = card.get("links") or {}
    if not isinstance(links, dict):
        rep.error(where, "`links` must be a map of relation -> [ids]")
        links = {}
    for rel, targets in links.items():
        if rel not in RELATIONS:
            rep.error(where, f"unknown relation `{rel}`")
        if not isinstance(targets, list):
            rep.error(where, f"links.{rel} must be a list")
            continue
        for t in targets:
            if ":" in str(t):
                if not str(t).startswith("st:"):
                    rep.warn(where, f"cross-book link {t} (not checked)")
                    continue
                t = str(t)[3:]
            if t not in cards:
                rep.error(where, f"links.{rel} -> unknown card `{t}`")
            elif t == card.get("id"):
                rep.error(where, f"links.{rel} points at itself")
    for s in card.get("series") or []:
        if s not in series:
            rep.error(where, f"series concept `{s}` not in series-concepts.yaml")

    body = card["_body"]
    for section in TYPE_SECTIONS.get(ctype, []):
        if not re.search(rf"^## {re.escape(section)}\s*$", body, re.MULTILINE):
            rep.error(where, f"missing body section `## {section}`")
    if len(body.strip()) < 80:
        rep.warn(where, "body is very short")

    # Costume lint: everywhere except the fields allowed to keep the voice.
    # Fenced code is exempt: it has to match the book's real model and scripts.
    texts = [("body", re.sub(r"```.*?```", "", body, flags=re.DOTALL))]
    for k, v in card.items():
        if k.startswith("_") or k in COSTUME_OK_FIELDS:
            continue
        texts.append((k, yaml.safe_dump(v, allow_unicode=True) if not isinstance(v, str) else v))
    for name, text in texts:
        hit = COSTUME.search(text)
        if hit:
            rep.error(where, f"costume word {hit.group(0)!r} in `{name}`")

    if ctype == "archetype" or "structure" in card:
        check_structure(card, rep)


def check_structure(card: dict, rep: Report) -> None:
    where = card["_path"]
    st = card.get("structure") or {}
    variables = st.get("variables") or []
    links = st.get("links") or []
    loops = st.get("loops") or []
    vset = set(variables)
    if len(vset) != len(variables):
        rep.error(where, "structure: duplicate variable")
    edge: dict[tuple[str, str], str] = {}
    exogenous = set()
    for ln in links:
        if ln.get("exogenous"):
            exogenous.add((ln.get("from"), ln.get("to")))
        a, b, pol = ln.get("from"), ln.get("to"), str(ln.get("polarity"))
        for v in (a, b):
            if v not in vset:
                rep.error(where, f"structure: link uses undeclared variable {v!r}")
        if pol not in {"+", "-"}:
            rep.error(where, f"structure: link {a} -> {b} has polarity {pol!r}")
        edge[(a, b)] = pol
    if not loops:
        rep.error(where, "structure: no loops declared")
    used = set()
    for lp in loops:
        path = lp.get("path") or []
        lid = lp.get("id", "?")
        if len(path) < 2:
            rep.error(where, f"structure: loop {lid} path too short")
            continue
        minus = 0
        closed = True
        for a, b in zip(path, path[1:] + path[:1]):
            used.add((a, b))
            if (a, b) not in edge:
                rep.error(where, f"structure: loop {lid} needs link {a} -> {b}, not declared")
                closed = False
            elif edge[(a, b)] == "-":
                minus += 1
        if closed:
            actual = "R" if minus % 2 == 0 else "B"
            if lp.get("type") != actual:
                rep.error(
                    where,
                    f"structure: loop {lid} declared {lp.get('type')} but has {minus} minus links, so it is {actual}",
                )
    for e in edge:
        if e not in used and e not in exogenous:
            rep.warn(where, f"structure: link {e[0]} -> {e[1]} is on no declared loop")


def check_evals(bundle: Path, cards: dict, rep: Report) -> list[dict]:
    items: list[dict] = []
    seen: set[str] = set()
    for path in sorted((bundle / "evals").glob("*.yaml")):
        rel = str(path.relative_to(bundle))
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        if not isinstance(data, list):
            rep.error(rel, "eval file must be a list of items")
            continue
        for it in data:
            where = f"{rel}#{it.get('id', '?')}"
            for f in EVAL_REQUIRED:
                if not it.get(f):
                    rep.error(where, f"missing `{f}`")
            if it.get("id") in seen:
                rep.error(where, "duplicate eval id")
            seen.add(it.get("id"))
            if it.get("kind") not in EVAL_KINDS:
                rep.error(where, f"unknown kind {it.get('kind')!r}")
            for u in it.get("uses") or []:
                if u not in cards:
                    rep.error(where, f"uses unknown card `{u}`")
            text = json.dumps(it, ensure_ascii=False)
            hit = COSTUME.search(text)
            if hit:
                rep.error(where, f"costume word {hit.group(0)!r}")
            it["_file"] = rel
            items.append(it)
    return items


def build_graph(cards: dict) -> dict:
    nodes = []
    edges = set()
    for cid, c in sorted(cards.items()):
        nodes.append({
            "id": f"st:{cid}",
            "type": c["type"],
            "title": c["title"],
            "summary": c["summary"],
            "chapters": c["chapters"],
            "path": c["_path"],
            "series": c.get("series") or [],
        })
        for rel, targets in (c.get("links") or {}).items():
            for t in targets:
                tid = t if ":" in t else f"st:{t}"
                edges.add((f"st:{cid}", rel, tid))
                if rel in SYMMETRIC:
                    edges.add((tid, rel, f"st:{cid}"))
        for s in c.get("series") or []:
            edges.add((f"st:{cid}", "instance-of", f"series:{s}"))
    return {
        "nodes": nodes,
        "edges": [{"source": a, "relation": r, "target": b} for a, r, b in sorted(edges)],
    }


def write_turtle(graph: dict, series: dict, out: Path) -> None:
    def lit(s: str) -> str:
        return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'

    def iri(x: str) -> str:
        pfx, local = x.split(":", 1)
        return f"{pfx}:{local}"

    lines = [
        "@prefix st: <https://badass-data-science.github.io/supervillains/st/> .",
        "@prefix series: <https://badass-data-science.github.io/supervillains/series/> .",
        "@prefix rel: <https://badass-data-science.github.io/supervillains/rel/> .",
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "",
    ]
    for sid, s in series.items():
        lines.append(f"series:{sid} rdfs:label {lit(s['title'])} ; rdfs:comment {lit(s['summary'])} .")
    for n in graph["nodes"]:
        lines.append(
            f"{iri(n['id'])} a rel:{n['type'].capitalize()} ; rdfs:label {lit(n['title'])} ; "
            f"rdfs:comment {lit(n['summary'])} ; rel:path {lit(n['path'])} ."
        )
    for e in graph["edges"]:
        lines.append(f"{iri(e['source'])} rel:{e['relation'].replace('-', '_')} {iri(e['target'])} .")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_index(cards: dict, evals: list[dict], out: Path) -> None:
    lines = [
        "# Index",
        "",
        "Generated by `tools/build_bundle.py`; don't edit by hand. Every card in the bundle, by type, with its one-line summary and home chapter.",
        "",
    ]
    for type_name, folder in TYPES.items():
        group = sorted((c for c in cards.values() if c["type"] == type_name), key=lambda c: c["title"].lower())
        if not group:
            continue
        lines += [f"## {folder.capitalize()} ({len(group)})", ""]
        for c in group:
            lines.append(f"- [{c['title']}]({c['_path']}) (Ch. {c['chapters'][0]}): {c['summary']}")
        lines.append("")
    kinds = defaultdict(int)
    for it in evals:
        kinds[it["kind"]] += 1
    lines += [
        f"## Evals ({len(evals)})",
        "",
        "In `evals/`: " + ", ".join(f"{k} {v}" for k, v in sorted(kinds.items())) + ".",
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str]) -> int:
    bundle = Path(argv[1]).resolve() if len(argv) > 1 else DEFAULT_BUNDLE
    rep = Report()
    series = {}
    if SERIES_FILE.exists():
        series = {s["id"]: s for s in yaml.safe_load(SERIES_FILE.read_text(encoding="utf-8")) or []}
    cards = load_cards(bundle, rep)
    for c in cards.values():
        check_card(c, cards, set(series), rep)
    evals = check_evals(bundle, cards, rep)

    # Every card path SKILL.md routes to must exist.
    skill = bundle / "SKILL.md"
    if skill.exists():
        for ref in sorted(set(re.findall(r"`((?:%s)/[a-z0-9-]+\.md)`" % "|".join(TYPES.values()), skill.read_text(encoding="utf-8")))):
            if not (bundle / ref).exists():
                rep.error("SKILL.md", f"routes to missing card {ref}")
        # Agent Skills cap the description at 1,024 characters; a longer one
        # may be truncated or rejected by the loader.
        head = skill.read_text(encoding="utf-8").split("---")
        meta = yaml.safe_load(head[1]) if len(head) > 2 else None
        desc = (meta or {}).get("description", "")
        if not desc:
            rep.error("SKILL.md", "frontmatter has no description")
        elif len(desc) > 1024:
            rep.error("SKILL.md", f"description is {len(desc)} characters; the limit is 1024")
    else:
        rep.warn("SKILL.md", "missing")

    # code/ mirrors the book's published code; warn if they have drifted apart.
    if CODE_SOURCE is not None and not CODE_SOURCE.is_dir():
        rep.warn("BUNDLE_CODE_SOURCE", f"{CODE_SOURCE} is not a folder; code drift not checked")
    elif CODE_SOURCE is not None and (bundle / "code").is_dir():
        for src in sorted(CODE_SOURCE.iterdir()):
            if src.suffix not in {".py", ".xmile", ".md"}:
                continue
            dst = bundle / "code" / src.name
            if not dst.exists():
                rep.warn(f"code/{src.name}", "missing copy of a file in BUNDLE_CODE_SOURCE")
            elif dst.read_bytes() != src.read_bytes():
                rep.warn(f"code/{src.name}", "differs from BUNDLE_CODE_SOURCE (copy it again)")

    # Orphans: a card nothing links to and that links to nothing is probably missing context.
    linked = set()
    for c in cards.values():
        for targets in (c.get("links") or {}).values():
            linked.update(t for t in targets if ":" not in t)
        if c.get("links"):
            linked.add(c["id"])
    for cid in sorted(set(cards) - linked):
        rep.warn(cards[cid]["_path"], "orphan card (no links in or out)")
    used = {u for it in evals for u in it.get("uses") or []}
    untested = sorted(cid for cid, c in cards.items() if cid not in used and c["type"] in {"procedure", "archetype"})
    for cid in untested:
        rep.warn(cards[cid]["_path"], "no eval exercises this card")

    for line in rep.warnings + rep.errors:
        print(line)
    counts = defaultdict(int)
    for c in cards.values():
        counts[c["type"]] += 1
    summary = ", ".join(f"{counts[t]} {t}" for t in TYPES)
    print(f"\n{len(cards)} cards ({summary}); {len(evals)} evals; "
          f"{len(rep.errors)} errors, {len(rep.warnings)} warnings")
    if rep.errors:
        return 1
    graph = build_graph(cards)
    (bundle / "graph.json").write_text(json.dumps(graph, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    write_turtle(graph, series, bundle / "graph.ttl")
    write_index(cards, evals, bundle / "INDEX.md")
    print(f"wrote graph.json ({len(graph['nodes'])} nodes, {len(graph['edges'])} edges), graph.ttl, INDEX.md")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
