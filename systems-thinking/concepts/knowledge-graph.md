---
id: knowledge-graph
type: concept
title: Knowledge graph, RDF and SPARQL
aliases: [RDF, SPARQL, triple store, Turtle]
summary: A knowledge graph represents entities as nodes and typed relationships as labeled edges, a model of facts rather than dynamics; RDF is the W3C standard for writing it as subject-predicate-object triples, and SPARQL is its query language.
chapters: [23, 10]
attribution: RDF and SPARQL are World Wide Web Consortium (W3C) standards
links:
  contrasts-with: [causal-loop-diagram]
  related: [property-graph, graphs-not-just-chats, choose-model-by-question, retrieval-augmented-generation]
series: [knowledge-representation]
---

A CLD's arrow claims that one quantity pushes another; a knowledge graph's edge records a fact ("the mine supplies the refinery"; "its ore takes fourteen days") and claims nothing about change. It can store a causal claim, but only as a fact to look up; nothing in the graph traces what the claim does downstream.

```turtle
@prefix : <http://example.org/supply-chain#> .
:mine     :suppliesTo            :refinery .
:mine     :shippingDelayDays     14 .
:refinery :increasesDefectRateOf :assemblyLine .
```

```sparql
PREFIX : <http://example.org/supply-chain#>
SELECT ?supplier ?customer ?days WHERE {
  ?supplier :suppliesTo ?customer ; :shippingDelayDays ?days .
  FILTER (?days > 10)
}
```

That query ("which suppliers take more than ten days, and to whom?") returns one row: mine, refinery, 14. No CLD can answer it (nowhere to keep a delivery time) and no simulation needs to (nothing runs forward). It's a lookup, which stays quick as a graph grows, and works the same whether a person, a script or an agent sends it. Property paths such as `:readsOutputOf+` follow a link any number of steps.

A triple has nowhere to hang a fact on a link (the fourteen days really belong to the mine-to-refinery link); RDF needs a separate node or a reified statement, where a property graph puts a property on the edge.

**Limitation**: a graph does not natively represent loop polarity or behavior over time. A naive graph-only model loses the feedback structure unless polarity and delay are deliberately encoded as edge properties.

**Literacy is the goal**: enough to read a query and know what question it asks. Runnable examples: `code/chapter_23_graphs.py`.
