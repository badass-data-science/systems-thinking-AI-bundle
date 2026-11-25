---
id: agent-registry-graph
type: case
title: Finding the unreviewed agent
summary: A small graph of three agents (a forecaster, a coding agent and a pricing agent) shows by query that the pricing agent sets prices with nobody reviewing it while reading the forecaster's output.
chapters: [23]
source_example: "The Lab's operations graph of Omen, the coding agent and a pricing agent (Chapter 23)"
links:
  uses: [map-the-agents]
  related: [textbook-pricing-bots, trusted-forecasting-tool]
---

## Situation

An organization runs a forecasting agent (reviewed by its owner), a coding agent on control software (reviewed by a review team), and a newly added pricing agent that reads the forecast.

## Analysis

```turtle
:forecaster   a :Agent ; :actsOn :revenueForecast ; :reviewedBy :owner .
:codingAgent  a :Agent ; :actsOn :controlSoftware ; :reviewedBy :reviewTeam .
:pricingAgent a :Agent ; :actsOn :prices ; :readsOutputOf :forecaster .
```

The unreviewed-agent query returns one row: the pricing agent, setting prices. `?downstream :readsOutputOf+ :forecaster` shows that a forecasting error flows into prices with no human in between: the beginning of the pattern behind interacting pricing bots.

## Lesson

The graph says what to trace; whether an error would spiral, settle or swing is a question for a CLD and a simulation.
