---
id: trace-three-orders
type: procedure
title: Trace a change three orders deep
summary: For a real change (often an AI-augmented workflow), write the first-order effect, what it causes months later, and what that might cause a year out (labeled speculative), check each against the archetypes, and pick remedies that keep the first-order gain.
chapters: [22]
inputs: [A change that has been or will be adopted, Knowledge of what sits downstream of it (people, reviews, systems)]
outputs: [Three ordered effects with time horizons and confidence, Any archetype each matches, Remedies that keep the gain]
links:
  uses: [second-order-effects, diagnose-an-archetype]
  related: [knowledge-graph, map-the-agents]
series: [unintended-consequences, ai-delegation]
---

## When to use

When adopting a change with a clear first-order benefit, especially one that speeds up part of a workflow, such as an AI coding agent or an AI-assisted analysis pipeline.

## Steps

1. **First order**: state the immediate, visible effect honestly, including the gain.
2. **Second order**: ask "and then what?" What does that effect do to the parts of the system downstream of it over the next few months? Name those parts concretely (which reviewers, which teams, which systems), looking them up if the system is large.
3. **Third order**: ask again, a year or more out, and label it as more speculative.
4. Stop when the chain is too thin to defend.
5. For each order, ask whether it matches an archetype (an Accidental Adversaries pair, a Shifting the Burden capability, a Fixes That Fail side effect). If so, take the archetype's remedy.
6. Choose remedies that keep the first-order gain rather than reversing the change.
7. Circle any consequence nobody on the team has said aloud.

## Checks

- The first-order gain is stated, not dismissed.
- Each later order names a mechanism and a horizon.
- The remedies don't give up the gain.

## Common mistakes

- Collapsing to an all-or-nothing verdict on the tool. A real gain and a real risk can both be true.
- Going five or six orders deep into speculation.
- Tracing consequences without first looking up what's actually downstream.
