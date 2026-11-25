# Retest, 2026-11-23: routing fixes on new held-out items

The 2026-11-22 retest left two follow-ups: an incident follow-up where the skill didn't load (fresh-004), and a contested problem definition where it loaded but the answer jumped to a stock-and-flow model before agreeing on the problem (fresh-029). Commit `fecf19f` changed `SKILL.md` for both:

- **Description:** adds "following up an incident or postmortem" and "groups disagree on what it is". To stay within the 1,024-character limit it drops "hand-iterating", "Sobol" and "checked loop structures" (now "checked loops").
- **Routing table:** two new rows, one for incidents under pressure (`pressure-shrinks-the-iceberg`, `iceberg-analysis`) and one for contested problems (`hard-and-soft-systems-thinking`, `soft-systems-methodology`, `catwoe`, `tame-messy-wicked-problems`).

## Setup

- **Held-out items:** 30 new items (`systems-thinking/evals/held-2026-11-23.yaml`), written by a separate Opus session that saw the cards and all earlier evals but not `SKILL.md`, using `item-generation-prompt.txt`. That prompt is last time's with one added paragraph asking for at least five incident or postmortem items, five where people disagree about what the problem is, and four on simulation or sensitivity analysis. The items were committed (`e0ad1e2`) before any answers were run, and weren't edited.
- **Three conditions,** all run fresh: `new` (current `SKILL.md`), `prev` (`SKILL.md` before `fecf19f`), `without` (no skill). Sonnet answers, Opus grades blind, as before. Cost $8.03 for the run plus $2.42 to write the items.

## Results

| | New | Previous | No skill |
|---|---|---|---|
| Mean score | **0.85** | 0.82 | 0.70 |
| Skill loaded | 30 of 30 | 30 of 30 | 0 |
| Better / worse than no skill | 19 / 0 | 18 / 0 | |
| Mean gain over no skill (95% interval) | +0.15 (+0.10 to +0.21) | +0.13 (+0.08 to +0.18) | |

**New vs. previous directly:** +0.03 (95% paired bootstrap −0.01 to +0.06), better on 8 items, worse on 3. Not distinguishable from no difference at this sample size.

## What it shows

- **Loading didn't separate the two descriptions.** The previous description loaded on all 30, including the six incident and postmortem items. So this batch can't show whether the incident wording fixes fresh-004's kind of miss; the generator's incident items evidently read as systems questions with either description. The trimmed trigger words ("Sobol", "hand-iterating") cost nothing measurable: the simulation and sensitivity items loaded and scored the same under both.
- **The new routing rows are used and point the right way.** With the new `SKILL.md`, answers opened the contested-problem cards on held-007, -009 and -010, and `pressure-shrinks-the-iceberg` on held-004 and -005; with the previous one, none of them did. The clearest gain is held-007 (school absenteeism, every group defines the problem differently): 0.62 against 0.38. Held-009 and -010 also rose (0.88 against 0.75 each).
- **The three items where new scored lower** (held-008, -012, -026) weren't in the areas the fix changed; with one run per item and a 0.125 rubric step, single-item drops of that size are within noise.

## Caveats

Same as before: one run per item, a model grader, and a rubric written in the book's vocabulary by a same-family model. The added paragraph in the item prompt steered the batch toward the areas the fix changed, which makes it a fair test of those areas but not a random sample of everything users ask.

`out/` holds every answer and grade; `summary.md` has per-item scores.
