---
id: undrawn-leak
type: case
title: Material leaking through a pipe nobody drew
summary: One department quietly diverts top-grade material from shipments to another use, so the model keeps counting it as in transit when it will never arrive.
chapters: [4, 15]
source_example: "Marketing pulling Grade-A villainium ore for gift-shop keychains (Chapter 4; revisited Chapter 15)"
links:
  uses: [draw-a-boundary, flow]
  related: [accidental-adversaries]
---

## Situation

A mine produces two grades of ore from the same holes. Only the top grade is usable downstream, so the boundary follows only that grade. Another department, which has never fully accepted that the grades are tracked separately, sometimes pulls top-grade ore out of shipments for its own product.

## Analysis

That is an outflow from the in-transit stock that no one drew. The model continues to count the diverted ore as in transit, so its projections of downstream supply are wrong in a way nothing inside the model can reveal.

## Lesson

A boundary drawn on purpose has to account for flows that leave the system from inside, not only for what sits outside it. Ask of every stock: is anything leaving it that isn't on the diagram?
