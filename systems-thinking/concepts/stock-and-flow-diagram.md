---
id: stock-and-flow-diagram
type: concept
title: Stock-and-flow diagram and flow equations
aliases: [stock/flow diagram, SFD, flow equation, difference equation]
summary: The quantified version of a system sketch or translated CLD, with units and a starting value on every stock and an equation on every flow, stepped forward as a first-order difference equation.
chapters: [16, 4]
links:
  requires: [stock, flow]
  related: [translate-cld-to-stock-and-flow, hand-iterate-a-model, auxiliary, co-flow, source-and-sink]
series: [feedback]
---

A CLD shows what pushes what. A stock-and-flow diagram keeps that structure and adds which quantities accumulate and which are rates, plus the arithmetic rule on every flow. That's the difference between asking "up or down?" and asking "by how much, and when?"

**Stock update rule**, one time step at a time: end level = start level + inflows − outflows. With a flow equation on every flow, the whole model is a first-order difference equation, each step computed from the last. No calculus, just arithmetic applied consistently.

**Flow equations should carry their constraints.** Write `refining_rate = min(ore_available, refinery_capacity) × yield`, not a bare number. A bare number ("assembly rate = 60") discards the capacity dynamics the model exists to capture and hides which constraint is binding in any given step.

**Delays carry numbers.** A material delay is a stock whose size and residence time set its outflow: 180 tons in transit, each spending two weeks there, delivers 180 ÷ 2 = 90 tons a week.

**A stock remembers; a flow doesn't.** That memory is where a loop's momentum comes from, and why a stock can rise while its inflow falls.
