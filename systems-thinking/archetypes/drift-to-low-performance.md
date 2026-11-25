---
id: drift-to-low-performance
type: archetype
title: Drift to Low Performance
aliases: [eroding goals, normalization of deviance, boiled frog]
summary: A goal quietly erodes toward whatever performance is being achieved, because lowering the target closes the gap faster than improving performance does.
chapters: [15, 8, 14]
attribution: Peter Senge, The Fifth Discipline (1990), as Eroding Goals; this name from Donella Meadows, Thinking in Systems (2008)
diagnostic_question: Has the goal itself quietly moved down to meet current results, rather than results being pushed up to meet the goal?
links:
  requires: [balancing-loop, reference-point, delay]
  related: [growth-and-underinvestment, find-the-unwritten-goal]
series: [balancing-dynamics, proxy-metric]
structure:
  variables: [gap below target, corrective action, actual performance, pressure to lower target, target]
  links:
    - {from: gap below target, to: corrective action, polarity: "+"}
    - {from: corrective action, to: actual performance, polarity: "+", delay: material}
    - {from: actual performance, to: gap below target, polarity: "-"}
    - {from: gap below target, to: pressure to lower target, polarity: "+"}
    - {from: pressure to lower target, to: target, polarity: "-"}
    - {from: target, to: gap below target, polarity: "+"}
  loops:
    - {id: B1, type: B, label: fix performance, path: [gap below target, corrective action, actual performance]}
    - {id: B2, type: B, label: lower the goal, path: [gap below target, pressure to lower target, target]}
---

## Signature

Two balancing loops close the same gap. B1, the fix, has to wait for a delay. B2, lowering the target, takes only a meeting, so it closes the gap first, and the target moves instead of performance. Each loop has one minus sign.

## Symptoms

- A target adjusted downward several times, each time in response to a miss rather than a deliberate reconsideration (e.g. an acceptable success rate falling from 90% to 70% over three years).
- Each adjustment looked like reasonable pragmatism ("let's be realistic given current conditions").
- No single decision anyone can point to; it never announces itself as a crisis.

## Interventions

- Anchor the goal to something outside the system's own recent results: what customers need, what a competitor achieves, what the organization achieved in a good year.
- Then a miss stays a gap to close, and any change to the goal must be argued on its merits as a decision rather than slipping through as an adjustment.
- Write the goal down; an unwritten goal can drift without anyone noticing.

## Misapplications

- Treating a single missed target as drift. One miss is just a miss.
- Treating every target revision as drift. A deliberate reconsideration of what the organization wants is legitimate.

## Distinguish from

- **Growth and Underinvestment**: contains an eroding standard as one of its loops, inside a capacity-investment structure.
- **Fixes That Fail**: the problem worsens through a side effect; here the standard moves.
