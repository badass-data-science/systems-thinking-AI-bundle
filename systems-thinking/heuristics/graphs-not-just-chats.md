---
id: graphs-not-just-chats
type: heuristic
title: Graphs, not just chats
summary: When an AI agent answers factual questions about a system, give it a knowledge graph to query so its answers are reproducible, traceable to sources and shared, rather than left in one conversation.
chapters: [23, 20, 21]
when: An agent is being asked factual questions about a system (who reviews what, which suppliers run late, what sits downstream of a stage).
then: Put the facts, with their sources and whether each was measured, in a graph the agent queries. Treat the lookup as a clear-domain decision behind a deterministic gate.
links:
  uses: [knowledge-graph]
  counters: [ai-trust-loop]
  related: [deterministic-gate-principle, retrieval-augmented-generation]
series: [knowledge-representation, ai-delegation]
---

Without a source, an agent answers from its conversation and training: possibly fluent and wrong, visible to no one else, unrepeatable tomorrow, with no record of where each fact came from. With a graph: **reproducible** (same question, same graph, same rows), **traceable** (each fact carries its source), **shared** (every person and agent sees the same facts).

It answers the trust loop: scrutiny falls because checking costs effort; when an answer arrives with its facts and sources, checking costs a glance. A graph doesn't make the agent right. It makes its factual claims cheap to check.
