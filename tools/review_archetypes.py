#!/usr/bin/env python3
"""Compare each archetype card's `structure` with the book's own causal loop diagram.

The book keeps each archetype figure's structure in a `.cld` file, checked
against the drawn figure in the book's own (private) repository. Copies of
those files live in `archetype-review/cld/`, so this script needs nothing
from the book. The bundle's archetype cards restate that structure with
neutral variable names. This script takes the proposed
renaming in `archetype-review/mappings.yaml` and checks, for each card:

1. every link: present in both, same polarity, delay on the same link;
2. every feedback loop (all elementary cycles, not just the labeled ones):
   present in both, same type by counting minus signs;
3. the card's own loop labels: each is a real cycle of the card's links, and
   its R/B label matches its minus-sign count;
4. independently of the proposed mapping, whether ANY renaming makes the two
   diagrams identical (signed links and delays), and whether the proposed
   one is among them.

A book variable the mapping leaves out with one link in and one link out is
"contracted": the card may draw its two links as one, whose polarity is the
product. That is reported, not silently accepted.

What it cannot check: whether a rename keeps the book's meaning. That is the
human part of the review, and each page leaves room for it.

Usage:
    python3 tools/review_archetypes.py           # write archetype-review/*.md
    python3 tools/review_archetypes.py --check   # print the summary; exit 1 on any difference
"""

from __future__ import annotations

import argparse
import itertools
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent / "systems-thinking"
REVIEW = HERE.parent / "archetype-review"
CLD_DIR = REVIEW / "cld"  # copies of the book's archetype .cld files

CLD_LINK = re.compile(r"^(.+?)\s*->\s*(.+?)\s*:\s*([+-])(.*)$")


# ---------------------------------------------------------------- parsing

def parse_cld(path: Path) -> dict:
    links, loops = {}, []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("loop:"):
            loops.append([v.strip() for v in line[5:].split(",")])
            continue
        m = CLD_LINK.match(line)
        if not m:
            raise ValueError(f"{path.name}: can't parse line: {line}")
        src, dst, pol, rest = m.groups()
        links[(src, dst)] = {"polarity": pol, "delay": "delay" in rest.split(), "delay_type": None}
    nodes = sorted({n for e in links for n in e})
    return {"nodes": nodes, "links": links, "loops": loops}


def load_card(card_id: str) -> tuple[dict, str]:
    text = (BUNDLE / "archetypes" / f"{card_id}.md").read_text(encoding="utf-8")
    _, front, body = text.split("---", 2)
    return yaml.safe_load(front), body


def card_graph(meta: dict) -> dict:
    s = meta["structure"]
    links = {}
    for l in s["links"]:
        links[(l["from"], l["to"])] = {"polarity": l["polarity"], "delay": "delay" in l,
                                       "delay_type": l.get("delay"), "exogenous": l.get("exogenous", False)}
    return {"nodes": list(s["variables"]), "links": links, "loops": s.get("loops", [])}


# ---------------------------------------------------------------- graph helpers

def cycles(nodes: list[str], links: dict) -> list[tuple[str, ...]]:
    """Every elementary cycle, each as a tuple starting at its smallest-index node."""
    order = {n: i for i, n in enumerate(nodes)}
    succ = {n: [d for (s, d) in links if s == n] for n in nodes}
    found = []

    def walk(start, node, path, seen):
        for nxt in succ[node]:
            if nxt == start:
                found.append(tuple(path))
            elif nxt not in seen and order[nxt] > order[start]:
                walk(start, nxt, path + [nxt], seen | {nxt})

    for n in nodes:
        walk(n, n, [n], {n})
    return found


def canon(cycle) -> tuple:
    """Rotation-independent form of a cycle, for comparing across graphs."""
    c = list(cycle)
    i = c.index(min(c))
    return tuple(c[i:] + c[:i])


def minus_count(cycle, links) -> int:
    return sum(links[(cycle[i], cycle[(i + 1) % len(cycle)])]["polarity"] == "-" for i in range(len(cycle)))


def loop_type(cycle, links) -> str:
    return "R" if minus_count(cycle, links) % 2 == 0 else "B"


def isomorphisms(a: dict, b: dict, with_delays: bool) -> list[dict]:
    """All renamings of a's nodes onto b's under which their signed links match exactly."""
    if len(a["nodes"]) != len(b["nodes"]) or len(a["links"]) != len(b["links"]):
        return []
    def sig(links, s, d):
        e = links.get((s, d))
        if e is None:
            return None
        return (e["polarity"], e["delay"]) if with_delays else e["polarity"]
    def degree(g, n):
        return (sum(1 for (s, _) in g["links"] if s == n), sum(1 for (_, d) in g["links"] if d == n))
    an, bn = a["nodes"], b["nodes"]
    found = []

    def extend(i, m, used):
        if i == len(an):
            found.append(dict(m))
            return
        x = an[i]
        for y in bn:
            if y in used or degree(a, x) != degree(b, y):
                continue
            ok = all(sig(a["links"], x, p) == sig(b["links"], y, m[p]) and
                     sig(a["links"], p, x) == sig(b["links"], m[p], y) for p in m)
            ok = ok and sig(a["links"], x, x) == sig(b["links"], y, y)
            if ok:
                m[x] = y
                extend(i + 1, m, used | {y})
                del m[x]

    extend(0, {}, set())
    return found


# ---------------------------------------------------------------- comparison

def compare(card: dict, book: dict, mapping: dict) -> dict:
    """Translate the book graph into card names and compare."""
    inv = {}
    for c, b in mapping.items():
        if b not in book["nodes"]:
            raise ValueError(f"mapping names book variable {b!r}, which isn't in the .cld")
        inv[b] = c
    unknown = [c for c in mapping if c not in card["nodes"]]
    if unknown:
        raise ValueError(f"mapping names card variables not in the card: {unknown}")

    book_only_nodes = [n for n in book["nodes"] if n not in inv]
    # Contract book-only nodes with exactly one link in and one out, both mapped.
    contracted, absorbed = [], set()
    tlinks = {}
    for (s, d), e in book["links"].items():
        if s in inv and d in inv:
            tlinks[(inv[s], inv[d])] = dict(e, via=None)
    for n in book_only_nodes:
        ins = [(s, d) for (s, d) in book["links"] if d == n]
        outs = [(s, d) for (s, d) in book["links"] if s == n]
        if len(ins) == 1 and len(outs) == 1 and ins[0][0] in inv and outs[0][1] in inv:
            e1, e2 = book["links"][ins[0]], book["links"][outs[0]]
            pol = "+" if (e1["polarity"] == e2["polarity"]) else "-"
            key = (inv[ins[0][0]], inv[outs[0][1]])
            tlinks[key] = {"polarity": pol, "delay": e1["delay"] or e2["delay"], "delay_type": None, "via": n}
            contracted.append({"node": n, "from": ins[0][0], "to": outs[0][1],
                               "pols": (e1["polarity"], e2["polarity"]), "net": pol})
            absorbed.add(n)
    leftover_nodes = [n for n in book_only_nodes if n not in absorbed]
    book_only_links = [(s, d, e) for (s, d), e in book["links"].items()
                       if (s in leftover_nodes or d in leftover_nodes)]

    rows, problems = [], []
    keys = list(card["links"]) + [k for k in tlinks if k not in card["links"]]
    for k in keys:
        c, b = card["links"].get(k), tlinks.get(k)
        if c and b:
            status = []
            if c["polarity"] != b["polarity"]:
                status.append("polarity differs")
            if c["delay"] != b["delay"]:
                status.append("delay differs")
            if b.get("via"):
                status.append(f"book draws two links via '{b['via']}'")
            rows.append((k, c, b, "; ".join(status) or "match"))
            if c["polarity"] != b["polarity"] or c["delay"] != b["delay"]:
                problems.append(f"{k[0]} → {k[1]}: {'; '.join(status)}")
        elif c:
            rows.append((k, c, None, "exogenous; card only" if c.get("exogenous") else "card only"))
            problems.append(f"{k[0]} → {k[1]}: in the card, not the book")
        else:
            rows.append((k, None, b, "book only"))
            problems.append(f"{k[0]} → {k[1]}: in the book, not the card")

    # Loops: all elementary cycles in each, compared in card names.
    tnodes = [n for n in card["nodes"] if any(n in k for k in tlinks)] + \
             [n for n in {x for k in tlinks for x in k} if n not in card["nodes"]]
    ccyc = {canon(c): loop_type(c, card["links"]) for c in cycles(card["nodes"], card["links"])}
    bcyc = {canon(c): loop_type(c, tlinks) for c in cycles(tnodes, tlinks)}
    loop_rows = []
    for k in sorted(set(ccyc) | set(bcyc), key=lambda c: (len(c), c)):
        ct, bt = ccyc.get(k), bcyc.get(k)
        st = "match" if ct == bt else ("card only" if bt is None else "book only" if ct is None else "type differs")
        loop_rows.append((k, ct, bt, st))
        if st != "match":
            problems.append(f"loop {' → '.join(k)}: {st}")
    # Loops through the book-only nodes that weren't contracted.
    if leftover_nodes:
        full = cycles(book["nodes"], book["links"])
        extra = [c for c in full if any(n in leftover_nodes for n in c)]
    else:
        extra = []

    # Independent check: does ANY renaming make the comparable parts identical?
    comparable = {"nodes": [n for n in book["nodes"] if n in inv],
                  "links": {k: v for k, v in book["links"].items() if k[0] in inv and k[1] in inv}}
    # include contracted links as single edges between mapped book nodes
    for cinfo in contracted:
        e1 = book["links"][(cinfo["from"], cinfo["node"])]
        e2 = book["links"][(cinfo["node"], cinfo["to"])]
        comparable["links"][(cinfo["from"], cinfo["to"])] = {"polarity": cinfo["net"], "delay": e1["delay"] or e2["delay"]}
    card_cmp = {"nodes": card["nodes"], "links": {k: v for k, v in card["links"].items() if not v.get("exogenous")}}
    card_cmp["nodes"] = [n for n in card["nodes"] if any(n in k for k in card_cmp["links"])]
    isos = isomorphisms(card_cmp, comparable, with_delays=True)
    proposed = {c: mapping[c] for c in card_cmp["nodes"] if c in mapping}
    return {"rows": rows, "loop_rows": loop_rows, "problems": problems, "contracted": contracted,
            "leftover_nodes": leftover_nodes, "book_only_links": book_only_links, "extra_cycles": extra,
            "isomorphisms": isos, "proposed_is_iso": proposed in isos,
            "restricted": bool(book_only_nodes) or len(card_cmp["nodes"]) != len(card["nodes"])}


def check_card_loops(card: dict) -> list[str]:
    """The card's own labeled loops: real cycles, R/B label matching the minus count."""
    out = []
    for l in card["loops"]:
        p = l["path"]
        missing = [(p[i], p[(i + 1) % len(p)]) for i in range(len(p)) if (p[i], p[(i + 1) % len(p)]) not in card["links"]]
        if missing:
            out.append(f"{l['id']}: path isn't a cycle of the card's links (missing {missing})")
            continue
        t = loop_type(p, card["links"])
        if t != l["type"]:
            out.append(f"{l['id']}: labeled {l['type']}, but {minus_count(p, card['links'])} minus signs make it {t}")
    return out


# ---------------------------------------------------------------- report

def fmt_link(k, e):
    if not e:
        return "—"
    d = ""
    if e.get("delay"):
        d = f", delay ({e['delay_type']})" if e.get("delay_type") else ", delay"
    return f"{k[0]} → {k[1]} ({e['polarity']}{d})"


def section(body: str, heading: str) -> str:
    m = re.search(rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1).strip() if m else ""


def page(card_id, spec, meta, body, results, own_loop_issues) -> str:
    title = meta["title"]
    L = [f"# Review: {title}", ""]
    L.append(f"Card: [`systems-thinking/archetypes/{card_id}.md`](../systems-thinking/archetypes/{card_id}.md)  ")
    L.append(f"Chapters: {', '.join(str(c) for c in meta.get('chapters', []))}  ")
    L.append(f"Attribution on the card: {meta.get('attribution', '—')}")
    L.append("")
    L.append(f"**Summary on the card:** {meta['summary']}")
    L.append("")
    L.append(f"**Diagnostic question:** {meta.get('diagnostic_question', '—')}")
    L.append("")
    if spec.get("figure"):
        m = re.match(r"ch(\d+)-img(\d+)", spec["figure"])
        L.append(f"The book's figure: Figure {int(m[1])}.{m[2]}." if m else f"The book's figure: {spec['figure']}.")
        L.append("")

    L.append("## Machine check")
    L.append("")
    if own_loop_issues:
        L.append("**The card's own loop labels:** " + "; ".join(own_loop_issues))
    else:
        L.append("**The card's own loop labels:** every labeled loop is a real cycle of the card's links, and its R/B label matches its minus-sign count.")
    L.append("")

    if not results:
        L.append(f"**No `.cld` in the book for this archetype**, so there's nothing to compare mechanically. Read the card's structure against {spec.get('compare_with', 'the book')}.")
        L.append("")
    for src, r in results:
        L.append(f"### Against `{src}`")
        L.append("")
        if not r["problems"]:
            L.append("**No differences:** every link, polarity, delay and loop matches under the proposed renaming.")
        else:
            L.append("**Differences found:**")
            L.append("")
            for p in r["problems"]:
                L.append(f"- {p}")
        L.append("")
        n = len(r["isomorphisms"])
        scope = " (comparing only the variables both share)" if r["restricted"] else ""
        if n:
            L.append(f"**Independent of the proposed names{scope}:** {n} renaming{'s' if n != 1 else ''} make{'s' if n == 1 else ''} the two diagrams identical, links, polarities and delays alike; "
                     + ("the proposed mapping is one of them." if r["proposed_is_iso"] else "**the proposed mapping is not one of them.**"))
            if n > 1:
                L.append(" More than one usually means the diagram is symmetric (A and B swap).")
        else:
            L.append(f"**Independent of the proposed names{scope}:** no renaming makes the two diagrams identical.")
        L.append("")
        if r["contracted"]:
            for c in r["contracted"]:
                L.append(f"- *Contracted:* the book draws `{c['from']}` → `{c['node']}` ({c['pols'][0]}) → `{c['to']}` ({c['pols'][1]}); "
                         f"the card draws one link with the same net polarity ({c['net']}). Decide whether dropping `{c['node']}` loses anything.")
            L.append("")
        if r["leftover_nodes"]:
            L.append(f"- *Book only:* {', '.join(f'`{n}`' for n in r['leftover_nodes'])}, with {len(r['book_only_links'])} links and {len(r['extra_cycles'])} loops through them. Decide whether the card's generalization drops anything.")
            L.append("")
        L.append("| Card link | Book link (in card names) | Result |")
        L.append("|---|---|---|")
        for k, c, b, st in r["rows"]:
            L.append(f"| {fmt_link(k, c)} | {fmt_link(k, b)} | {st} |")
        L.append("")
        L.append("All feedback loops (every cycle, labeled or not):")
        L.append("")
        L.append("| Loop | Card | Book |")
        L.append("|---|---|---|")
        for k, ct, bt, st in r["loop_rows"]:
            L.append(f"| {' → '.join(k)} | {ct or '—'} | {bt or '—'}{'' if st == 'match' else ' ⚠ ' + st} |")
        labeled = {canon(l["path"]) for l in meta["structure"]["loops"]}
        unlabeled = [k for k, *_ in r["loop_rows"] if k not in labeled]
        if unlabeled:
            L.append("")
            L.append(f"{len(unlabeled)} of these loop{'s are' if len(unlabeled) != 1 else ' is'} not among the card's labeled loops. They follow from the links; the card isn't wrong to leave them unlabeled, but check none of them changes the story.")
        L.append("")

    L.append("## Proposed renaming (judge each)")
    L.append("")
    if spec["sources"]:
        heads = " | ".join(f"Book: `{s['cld']}`" for s in spec["sources"])
        L.append(f"| Card variable | {heads} | Keeps the meaning? |")
        L.append("|---" * (len(spec["sources"]) + 2) + "|")
        for v in meta["structure"]["variables"]:
            cells = " | ".join(s["map"].get(v, "—") for s in spec["sources"])
            L.append(f"| {v} | {cells} | ☐ |")
    else:
        L.append(f"No book diagram to map to. Judge the variable names against {spec.get('compare_with', 'the book')}.")
        L.append("")
        for v in meta["structure"]["variables"]:
            L.append(f"- ☐ {v}")
    L.append("")

    sig = section(body, "Signature")
    L.append("## The card's own description (check it agrees with the structure)")
    L.append("")
    L.append("> " + sig.replace("\n", "\n> ") if sig else "*(no Signature section)*")
    L.append("")

    if not spec["sources"]:
        L.append("## The card's structure, to read against the book")
        L.append("")
        L.append(f"Compare with {spec.get('compare_with', 'the book')}. The book's text isn't reproduced here.")
        L.append("")
        L.append("")
        for l in meta["structure"]["links"]:
            k = (l["from"], l["to"])
            L.append(f"- {fmt_link(k, card_graph(meta)['links'][k])}{' — exogenous (feeds the loop from outside)' if l.get('exogenous') else ''}")
        L.append("")

    L.append("## Your verdict")
    L.append("")
    L.append("- ☐ Structure matches the book")
    L.append("- ☐ Every rename keeps the meaning")
    L.append("- ☐ The card's description agrees with its structure")
    L.append("- Notes:")
    L.append("")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="print the summary only; exit 1 on any difference")
    args = ap.parse_args()

    specs = yaml.safe_load((REVIEW / "mappings.yaml").read_text(encoding="utf-8"))
    cards = sorted(p.stem for p in (BUNDLE / "archetypes").glob("*.md"))
    missing = [c for c in cards if c not in specs]
    if missing:
        print(f"no mapping for: {missing}", file=sys.stderr)
        return 2

    summary, any_diff = [], False
    for cid in cards:
        spec = specs[cid]
        meta, body = load_card(cid)
        card = card_graph(meta)
        own = check_card_loops(card)
        results = []
        for s in spec["sources"]:
            book = parse_cld(CLD_DIR / s["cld"])
            results.append((s["cld"], compare(card, book, s["map"])))
        diffs = sum(len(r["problems"]) for _, r in results) + len(own)
        any_diff |= diffs > 0
        if not results:
            status = "no book diagram; read against " + spec.get("compare_with", "the book")
        elif diffs == 0:
            status = "matches" + (" (both diagrams)" if len(results) > 1 else "")
            notes = [f"merges `{c['node']}` into one link" for _, r in results for c in r["contracted"]]
            notes += [f"leaves out {', '.join(f'`{n}`' for n in r['leftover_nodes'])}" for _, r in results if r["leftover_nodes"]]
            if notes:
                status += "; simplifies the book: " + "; ".join(notes)
        else:
            status = f"{diffs} difference{'s' if diffs != 1 else ''}"
        summary.append((cid, meta["title"], status, results))
        if not args.check:
            (REVIEW / f"{cid}.md").write_text(page(cid, spec, meta, body, results, own), encoding="utf-8")

    for cid, title, status, _ in summary:
        print(f"{title:42} {status}")
    if not args.check:
        write_readme(summary)
    return 1 if any_diff else 0


def write_readme(summary):
    L = ["# Archetype structure review", "",
         "Each archetype card in `systems-thinking/archetypes/` carries a `structure` block: variables, signed links, delays and labeled loops. The cards were written by an AI agent from the book's figures and Toolkit boxes, and until this review nobody else had compared them with the book.",
         "",
         "The book keeps each archetype figure's structure in a `.cld` file, checked against the drawn figure and against Kim and Senge in the book's October 2026 archetype passes. Copies of those files are in [`cld/`](cld/). So the comparison splits in two:",
         "",
         "1. **Mechanical, done by `tools/review_archetypes.py`:** under the proposed renaming in `mappings.yaml`, every link, polarity, delay and feedback loop (every cycle, not just the labeled ones) in the card against the book's `.cld`. It also searches for *any* renaming that makes the two diagrams identical, independently of the proposed one, so a wrong proposal can't hide a mismatch.",
         "2. **Judgment, yours:** whether each neutral name keeps the book's meaning, whether a simplification the card makes loses anything, and whether the card's prose agrees with its structure. Each page has checkboxes for these.",
         "",
         "**Start with [OBSERVATIONS.md](OBSERVATIONS.md):** four things the agent noticed while reading these pages that no script could flag, each a question for you.",
         "",
         "## Pages", "",
         "| Archetype | Machine check | Page |", "|---|---|---|"]
    for cid, title, status, _ in summary:
        L.append(f"| {title} | {status} | [{cid}.md]({cid}.md) |")
    L += ["",
          "## How to review a page", "",
          "1. Look at the book's figure, then the **Machine check**. \"No differences\" means the card is the book's diagram renamed; anything else is listed with what to decide.",
          "2. Go down the **Proposed renaming** table and tick each name that keeps the meaning. This is the part no script can check.",
          "3. Read the card's **Signature** and check it says what the structure shows.",
          "4. Tick the verdict, add notes, and commit. Anything you want changed in a card, note it on its page; the agent can then fix the card and rerun the check.",
          "",
          "## Rerunning", "",
          "```bash",
          "python3 tools/review_archetypes.py          # rewrite these pages (overwrites ticks and notes!)",
          "python3 tools/review_archetypes.py --check  # summary only; exit 1 on any difference",
          "```",
          "",
          "Rewriting the pages overwrites any ticks and notes on them, so copy those somewhere first, or use `--check` after editing a card.",
          ""]
    (REVIEW / "README.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
