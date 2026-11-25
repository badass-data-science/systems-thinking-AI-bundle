# Retest, 2026-11-22: revised SKILL.md description on held-out items

The first eval run (`../2026-11-21-sonnet-graded-by-opus/`) found that Sonnet loaded the skill on only 37 of 55 items, and that when it didn't, the skill made no difference. This run tests a revised `description` in `SKILL.md` that names those situations in plain language and says to load the skill even when an answer seems obvious.

## Setup

- **Held-out items:** 30 new items (`systems-thinking/evals/fresh-2026-11-22.yaml`), written by a separate Opus session from the cards and the existing evals, using the prompt in `item-generation-prompt.txt`. That session didn't see `SKILL.md` or the list of missed items. At least 20 of the prompts describe a situation in plain language without naming a systems-thinking term. The items were committed (`ca0c191`) before the description was changed and were not edited.
- **Three conditions,** otherwise as in the first run (Sonnet answering, Opus grading blind):
  - `new`: the revised description;
  - `old`: the original description;
  - `without`: no skill.
- The `old` and `without` answers on the fresh items, and all `old` and `without` answers on the 18 earlier misses, come from the same setup as the first run. Only `new` was run for this retest. Total cost about $10.

## Results on the 30 held-out items

| | New description | Old description | No skill |
|---|---|---|---|
| Mean score | **0.84** | 0.79 | 0.70 |
| Skill loaded | **29 of 30** | 19 of 30 | 0 |
| Better / worse than no skill | 18 / 0 | 17 / 4 | |
| Mean gain over no skill (95% interval) | +0.14 (+0.09 to +0.20) | +0.09 (+0.03 to +0.15) | |

Comparing the new description directly with the old one gives +0.05 (95% interval +0.01 to +0.10). The new one is better on 8 items and worse on 3, each of the 3 by one rubric point.

## Results on the 18 items the old description missed

The revised description was written with these in mind, so they show the fix works where intended but are not a fair test of it:

| | New | Old | No skill |
|---|---|---|---|
| Mean score | 0.97 | 0.89 | 0.88 |
| Skill loaded | 17 of 18 | 0 of 18 | 0 |

## What's left

- **One held-out miss:** fresh-004, a "the CEO wants a plan tonight" incident follow-up after a bad release. Arguably the skill should load there, since the iceberg analysis is the point of the item. Adding incident follow-ups and postmortems to the description would be the fix, but it should be tested on new items again, not on this one.
- **Loaded but still weak:** fresh-029, a hospital "discharge problem" where each group defines the problem differently. With the skill, the answer still jumped to a stock-and-flow sketch before agreeing on what the problem is (0.25). `SKILL.md`'s routing table has no row for "people disagree about what the problem is". One pointing to `catwoe`, the rich picture and `hard-and-soft-systems-thinking` would likely help.
- **Same caveats as the first run:** a model grader, one run per item, and a rubric written in the book's vocabulary. This time the rubric's author is a different session from the author of the cards, but it is still the same model family.

`fresh/` and `misses/` each hold every answer, grade and per-item summary.
