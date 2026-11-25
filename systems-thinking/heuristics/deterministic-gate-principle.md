---
id: deterministic-gate-principle
type: heuristic
title: Deterministic-gate principle
summary: If a decision should produce the identical answer every time given identical inputs, it belongs behind a rule-based gate, not in open-ended judgment by a person or an agent.
chapters: [21, 20, 23]
when: Designing where an AI agent (or a person) may decide freely and where a rule must decide.
then: "Ask: should the same facts always give the same answer? If yes, encode it as a gate the agent must pass (a rule, a check, an explicit confirmation flag) rather than leaving it to reasoning. Reserve judgment for decisions that benefit from context and nuance."
links:
  related: [cynefin-as-delegation-guide, break-the-trust-loop, graphs-not-just-chats]
series: [ai-delegation, decision-domain]
---

Reproducibility given the same inputs is the dividing line. The series' first volume builds its forecasting toolkit this way: a redeploy refuses to run without an explicit `confirmed=True`, so the highest-stakes decision never depends on how confident the agent sounds that day. Gates also break the trust-and-scrutiny loop, because a gate's scrutiny doesn't fall as trust rises.
