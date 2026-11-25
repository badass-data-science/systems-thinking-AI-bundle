---
id: convenience-boundary-trap
type: heuristic
title: Suspect a boundary that matches your data
summary: If a model's boundary sits exactly where the easy data ends, it was probably drawn for convenience rather than for the question.
chapters: [4, 3]
when: The factors inside a model are the ones with good data, and the factors outside are the ones that are hard to measure.
then: Ask whether an excluded factor is part of why the system behaves as it does. If it is, bring it inside, even roughly estimated, or state plainly that the model can't explain behavior that depends on it.
links:
  related: [system-boundary, draw-a-boundary]
series: [boundary]
---

Nobody draws the narrow boundary out of malice; they draw it because one dataset was hard to get and another wasn't. The cost arrives later, when something outside the line moves and the "fully modeled" system falls over for reasons the model can't express. Global supply chains during the pandemic showed the same trap at scale.

The heuristic doesn't say "include everything." A boundary should be the smallest slice that still contains the structure producing the behavior. It says that data availability is not a reason.
