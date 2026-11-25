---
id: translate-cld-to-stock-and-flow
type: procedure
title: Translate a CLD into stocks and flows
summary: "Six steps: snapshot-test every node, give each stock its pipes, turn every delay into a stock, make everything else an auxiliary, check every loop passes through a stock, then write and check each equation's units and polarity."
chapters: [16]
inputs: [A causal loop diagram with polarities and typed delays, The system's stock-and-flow skeleton if one exists]
outputs: [A stock-and-flow diagram with every flow and auxiliary named, An equation for each, Any nodes the CLD left implicit (goals, gaps, drains)]
links:
  uses: [snapshot-test, stock-and-flow-diagram, auxiliary, co-flow, delay]
  requires: [causal-loop-diagram]
  related: [hand-iterate-a-model, plus-into-a-stock]
series: [feedback]
---

## When to use

When a question changes from "what structure produces this?" to "how much, how fast, what if?". Dedicated simulation tools run the stock-and-flow model, never the CLD, so this translation always comes first.

## Steps

1. **Snapshot test** every node. What survives the photograph is a stock.
2. **Give every stock its pipes.** Whatever the CLD shows changing a stock directly becomes a flow into it (`+` link) or out of it (`−` link). A node that measures a stock's net change splits into that stock's inflows and outflows; often this forces a new drain the CLD never drew (for example, "defect scrap" draining a stockpile).
3. **Turn every delay mark into a stock.** A material delay is the material in the pipeline (possibly as a co-flow shadowing an existing stock); an information delay is a belief catching up.
4. **Everything else becomes an auxiliary**, recalculated each step. Constants (capacities, targets, yields) join them.
5. **Check every feedback loop passes through at least one stock.** A loop with none is an instantaneous circle no model can step through.
6. **Write an equation** for every flow and auxiliary, check its units, and check it reproduces each link's polarity. Expect to spell out comparisons the CLD left implicit: an arrow from a stock to "urgency" usually hides a goal and a gap (a schedule, and the shortfall against it).

## Checks

- Every loop has a stock on it.
- Units balance on every equation (tons per week into a stock of tons).
- Each CLD link's polarity is reproduced by the equations.
- A `+` into a stock now reads as "adds to."

## Common mistakes

- Treating every CLD node as a stock.
- Forgetting the drains a net-flow node implies.
- Leaving delays as fixed lags instead of stocks.
- Writing bare constants where a `min()` of competing constraints belongs.
