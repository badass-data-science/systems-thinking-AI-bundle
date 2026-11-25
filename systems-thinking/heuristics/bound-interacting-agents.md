---
id: bound-interacting-agents
type: heuristic
title: Bound interacting agents and watch them together
summary: When independently built agents react to one another's outputs with nobody coordinating, give each hard limits it can't reason past and monitor their joint behavior, because what they do together belongs to none of them.
chapters: [21, 3, 12]
when: Several automated agents (pricing bots, trading agents, independently built AI agents) respond to each other.
then: Add hard bounds (ceilings, floors, rate limits) to each agent, and monitor the combined behavior, not just each agent's behavior alone.
links:
  uses: [swarm-test]
  related: [escalation, cynefin-framework]
series: [ai-delegation, escalation]
---

Studying each agent, however carefully, won't reveal what they'll do together; their joint behavior is in the complex domain. Each agent's rule can be sensible alone while the combination escalates (see the textbook-pricing case).
