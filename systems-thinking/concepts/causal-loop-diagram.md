---
id: causal-loop-diagram
type: concept
title: Causal loop diagram (CLD)
aliases: [CLD, influence diagram]
summary: "A picture of feedback structure with four ingredients: nodes that are quantities, cause-to-effect arrows marked + or -, R/B loop labels, and double-hash delay marks."
chapters: [6, 10]
links:
  requires: [feedback-loop]
  contrasts-with: [stock-and-flow-diagram]
  related: [build-cld-from-story, trace-loop-polarity, delay]
---

The four ingredients:

1. **Nodes**: each names a *quantity* that can rise or fall ("success rate," "training time per person"), not an event or an action ("a project succeeds," "we train the hires"). Phrase every node so that "higher" means "more of that thing"; it keeps the signs from getting away from you.
2. **Arrows** from cause to effect, each marked with a **polarity**: `+` when cause and effect move in the same direction, `−` when opposite.
3. **Loop labels**: `R` or `B` inside a small circular arrow, placed in each closed loop only after tracing it.
4. **Delay marks**: two short hash marks across an arrow whose effect arrives late.

A CLD draws stocks, flows and calculated quantities the same way, which keeps it quick to sketch. It shows *what pushes what*, setting the plumbing aside; a stock-and-flow diagram shows what accumulates where. They describe the same system from two angles, and one can be translated into the other (Ch. 16).

A CLD is a model of influence, not of facts: its arrows claim *what changes what*. A knowledge graph's edges, by contrast, record *what is so*.
