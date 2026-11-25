---
id: damp-an-oscillation
type: procedure
title: Damp an oscillation caused by delay
summary: When a balancing loop overshoots because its feedback is late, shorten the delay, correct only part of the gap at a time, or widen the acceptable band; never react harder to the same late signal.
chapters: [9]
inputs: [A balancing loop that swings past its goal repeatedly, Its delays, marked and typed]
outputs: [A chosen damping intervention, A prediction of what it does to the swings]
links:
  uses: [delay, oscillation-and-overshoot, balancing-loop]
series: [delay]
---

## When to use

Something overshoots and swings back: autoscaling that adds servers after the spike has passed, staffing that lurches between freezes and sprees, inventory that's always too much or too little.

## Steps

1. Draw the balancing loop: state, goal, gap, correction.
2. Mark every delay with hash marks and label its kind: information (finding out late) or material (the world changing slowly).
3. Sketch the state over time and check it oscillates around the goal.
4. Ask which delay could realistically be shortened (faster measurement, earlier signals, shorter pipelines). If one can, that's usually the best fix.
5. Otherwise, react more gently: correct part of the gap, then wait long enough to see what the last correction did before the next one.
6. Or widen the acceptable band around the goal, so a late signal doesn't demand as violent a correction.
7. Predict the effect on the swings before acting.

## Checks

- The intervention acts on the delay, the correction size, or the band, not on how urgently people react.
- Nobody is being blamed for acting late on information that hadn't arrived.

## Common mistakes

- Reacting faster and harder to the next signal. If the delay is structural, reacting harder to a signal that's just as late makes the overcorrection bigger.
- Treating oscillation as proof that the goal is wrong or the loop is broken.
- Blaming individuals for a structural delay.
