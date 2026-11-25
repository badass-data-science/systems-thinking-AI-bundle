---
id: calm-base-case-proves-nothing
type: heuristic
title: A calm base case doesn't prove a loop harmless
summary: If a loop never fires under baseline conditions, shock the model and compare runs with the loop intact and switched off before concluding it doesn't matter.
chapters: [16, 18]
when: A simulated feedback loop stays dormant in the base run.
then: Apply a realistic disturbance (a few steps of reduced capacity) and run it twice, loop on and loop off. The difference is the loop's real effect.
links:
  related: [hand-iterate-a-model, sensitivity-analysis]
series: [model-validation]
---

In the book's supply chain, eight calm weeks hid a loop that, after a three-week labor shortfall, turned a 30-ton gap (loop cut) into a 285-ton gap that was still growing (loop intact). A calm base case may only mean the schedule has no slack and nothing has disturbed it yet.
