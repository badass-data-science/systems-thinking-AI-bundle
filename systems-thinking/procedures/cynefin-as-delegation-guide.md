---
id: cynefin-as-delegation-guide
type: procedure
title: Use Cynefin to decide what to delegate to an AI agent
summary: "Classify a decision's Cynefin domain before any agent sees it, and let the domain, never the agent's fluency or track record, set the agent's job: a rule it calls, an analysis someone checks, probes it proposes, or a runbook it follows."
chapters: [21, 20]
inputs: [A specific decision, An AI agent that could help with it]
outputs: [The decision's domain, The agent's job and its limits, The scrutiny that applies (set by domain, not by track record)]
links:
  uses: [cynefin-framework, deterministic-gate-principle]
  counters: [ai-trust-loop]
  related: [break-the-trust-loop, fluency-is-not-correctness]
series: [decision-domain, ai-delegation]
---

## When to use

Before handing any part of a decision to an AI agent.

## Steps

1. **Classify the decision yourself** (or have the agent propose a classification that a person checks). Ask: are cause and effect obvious, discoverable with expertise, coherent only in retrospect, or not perceivable at all?
2. **Assign the agent's job by domain:**
   - **Clear**: write the procedure down as a rule, script or checklist; the agent *calls* it rather than improvising its own version.
   - **Complicated**: the agent analyzes toward a knowable answer; check it with an expert or against data the analysis never saw (a held-out test). Agents suit this domain best, because a knowable answer is checkable.
   - **Complex**: don't ask for the answer. Have the agent propose and track small, reversible probes; someone accountable chooses which probes to run and judges what they show.
   - **Chaotic**: stabilize first. The agent runs only steps written down in advance (a runbook from calmer times, which turns the first moves into clear-domain decisions); it doesn't draft new plans mid-crisis.
   - **Disorder**: classify first, and don't let the agent do the classifying unchecked.
3. **Set scrutiny by domain**, not by the agent's recent record. A run of good answers to complicated questions is evidence only about complicated questions.
4. If several independently built agents will interact with no coordinator (the swarm test passes), treat their joint behavior as complex: give each agent hard limits it can't reason its way past, and monitor what they do together.

## Checks

- The domain was set before the agent's answer was seen.
- In complex domains the agent's output is a set of probes, not a plan.
- In clear and chaotic domains the agent follows pre-written steps.

## Common mistakes

- Letting the agent's answer shape decide the domain. Agents reply in the shape of a complicated-domain answer (analysis then recommendation) almost regardless of the question, and nothing in the reply flags a complex problem.
- Accepting "here is the optimal strategy" for a complex question.
- Letting track record substitute for domain-based scrutiny (the trust loop).
