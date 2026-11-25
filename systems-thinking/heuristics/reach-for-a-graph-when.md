---
id: reach-for-a-graph-when
type: heuristic
title: Reach for a knowledge graph only when facts outgrow the diagram
summary: A well-drawn CLD or stock-and-flow diagram is the better tool for most systems thinking; a knowledge graph earns its cost when the facts are too many, change too often, must join external data, or must come back the same every time an agent answers.
chapters: [23, 17]
when: Someone proposes RDF, SPARQL or a graph database for a systems model.
then: List the factual questions the graph would answer that a diagram can't hold. If there aren't any, stay with the diagram. If there are, keep the graph beside the CLD and simulator, with polarity and delay encoded on edges.
links:
  related: [choose-model-by-question, software-is-escalation-of-commitment, knowledge-graph]
series: [knowledge-representation]
---

Reaching for graph tooling early is the same escalation-of-commitment trap as reaching for simulation software early. A diagram is more legible, faster to sketch, and easier to argue about in a room.
