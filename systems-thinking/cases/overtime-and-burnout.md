---
id: overtime-and-burnout
type: case
title: Overtime pay and burnout
summary: Overtime raised a slipping success rate for a quarter or two, while delayed burnout raised the mistake rate and pushed success down further, requiring more overtime.
chapters: [11]
source_example: "Overtime for henchmen when heist success rates slip (Chapter 11, Figure 11.1)"
links:
  instance-of: [fixes-that-fail]
  related: [emilys-laws-of-system-complexity]
structure:
  variables: [success rate, overtime, effort, burnout, mistakes]
  links:
    - {from: success rate, to: overtime, polarity: "-"}
    - {from: overtime, to: effort, polarity: "+"}
    - {from: effort, to: success rate, polarity: "+"}
    - {from: overtime, to: burnout, polarity: "+"}
    - {from: burnout, to: mistakes, polarity: "+", delay: material}
    - {from: mistakes, to: success rate, polarity: "-"}
  loops:
    - {id: B1, type: B, label: quick fix, path: [success rate, overtime, effort]}
    - {id: R1, type: R, label: burnout, path: [success rate, overtime, burnout, mistakes]}
---

## Situation

Project success rates were slipping. The response was overtime pay: more hours and more effort per project, and for a quarter or two, more successes.

## Analysis

B1 (one minus) is the fix doing its job. R1 (two minuses) runs underneath: overtime → burnout → (delayed) mistakes → lower success → more overtime. The fix's lever has a ceiling (hours in a shift); the reinforcing loop doesn't. The delay means several rounds of overtime pile up burnout before anyone sees it.

## Lesson

Overtime that covers one rough month while the organization finds out why projects are failing is a reasonable bridge. Overtime as the standing answer is the trap.
