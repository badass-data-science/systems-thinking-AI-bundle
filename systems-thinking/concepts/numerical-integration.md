---
id: numerical-integration
type: concept
title: Numerical integration method and time step
aliases: [Euler's method, Runge-Kutta, DT, time step]
summary: How simulation software steps a model through time; Euler and Runge-Kutta methods can give meaningfully different output on the same model, so the method and time step are modeling decisions, not defaults to ignore.
chapters: [17]
links:
  related: [stock-and-flow-diagram, vensim, xmile]
---

A hand-iterated table is Euler's method: assume each flow holds steady for the whole step, then update every stock at once. Runge-Kutta methods sample the flows several times within each step and blend the results, costing more arithmetic and staying closer to a continuously changing system.

Quick check that a result isn't an artifact of the step: halve the time step and rerun. If the conclusion changes, the step size was driving it. Differences in default method or step between tools are also why a model can give different numbers after an XMILE round trip.
