---
id: swarm-test
type: heuristic
title: Swarm test
summary: Ask "is anyone in charge?"; if coordination is assigned by someone accountable, use the ordinary stock/flow and feedback toolkit; if it emerges from many actors following local rules with nobody in charge, treat it as a swarm.
chapters: [3, 21]
when: You're about to model a multi-actor system (a supply chain, a multi-agent AI pipeline, a market of automated traders) and need to choose a modeling approach.
then: "Ask whether coordination is assigned or emergent. Named owners, reporting lines and a designed hand-off mean the ordinary toolkit fits. Many independently built actors reacting to one another's outputs with no coordinator means a swarm: expect emergent behavior the ordinary toolkit may not capture."
links:
  uses: [complexity-science]
  related: [agentic-ai, actor-based-modeling]
---

Most systems that look swarm-like fail the test. A staged supply chain has a named owner per stage and a chain of command. A coding assistant has a person in charge of it. A designed multi-agent pipeline has its coordination assigned by whoever built it.

The test passes when many agents, built by different people for different ends, act on one another's outputs with nobody coordinating them: trading agents in one market, pricing agents on one storefront. That's where emergent behavior (flash crashes, price spirals) should be expected and where reasoning from a single drawn structure is weakest.
