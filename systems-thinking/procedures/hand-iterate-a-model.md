---
id: hand-iterate-a-model
type: procedure
title: Hand-iterate a stock-and-flow model
summary: Give each stock a starting value and each flow an honest-guess equation, step the model forward one time step at a time in a table, read off which constraint binds, then shock it to see whether its loops fire.
chapters: [16]
inputs: [A stock-and-flow diagram, Starting values and guessed parameters (honest guesses are fine)]
outputs: [A time-step table, The binding constraint, Findings the CLD alone couldn't show, A list of guessed parameters for sensitivity testing]
links:
  uses: [stock-and-flow-diagram]
  related: [sensitivity-analysis, quantified-supply-chain-model]
series: [model-validation]
---

## When to use

As soon as a model has been translated into stocks and flows, before reaching for software. Hand arithmetic is enough for a model with a handful of stocks.

## Steps

1. Write each stock's starting value with units.
2. Write each flow's equation, with its constraints as `min()` terms.
3. Choose a time step (one week, one day). For each step: compute every flow from the start-of-step stocks, then end level = start + inflows − outflows for every stock.
4. Iterate eight or so steps in a table.
5. Read the table: which `min()` term is binding each step? Which stocks pile up or drain? Does the trajectory match what the CLD predicted (rising, falling, oscillating)?
6. If a loop never fires in the base case, **shock the model** (cut a capacity for a few steps) and compare a run with the loop intact against one with it switched off.
7. List the guessed numbers the findings depend on; they go to sensitivity testing.

## Checks

- The table follows the update rule exactly on every row.
- If the model is later run in software, its output reproduces this table.

## Common mistakes

- Searching for the "correct" number before iterating. At this stage honest guesses are the point: writing an explicit equation forces disagreements a CLD lets stay vague, and those are cheap to resolve now.
- Concluding a loop is harmless because the base case is calm.
- Treating a disagreement between the table and the CLD as an error to hide. That gap is worth more than either answer.

## Worked example

Refined stock starts at 50 tons. Refining = min(90 arriving, 100 capacity) × 0.9 = 81/week. Assembly = min(on hand, 60 labor-hour cap) = 60/week. Week 1: 50 + 81 − 60 = 71; then 92, 113, ... 218 by week 8; finished stockpile 60, 120, ... 480. Findings: 21 tons a week pile up unused (the refinery out-produces assembly); output is capped by labor hours the whole time, never by ore or refining, so a bigger refinery optimizes the wrong constraint; and with deadlines at exactly 60/week, the schedule has no slack.
