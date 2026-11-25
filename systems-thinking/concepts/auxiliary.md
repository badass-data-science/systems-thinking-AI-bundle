---
id: auxiliary
type: concept
title: Auxiliary variable
aliases: [converter, auxiliary]
summary: In a stock-and-flow model, a quantity that is neither a stock nor a flow; recalculated each time step from other quantities, it sets how far a flow's valve opens, and constants (capacities, targets, yields) are drawn the same way.
chapters: [16]
links:
  part-of: [stock-and-flow-diagram]
---

Examples: urgency computed from a stockpile shortfall, quality computed from the share of rushed material, a defect rate computed from quality. Auxiliaries have no memory; they're whatever their equation says this step. In a translated CLD most nodes become auxiliaries.
