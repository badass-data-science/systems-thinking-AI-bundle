---
id: fluency-is-not-correctness
type: heuristic
title: Fluency is not system-level correctness
summary: A fast, confident, internally consistent answer to the question asked says nothing about whether the question was the right one, so check the question, not the polish.
chapters: [1, 20, 21]
when: An AI agent (or a fluent analyst) returns a well-formed diagnosis quickly, and the diagnosis is correct about the part it examined.
then: Ask whether anyone posed the structural question (has this shape of failure happened before, and what keeps producing it?). If not, pose it yourself; the agent will not widen its own question unprompted.
links:
  related: [systems-thinking, cynefin-as-delegation-guide, ai-trust-loop]
series: [ai-delegation]
mnemonic: "The AI's root-cause slide awarded itself a green '✓ Confidently Diagnosed' badge."
---

The properties people use to decide whether to trust an explanation (confidence, clean writing, internal consistency, a real finding) are properties of the answer's phrasing. None of them is evidence that the answer addresses the recurring structure. An agent answers the question it was given; the reframing step, noticing that a pattern of individually correct answers is what needs explaining, is a human judgment call that agents don't supply by default.

The danger scales with speed: an agent can dispatch the fifth, sixth and tenth proximate cause before anyone sees the pattern forming.
