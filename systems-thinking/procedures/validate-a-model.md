---
id: validate-a-model
type: procedure
title: Put a model on trial
summary: Before acting on a model, test its structure link by link, test its behavior against history separately, then find which guesses its advice depends on, while running a counter-practice for each of three named biases.
chapters: [18]
inputs: [A runnable model, Historical data for at least one past period, Access to people who work where each link lives]
outputs: [A structural verdict per link, A behavioral fit verdict, A ranked list of parameters to measure, A recorded disconfirming result written before the runs]
links:
  uses: [structural-and-behavioral-validity, one-at-a-time-swing-test, sobol-analysis, confirmation-bias, availability-heuristic, anchoring]
  related: [hand-iterate-a-model]
series: [model-validation, cognitive-bias]
---

## When to use

Before any model's recommendation is acted on, and again whenever the model changes.

## Steps

1. **Write down, before running anything, what result would prove the model (or your recommendation) wrong.**
2. **Structural trial.** For each link, ask someone who works where it lives (ideally someone who didn't build the model) to point to the mechanism and defend it. Record links that exist only because they improved the fit.
3. **Behavioral trial.** Run from a known past starting state and compare with the recorded history. Note which parameters you adjusted to get the fit.
4. Keep the verdicts separate. A good fit doesn't excuse an indefensible link, and a defensible structure that misses history needs investigation, not tuning.
5. **Sensitivity.** Run the one-at-a-time swing test on the shakiest guesses against the specific decision the model supports. If guesses might be wrong together, or the model is in Python, run a Sobol analysis (or Morris screening for slow models).
6. **Bias counter-practices**: for confirmation bias, steps 1 and 2; for availability, set each guess from the record, not from the most memorable incident; for anchoring, have someone estimate the key guesses independently before seeing yours, and swing the first-draft numbers.
7. Produce the to-do list: which parameter, if measured, would most change your confidence in the recommendation.

## Checks

- The disconfirming result was written before the runs.
- At least one structural reviewer didn't build the model.
- The sensitivity test was run against a decision, not against "robustness" in general.

## Common mistakes

- Treating a good historical fit as validation.
- Treating "it runs in PySD" as validation.
- Treating the biases as moral failings to resolve with willpower instead of naming them and running a concrete counter-practice.
