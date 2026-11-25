# Archetype structure review

Each archetype card in `systems-thinking/archetypes/` carries a `structure` block: variables, signed links, delays and labeled loops. The cards were written by an AI agent from the book's figures and Toolkit boxes, and until this review nobody else had compared them with the book.

The book keeps each archetype figure's structure in a `.cld` file, checked against the drawn figure and against Kim and Senge in the book's October 2026 archetype passes. Copies of those files are in [`cld/`](cld/). So the comparison splits in two:

1. **Mechanical, done by `tools/review_archetypes.py`:** under the proposed renaming in `mappings.yaml`, every link, polarity, delay and feedback loop (every cycle, not just the labeled ones) in the card against the book's `.cld`. It also searches for *any* renaming that makes the two diagrams identical, independently of the proposed one, so a wrong proposal can't hide a mismatch.
2. **Judgment, yours:** whether each neutral name keeps the book's meaning, whether a simplification the card makes loses anything, and whether the card's prose agrees with its structure. Each page has checkboxes for these.

**Start with [OBSERVATIONS.md](OBSERVATIONS.md):** four things the agent noticed while reading these pages that no script could flag, each a question for you.

## Pages

| Archetype | Machine check | Page |
|---|---|---|
| Accidental Adversaries | matches; simplifies the book: merges `held shipments` into one link | [accidental-adversaries.md](accidental-adversaries.md) |
| Attractiveness Principle | matches | [attractiveness-principle.md](attractiveness-principle.md) |
| Drift to Low Performance | matches | [drift-to-low-performance.md](drift-to-low-performance.md) |
| Escalation | matches | [escalation.md](escalation.md) |
| Fixes That Fail | matches | [fixes-that-fail.md](fixes-that-fail.md) |
| Growth and Underinvestment | matches | [growth-and-underinvestment.md](growth-and-underinvestment.md) |
| Limits to Growth | no book diagram; read against Chapter 13, "The Wall Everyone Eventually Hits" | [limits-to-growth.md](limits-to-growth.md) |
| Shifting the Burden | matches | [shifting-the-burden.md](shifting-the-burden.md) |
| Shifting the Burden to the Intervenor | matches (both diagrams) | [shifting-the-burden-to-the-intervenor.md](shifting-the-burden-to-the-intervenor.md) |
| Success to the Successful | matches | [success-to-the-successful.md](success-to-the-successful.md) |
| Tragedy of the Commons | matches; simplifies the book: leaves out `Operation C lair gains`, `Operation C overbuilding` | [tragedy-of-the-commons.md](tragedy-of-the-commons.md) |

## How to review a page

1. Look at the book's figure, then the **Machine check**. "No differences" means the card is the book's diagram renamed; anything else is listed with what to decide.
2. Go down the **Proposed renaming** table and tick each name that keeps the meaning. This is the part no script can check.
3. Read the card's **Signature** and check it says what the structure shows.
4. Tick the verdict, add notes, and commit. Anything you want changed in a card, note it on its page; the agent can then fix the card and rerun the check.

## Rerunning

```bash
python3 tools/review_archetypes.py          # rewrite these pages (overwrites ticks and notes!)
python3 tools/review_archetypes.py --check  # summary only; exit 1 on any difference
```

Rewriting the pages overwrites any ticks and notes on them, so copy those somewhere first, or use `--check` after editing a card.
