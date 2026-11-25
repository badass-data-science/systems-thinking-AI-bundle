---
id: choose-model-by-question
type: heuristic
title: Choose the model by the question
summary: "Three questions, three models: what structure is producing this? (a CLD); how will it behave over time? (a stock-and-flow simulation); what do we know and what is connected to what? (a knowledge graph)."
chapters: [23, 10, 17]
when: Deciding which kind of model, notation or tool to use, or whether a diagram has outgrown paper.
then: "Name the question first. Size, team, and who is asking (a person, a script, an AI agent) matter less. Use them side by side when the questions are mixed: a graph holding the model's structure and what's known about it, a simulator running its dynamics."
links:
  related: [causal-loop-diagram, stock-and-flow-diagram, knowledge-graph, kumu, loopy, pysd]
series: [knowledge-representation]
---

- *What feedback structure is producing this?* A CLD: on paper, or in Kumu or Loopy once it outgrows a page or needs a team.
- *How will it behave over time: how much, how fast, what if?* No CLD can answer this. Translate it into stocks and flows and run it by hand, in Vensim or Stella, or with PySD.
- *What do we know, and what is connected to what?* (Which suppliers take more than ten days; everything downstream of a stage; which links rest on an unmeasured guess.) A knowledge graph. It records facts and answers by lookup, not by tracing loops or running time forward.
