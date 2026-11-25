---
id: sensitivity-analysis
type: concept
title: Sensitivity analysis
summary: The discipline of finding out which of a model's guessed parameters its conclusions depend on, whose real payoff is a prioritized list of what to measure before trusting a specific recommendation.
chapters: [18]
links:
  related: [one-at-a-time-swing-test, sobol-analysis, morris-screening, validate-a-model]
series: [uncertainty]
---

It asks a practical question that the validity trials don't: which of the model's guesses does its advice depend on? The informal version (swing one parameter at a time by hand) is cheap and belongs in every model. Formal global methods (Sobol, Morris) vary every parameter at once and catch interactions.

Test against a decision, not against the model in general. Define the outcome that matters as a margin between options (for example, how many units further ahead option A leaves you than option B), so "the recommendation flips" has a precise meaning: the margin crosses zero.

Rarely is the payoff the reassurance that "the model is robust." It's usually a to-do list: go measure *this* parameter first.
