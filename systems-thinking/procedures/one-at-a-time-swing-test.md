---
id: one-at-a-time-swing-test
type: procedure
title: One-at-a-time swing test
summary: Move each of the shakiest guessed parameters 25% up and 25% down while holding the others at their guesses, rerun, and see whether the recommendation flips; draw the results as a tornado chart.
chapters: [18]
inputs: [A runnable model (by hand or in software), A decision it supports, framed as a margin between options, A list of guessed parameters]
outputs: [A tornado chart, The parameters that flip the recommendation and where they flip, A measurement to-do list]
links:
  uses: [sensitivity-analysis]
  contrasts-with: [sobol-analysis]
  counters: [anchoring]
series: [uncertainty]
---

## When to use

On every model, before trusting any recommendation. No software needed.

## Steps

1. Frame the outcome as a margin between the options being compared, so a sign change means the recommendation flips.
2. Run the base case at the guesses and record the margin.
3. For each shaky parameter: set it to +25%, run; set it to −25%, run; return it to its guess. Hold everything else fixed.
4. Draw a tornado chart: one bar per parameter spanning its two results, with a line at the base margin and a dashed line at zero.
5. For any parameter whose bar crosses zero, search for the flip point (the value where the margin is zero) and note how far it is from the guess.
6. Note whether the parameter has ever been measured.

## Checks

- Exactly one parameter moves per run.
- Results are read against the decision, not against raw output.

## Common mistakes

- Concluding a parameter "doesn't matter" from a zero swing. In a switch-like model, a swing that keeps the outcome on one side of a threshold shows no change at all; the same parameter can matter a lot once another guess is off. One-at-a-time testing never lets two guesses be wrong together.
- Swinging only the parameters that are easy to change.

## Worked example

Decision: expand assembly capacity 10% (60 to 66 a week) versus stop corner-cutting on rushed material, under a six-week labor shortage, looking 26 weeks ahead. Margin ("expansion's lead") at the guesses: 60 tons. Refining yield (67.5%–100%) and transit time (1.5–2.5 weeks) don't move it. Quality lost to corner-cutting: −25% changes nothing; +25% flips the recommendation, and the flip is at 0.57, about 15% above the guessed 0.5. It has never been measured. That's the to-do list.
