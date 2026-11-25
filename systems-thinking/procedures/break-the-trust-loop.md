---
id: break-the-trust-loop
type: procedure
title: Audit and break an AI trust-and-scrutiny loop
summary: Draw the AI-assisted workflow with an explicit "scrutiny per output" node, trace whether rising trust lowers it, find where you'd notice scrutiny falling to zero, then tie scrutiny to something other than trust.
chapters: [20, 21, 23]
inputs: [An AI-assisted workflow (a coding agent, an analysis tool, a forecasting tool), Who checks its output today and how often]
outputs: [A CLD of the workflow with its trust and scrutiny loops traced, The place a zero-scrutiny state would become visible (or the admission there is none), One or more scrutiny rules that don't depend on track record]
links:
  uses: [ai-trust-loop, trace-loop-polarity]
  counters: [shifting-the-burden-to-the-intervenor]
  related: [cynefin-as-delegation-guide, graphs-not-just-chats, deterministic-gate-principle]
series: [ai-delegation]
---

## When to use

For any workflow where an AI agent's output is checked by a person sometimes, and that "sometimes" has never been written down.

## Steps

1. Draw the workflow as a CLD with nodes for usage volume, trust level, scrutiny per output, and errors caught.
2. Trace: does rising trust reduce scrutiny? Do fewer caught errors leave trust free to rise? Count minus signs; confirm whether the loop reinforces.
3. Mark trust as a stock: how long would it take to drain if outputs started going wrong?
4. Ask the hard question: where, specifically, would you *notice* if scrutiny had fallen to zero? If nowhere, record that.
5. List the capabilities people no longer exercise because the agent does the work (the intervenor check).
6. Choose scrutiny rules that don't follow trust:
   - checks at a fixed rate, whatever the track record;
   - deterministic gates on the decisions that matter most (an action refuses to run without explicit confirmation);
   - scrutiny set by the decision's Cynefin domain, not the agent's record;
   - facts the agent's answers can be cheaply checked against (a knowledge graph with sources);
   - regular exercises where people do the work without the agent and compare their answer with the agent's, not the other way round.
7. Treat any confidence signal the agent produces about itself as data, not evidence.

## Checks

- At least one scrutiny rule is independent of the agent's track record.
- There's a named place where falling scrutiny would show up.

## Common mistakes

- Concluding "the agent is untrustworthy." The point is that trust-and-scrutiny is a loop that runs whether or not anyone draws it.
- Watching only usage dashboards; the scrutiny loop's output is an absence.
- Comparing the agent to human answers only when the agent seems wrong (that's still trust-driven scrutiny).
