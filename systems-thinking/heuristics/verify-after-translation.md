---
id: verify-after-translation
type: heuristic
title: Verify after every translation
summary: After moving a model between tools, formats or languages (an XMILE round trip, a PySD import, a port to code), reproduce a known run on identical inputs before trusting it.
chapters: [17]
when: A model has been exported, imported, ported or re-implemented.
then: Run it on the inputs of a run you already trust (a hand table, the original tool's output) and compare. Check the time step and integration method if the numbers differ.
links:
  related: [pysd, xmile, numerical-integration]
series: [model-validation]
---

Interchange equivalence isn't numerical equivalence, and a successful import isn't validation. The book's PySD run reproduces the hand-worked table row for row, which is why it's shown.
