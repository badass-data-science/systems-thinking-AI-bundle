---
id: property-graph
type: concept
title: Property graph
aliases: [labeled property graph, Cypher]
summary: A graph data model where nodes and edges carry arbitrary key-value properties directly, rather than everything decomposed into triples; Neo4j's native model, queried in Cypher, not SPARQL.
chapters: [23]
links:
  contrasts-with: [knowledge-graph]
  related: [neo4j]
series: [knowledge-representation]
---

Not a lesser cousin of RDF. Attaching a delay duration directly to an edge is often a more natural fit for a system dynamics model's structure than RDF's triples. Ask "which one matches how this model wants to be described?" before "which is more rigorous?"
