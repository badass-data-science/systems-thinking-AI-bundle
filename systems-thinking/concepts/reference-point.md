---
id: reference-point
type: concept
title: Reference point (goal)
aliases: [goal, setpoint, target, threshold]
summary: The value a balancing loop steers toward; it comes from outside the loop and can be explicit or implicit, fixed or moving.
chapters: [8, 15, 19]
links:
  part-of: [balancing-loop]
  related: [drift-to-low-performance, leverage-points, find-the-unwritten-goal]
---

Varieties:

- **Explicit and fixed**: a written budget ceiling, a safety limit.
- **Inherited**: last year's number, carried forward because nobody questioned it.
- **Relative**: set by comparison with someone else. In Escalation each side defends its position relative to the other's.
- **Moving**: when the goal slides toward whatever the system is already delivering, that is Drift to Low Performance.
- **Implicit**: a threshold nobody has stated that the system visibly, reliably defends ("we lie low once it *feels* too hot").

Change the reference point and the loop steers the system somewhere new, as faithfully as before. That's why goals sit near the top of the leverage hierarchy, far above parameters.

On a CLD the goal's arrow into the gap comes from outside the loop and is not counted when tracing the loop's polarity. Its sign tells you which way a new goal pushes the gap, not which kind of loop it is.

An implicit goal isn't automatically a problem. It becomes one when it stops matching what the organization wants, because an unwritten goal can't be argued with, revised, or even noticed.
