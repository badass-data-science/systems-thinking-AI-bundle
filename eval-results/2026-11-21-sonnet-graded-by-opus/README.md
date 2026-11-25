# Eval run, 2026-11-21: Sonnet with and without the skill, graded by Opus

Run with `tools/run_evals.py` (Claude Code 2.1.330, headless `claude -p`). Total cost $6.79.

## Setup

- **Answering model:** Claude Sonnet, run once per item in each of two scratch folders that differ only in whether the skill is installed as a project skill. Neither run was told the skill exists. Tools: Read, Glob, Grep and Skill.
- **Grader:** Claude Opus, in a separate session with no tools. It saw the prompt, the item's `expected` points and `pitfalls`, and one answer, but not which condition produced the answer. It scored each expected point 0, 0.5 or 1 and was told to credit substance in any wording.
- **Score:** the share of an item's expected points earned. The mean is over all 55 items.

## Results

| | With skill | Without |
|---|---|---|
| Mean score | 0.94 | 0.82 |
| Items better / worse / tied with skill | 27 / 2 / 26 | |
| Pitfalls committed | 0 | 1 |

The mean difference is +0.12, with a 95% paired bootstrap interval of +0.08 to +0.17.

**Split by whether the model actually loaded the skill:**

| | Items | With | Without | Difference | Better / worse |
|---|---|---|---|---|---|
| Skill loaded | 37 | 0.96 | 0.78 | +0.18 | 26 / 0 |
| Skill available but not loaded | 18 | 0.89 | 0.88 | +0.01 | 1 / 2 |

When the skill wasn't loaded, the two conditions were the same model doing the same thing, so that row is the noise floor. It is close to zero. When the skill was loaded, the answers were better on 26 items and worse on none. The biggest gains were on procedure items (0.98 against 0.81) and recognition items (0.95 against 0.75).

`summary.md` has per-item scores. `out/` has every answer (with the tools it called) and every grade (with the grader's reason for each point).

## How far to trust this

- **The rubric was written by the same agent that wrote the cards,** in the book's vocabulary. The grader was told to credit the substance of a point in any wording, but answers that use the book's terms may still be easier to match. This is the main reason the gain may be overstated.
- **The grader is from the same model family,** not a person.
- **One run per item per condition.** There are no repeats, so the item-level results are noisy. The split by loading suggests the noise is small on average.
- **Loading wasn't random.** The model skipped the skill mostly where it already scored well without it (0.88), so the 18 unloaded items are easier than average. The +0.18 applies to the items where the model chose to use the skill, not to every item.

## What it suggests changing

- **The skill wasn't loaded on 18 items:** ai-002, ai-010, ai-011, ai-012, ai-014, arch-003, arch-005, found-004, found-005, found-010, found-011, found-012, and model-002, 005, 006, 007, 008 and 009. They cluster in modeling and validation questions (sensitivity analysis, calibration, choosing tools), checking AI output (citations, test coverage), and soft-systems framing (CATWOE, wicked problems). The `description` in `SKILL.md` could name those situations. The rerun to check it would have to use new items, so it isn't tuned to these.
- **The grader's notes flagged a few real errors in answers given with the skill.** For example, ai-001 got some sampling arithmetic wrong. A perfect rubric score doesn't mean a flawless answer.
