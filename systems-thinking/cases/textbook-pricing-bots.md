---
id: textbook-pricing-bots
type: case
title: Two pricing bots and a $23.7 million textbook
summary: In 2011 two sellers' repricing rules (one at 0.998 times its rival, the other at about 1.27 times) multiplied a biology textbook's listed price by about 1.27 a day until it peaked at $23,698,655.93.
chapters: [21]
source_example: "Michael Eisen's April 2011 observation of 'The Making of a Fly' on Amazon (Chapter 21)"
links:
  instance-of: [escalation]
  uses: [swarm-test, bound-interacting-agents]
series: [escalation, ai-delegation]
---

## Situation

The biologist Michael Eisen noticed two sellers listing Peter Lawrence's *The Making of a Fly* at over a million dollars. Each seller's software repriced against the other about once a day: one at about 0.998 times its rival's price, the other at about 1.27 times the first's (probably because it didn't hold a copy and needed margin to buy one elsewhere).

## Analysis

Each rule was sensible alone. Together they multiplied the price by about 0.998 × 1.27 ≈ 1.27 a day: an escalation loop, each side setting its price against the other's, with the spiral running up rather than down. It peaked at $23,698,655.93. Nobody chose that number; it emerged. These were two fixed multipliers, far simpler than adaptive agents, whose joint behavior is harder still to predict.

## Lesson

Bound each agent with limits it can't reason past (a price ceiling would have stopped this at its first absurd step) and watch what the agents do together.
