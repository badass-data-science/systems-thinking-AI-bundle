---
id: trusted-forecasting-tool
type: case
title: A forecasting tool everyone trusts
summary: An AI forecasting tool with a good track record accumulates trust, its forecasts get less scrutiny, and fewer errors are caught, so trust keeps rising whether or not errors occur; its designers put the highest-stakes actions behind deterministic gates.
chapters: [20, 21]
source_example: "Omen, the forecasting toolkit from Agentic Time Series Forecasting for Supervillains (Chapter 20, Figure 20.1)"
links:
  instance-of: [ai-trust-loop]
  uses: [break-the-trust-loop, deterministic-gate-principle]
---

## Situation

A real, working AI-driven time series forecasting toolkit (Omen, the subject of the series' first volume) is trusted because it produces correct forecasts.

## Analysis

Two reinforcing loops share trust: usage ↔ trust, and trust → less scrutiny → fewer errors caught → more trust. Trust is a stock built over months; if forecasts started going wrong it would drain slowly while scrutiny stayed low. The tool's design answers this without drawing the loop: its highest-stakes action (redeploying a model) refuses to run without an explicit `confirmed=True`, so that decision never depends on how far anyone trusts the agent.

## Lesson

The point isn't that the tool is untrustworthy. Trust-and-scrutiny runs whether or not anyone draws it; break it by tying scrutiny to something other than trust, such as gates, fixed-rate checks and domain-based review.
