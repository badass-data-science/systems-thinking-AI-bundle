---
id: draw-a-boundary
type: procedure
title: Draw a system boundary on purpose
summary: Choose the smallest slice of the world that still contains the structure producing the behavior in question, sketch its stocks and flows, and write a defense for every exclusion.
chapters: [4]
inputs: [A recurring problem or question, A first list of the stages or parts involved]
outputs: [A stock-and-flow skeleton inside a dotted boundary, One defending sentence per excluded factor, A list of flows that leave the system]
links:
  uses: [system-boundary, stock, flow]
  related: [catwoe, boundary-critique]
---

## When to use

At the start of any model, diagram or root-cause analysis, before the first box is drawn in detail.

## Steps

1. State the question the model must answer (for example, "why does the deadline miss rate never improve?").
2. List what accumulates in the system as stocks and what fills and drains them as flows. Draw them as boxes joined by pipes with valves.
3. Draw a dotted line around the smallest set that still contains the structure producing the behavior. Choose by what the question requires, not by where data is easy to get.
4. For each factor the line leaves out, write one honest sentence defending why. If you can't write it without hedging, move the line.
5. Check inside each stage: are there flows leaving the system that nobody drew (material diverted, units scrapped, people reassigned)? Draw them, or the model will count stock that never arrives.
6. Run CATWOE against the result.

## Checks

- The boundary was chosen for the question, and you can say what question.
- Every exclusion has a defense, written down.
- Every stock has all its real inflows and outflows, including leaks.

## Common mistakes

- The convenience trap: drawing the boundary around available data.
- Treating "should X be inside?" debates as boundary redesign. Re-arguing the box and redrawing the box are different exercises.
- Forgetting outflows that leave through pipes nobody owns.
