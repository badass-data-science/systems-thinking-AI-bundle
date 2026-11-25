---
id: attention-management-loop
type: case
title: Managing regulatory attention on instinct
summary: An organization lowers its operating tempo when outside scrutiny feels too high; the loop balances, its goal is unwritten, and two delays make it oscillate.
chapters: [8, 9]
source_example: "The Interpol heat-management loop (Chapters 8 and 9, Figures 8.3 and 9.1)"
links:
  uses: [find-the-unwritten-goal, damp-an-oscillation, delay]
  instance-of: [balancing-loop, oscillation-and-overshoot]
  related: [attention-decay-and-tempo]
mnemonic: "The goal box nobody has ever filled in: '? ? ?', labeled 'the loop most organizations run.'"
structure:
  variables: [attention level, attention above acceptable level, tempo reduction, acceptable attention level]
  links:
    - {from: attention level, to: attention above acceptable level, polarity: "+", delay: information}
    - {from: attention above acceptable level, to: tempo reduction, polarity: "+"}
    - {from: tempo reduction, to: attention level, polarity: "-", delay: material}
    - {from: acceptable attention level, to: attention above acceptable level, polarity: "-", exogenous: true}
  loops:
    - {id: B1, type: B, label: lie low, path: [attention level, attention above acceptable level, tempo reduction]}
---

## Situation

Every operation adds to a regulator's attention, which decays slowly on its own. The organization "lies low" once attention *feels* too high, reducing operating tempo. Nobody designed this; it's what anyone paying loose attention to consequences does.

## Analysis

Trace: attention level → attention above acceptable level (`+`) → tempo reduction (`+`, read as how hard tempo is cut) → attention level (`−`). One minus, balancing. The goal feeds the gap from outside with a `−` (a higher acceptable level leaves less above it) and isn't counted.

Ask what number the goal holds: "nobody knows, we just feel it."

Two delays: information (the regulator's case-building takes weeks, and the organization feels attention only when an investigation goes public) and material (once tempo drops, accumulated attention decays on its own slow clock). Run forward: attention builds unseen past the threshold; an inspection registers it all at once; tempo is cut sharply; attention keeps falling for weeks while the organization, still hearing late, keeps tempo low too long; then the cycle restarts. The inspections land late in each climb, near the peak.

## Lesson

A balancing loop with an implicit goal and two delays oscillates even when every decision is reasonable. The fixes: name the goal, shorten the information delay (an earlier signal than public investigations), correct gently, or widen the acceptable band. Reacting harder to the next inspection makes it worse.
