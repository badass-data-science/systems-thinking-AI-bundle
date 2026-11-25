---
id: a-trace-is-not-a-definition
type: heuristic
title: A correct trace isn't a correct archetype
summary: A diagram can close and trace to the polarity claimed and still not be the archetype it's named after; tracing confirms polarity, and only the literature confirms the structure.
chapters: [24, 11, 15]
when: An archetype diagram passes the trace-and-count check.
then: Compare its loops against the archetype's canonical definition (how many loops, which kind, which links are side effects), not just against its own labels.
links:
  related: [trace-loop-polarity, systems-archetype, diagnose-an-archetype]
series: [model-validation]
---

Examples from the book's own drafting: Accidental Adversaries drawn without its partnership loop; Escalation drawn as one loop instead of two balancing loops joined into a reinforcing one; the Attractiveness Principle defined wrongly from the outline onward. All traced correctly.

This bundle's own validator has exactly this limit: it checks that each archetype's loops close and match their declared R/B labels, which can't tell whether the structure is the archetype named.
