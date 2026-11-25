---
id: map-the-agents
type: procedure
title: Map the agents in a system as a graph
summary: Record each AI agent as triples (what it acts on, whose output it reads, who reviews it), then query for agents nobody reviews and for everything downstream of a given agent, as the list of what to trace before any CLD or simulation.
chapters: [23, 20, 21, 22]
inputs: [A system containing more than a few AI agents, Their configurations, owners and review arrangements]
outputs: [A graph of agents, targets, inputs and reviewers, The unreviewed agents, The downstream path of each agent's errors]
links:
  uses: [knowledge-graph]
  related: [trace-three-orders, bound-interacting-agents, break-the-trust-loop]
series: [ai-delegation, knowledge-representation]
---

## When to use

Once a system has more agents than anyone can hold in their head, or agents read one another's outputs.

## Steps

1. For each agent, write triples: `:agentX a :Agent ; :actsOn :target ; :readsOutputOf :agentY ; :reviewedBy :person .` Record the source of each fact.
2. Query for agents that act on something with no reviewer:
   ```sparql
   SELECT ?agent ?target WHERE {
     ?agent a :Agent ; :actsOn ?target .
     FILTER NOT EXISTS { ?agent :reviewedBy ?anyone }
   }
   ```
3. For each agent, list what its errors would flow into: `?downstream :readsOutputOf+ :agentY`.
4. Flag any path where one agent acts on another's output with no human in between. That is where interacting-agent escalation begins.
5. Hand those paths to a CLD or simulation to ask what an error would *do*. The graph supplies the map; it doesn't trace dynamics.
6. If agents drafted any of the triples, check the ones a decision will rest on.

## Checks

- Every agent has an owner and a review status recorded, even if the status is "none."
- Downstream paths were computed by query, not recalled.

## Common mistakes

- Expecting the graph to say whether an error would spiral or settle.
- Trusting agent-extracted triples unchecked: agents can invent a plausible fact or miss a link that spans two documents they read separately.
