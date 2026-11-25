#!/usr/bin/env python3
"""Plant known errors in copies of archetype structures and confirm review_archetypes.py reports each one."""
import copy
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import review_archetypes as ra  # noqa: E402

specs = yaml.safe_load((ra.REVIEW / "mappings.yaml").read_text(encoding="utf-8"))


def setup(cid, i=0):
    meta, _ = ra.load_card(cid)
    s = specs[cid]["sources"][i]
    return ra.card_graph(meta), ra.parse_cld(ra.CLD_DIR / s["cld"]), dict(s["map"])


failures = 0


def expect(name, cond):
    global failures
    print(("ok   " if cond else "FAIL ") + name)
    failures += not cond


# 1. Baseline: Fixes That Fail matches.
card, book, m = setup("fixes-that-fail")
r = ra.compare(card, book, m)
expect("baseline Fixes That Fail has no differences", not r["problems"] and r["proposed_is_iso"])

# 2. Flipped polarity in the card.
c2 = copy.deepcopy(card)
c2["links"][("quick fix", "side effect")]["polarity"] = "-"
r = ra.compare(c2, book, m)
expect("flipped polarity reported", any("polarity differs" in p for p in r["problems"]))
expect("flipped polarity changes a loop's type", any("type differs" in p for p in r["problems"]))
expect("flipped polarity: no renaming matches", not r["isomorphisms"])

# 3. Delay moved to another link.
c3 = copy.deepcopy(card)
c3["links"][("side effect", "underlying damage")]["delay"] = False
c3["links"][("quick fix", "side effect")]["delay"] = True
r = ra.compare(c3, book, m)
expect("moved delay reported on both links", sum("delay differs" in p for p in r["problems"]) == 2)

# 4. A link missing from the card.
c4 = copy.deepcopy(card)
del c4["links"][("underlying damage", "performance")]
r = ra.compare(c4, book, m)
expect("missing link reported", any("in the book, not the card" in p for p in r["problems"]))
expect("missing link: the book's R loop reported as book only", any("loop" in p and "book only" in p for p in r["problems"]))

# 5. A wrong (swapped) mapping on a structure that does match.
m5 = dict(m)
m5["quick fix"], m5["immediate relief"] = m["immediate relief"], m["quick fix"]
r = ra.compare(card, book, m5)
expect("swapped mapping reported", bool(r["problems"]))
expect("swapped mapping: a correct renaming still exists, and the proposal isn't it",
       r["isomorphisms"] and not r["proposed_is_iso"])

# 6. Card loop mislabeled.
c6 = copy.deepcopy(card)
c6["loops"] = [dict(l, type="B") if l["id"] == "R1" else l for l in c6["loops"]]
expect("mislabeled card loop reported", any("labeled B" in x for x in ra.check_card_loops(c6)))

# 7. Contraction: Accidental Adversaries merges a book node; a wrong net polarity must still show.
card, book, m = setup("accidental-adversaries")
r = ra.compare(card, book, m)
expect("contraction detected", [c["node"] for c in r["contracted"]] == ["held shipments"])
c7 = copy.deepcopy(card)
c7["links"][("B's local fix", "A's success")]["polarity"] = "+"
r = ra.compare(c7, book, m)
expect("contracted link with wrong net polarity reported", any("polarity differs" in p for p in r["problems"]))

sys.exit(1 if failures else 0)
