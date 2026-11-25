---
name: systems-thinking
description: "Systems thinking methods from the book Systems Thinking for Supervillains (by Lady Napalm): procedures, archetypes with checked loops, heuristics and worked cases. Load it for any question about why a system, team, market, model or AI setup behaves as it does, even when the answer seems obvious, because its checks change the answer. Use when: following up an incident or postmortem; a problem recurs or worsens despite fixes; a metric improves while the real goal declines; growth stalls, compounds or is credited to one cause; a level (headcount, backlog, inventory, trust) keeps rising or falling; something overshoots or oscillates; scoping a problem, or groups disagree on what it is (CATWOE, wicked problems, Cynefin); building, calibrating or validating a simulation, sensitivity analysis, or guessed parameters; choosing where to intervene; trusting, checking, delegating to or coordinating AI agents, including their citations, code and passing tests; tracing second-order effects; presenting a model to skeptics."
---

# Systems thinking

This skill packages the methods taught in *Systems Thinking for Supervillains: Feedback, Causality, and Mental Models for the Age of Agentic AI*. The book teaches with villainous examples; this bundle keeps the methods and restates the examples in neutral terms. Each card lists the chapters it comes from.

**The core habit:** when a whole keeps failing while its parts keep getting fixed, ask what *structure* is producing the behavior, draw it, and trace it before trusting any answer that skipped the sketch.

## How to use this bundle

1. Find the user's situation in the routing table below and open the cards it names. Every card is a small Markdown file with YAML frontmatter; `INDEX.md` lists all of them with one-line summaries.
2. Follow **procedure** cards step by step. Their `## Checks` and `## Common mistakes` sections are part of the method, not optional reading.
3. Before naming an **archetype**, trace the actual links. Each archetype card has a machine-checked `structure` block (variables, signed links, loops) to compare against.
4. Use **heuristic** cards as triggers: each has a `when` (the observable situation) and a `then` (what to do).
5. Use **case** cards as worked examples. Most are drawn from the book; a few are real-world cases it cites.
6. For relationships between cards, follow each card's `links`, or query `graph.json` or `graph.ttl` (RDF; see "Querying the graph").

## Routing

| The user's situation | Start with |
|---|---|
| Following up an incident under pressure ("a plan by tonight"); writing a postmortem | `heuristics/pressure-shrinks-the-iceberg.md`, `procedures/iceberg-analysis.md` |
| A problem keeps coming back; every postmortem finds a different, real cause | `heuristics/recurring-causes-mean-structure.md`, `procedures/iceberg-analysis.md` |
| Starting a model or analysis; deciding what's in scope | `procedures/draw-a-boundary.md`, `procedures/catwoe.md`, `heuristics/convenience-boundary-trap.md` |
| Groups disagree about what the problem even is; each blames another | `concepts/hard-and-soft-systems-thinking.md`, `concepts/soft-systems-methodology.md` (rich picture), `procedures/catwoe.md`, `concepts/tame-messy-wicked-problems.md`. Agree on the problem before building any model. |
| Turning a story or complaint into a diagram | `procedures/build-cld-from-story.md`, `procedures/trace-loop-polarity.md` |
| "Is this loop reinforcing or balancing?" | `procedures/trace-loop-polarity.md` |
| A change effort meets diffuse resistance; something keeps returning to a level nobody chose | `procedures/find-the-unwritten-goal.md` |
| Something overshoots and swings back (staffing, inventory, autoscaling) | `procedures/damp-an-oscillation.md`, `concepts/delay.md` |
| "Which archetype is this?" | `procedures/diagnose-an-archetype.md`, then the archetype card |
| Growth has stalled | `procedures/classify-a-growth-stall.md` |
| A fix works now but the problem keeps getting worse | `archetypes/fixes-that-fail.md`, `heuristics/ask-what-the-fix-does-later.md` |
| A quick workaround is crowding out the real fix; a key person, vendor or AI agent has become indispensable | `archetypes/shifting-the-burden.md`, `archetypes/shifting-the-burden-to-the-intervenor.md` |
| Two parties keep matching and raising each other | `archetypes/escalation.md`, `heuristics/change-the-comparison.md` |
| A shared resource nobody owns is degrading | `archetypes/tragedy-of-the-commons.md`, `heuristics/commons-need-collective-rules.md` |
| The winner keeps winning; resources follow past results | `archetypes/success-to-the-successful.md` |
| Targets keep getting lowered | `archetypes/drift-to-low-performance.md` |
| Two teams that should cooperate each blame the other | `archetypes/accidental-adversaries.md` |
| "How much, how fast, what if?" Quantifying a diagram | `procedures/translate-cld-to-stock-and-flow.md`, `procedures/hand-iterate-a-model.md` |
| Choosing a diagram, a simulation or a knowledge graph | `heuristics/choose-model-by-question.md` |
| Choosing modeling software or moving to Python | `procedures/choose-simulation-tooling.md`, `tools/pysd.md` |
| Before acting on a model's recommendation | `procedures/validate-a-model.md`, `procedures/one-at-a-time-swing-test.md`, `concepts/sobol-analysis.md` |
| Choosing where and how to intervene | `procedures/rank-interventions.md`, `concepts/leverage-points.md` |
| How much to trust or check an AI tool's output | `procedures/break-the-trust-loop.md`, `concepts/ai-trust-loop.md` |
| What to delegate to an AI agent for a given decision | `procedures/cynefin-as-delegation-guide.md`, `heuristics/deterministic-gate-principle.md` |
| Several AI agents interact with no coordinator | `heuristics/bound-interacting-agents.md`, `heuristics/swarm-test.md` |
| Adopting a change with a clear immediate benefit (often AI-assisted work) | `procedures/trace-three-orders.md` |
| An AI agent answers factual questions about a system | `heuristics/graphs-not-just-chats.md`, `procedures/map-the-agents.md` |
| Declaring work done; something slipped past review or tests | `procedures/audit-your-checks.md`, `heuristics/every-check-has-a-boundary-and-a-kind.md` |
| Presenting a model to the people it implicates | `procedures/live-build-technique.md`, `concepts/boundary-critique.md` |

## Ground rules

- **Trace, don't guess.** A loop's type comes from counting minus signs (even is reinforcing, odd is balancing), never from how it feels. Phrase every node as a quantity where "higher" means "more of that thing."
- **A familiar story is a hint, not a diagnosis.** Confirm an archetype against the traced links. And a correct trace still isn't a correct archetype: compare with the archetype's full structure.
- **Consistent isn't true.** Read every loop aloud to the people who work where its links live.
- **Name the flow.** A changing level is a claim about its inflows and outflows.
- **Delays change behavior,** not just speed. Don't react harder to a late signal.
- **Polarity carries no value.** Reinforcing isn't good; balancing isn't bad.
- **Fluency is not correctness,** including your own. Set scrutiny by the decision's domain and stakes, not by how confident an answer sounds. Mark guesses as guesses and say which parameter a recommendation depends on.
- **Don't announce the archetype first** when talking to people inside the system. Ask its diagnostic question and let them recognize it.

## Scope

The book, and so this skill, does not cover actor-based (agent-based) modeling, chaos mathematics, complexity science's formal toolkit, continuous-time system dynamics mathematics (it stays at difference equations; see Sterman's *Business Dynamics*), or Soft Systems Methodology beyond CATWOE and the rich picture. Say so when a problem needs them.

## Code

`code/` holds the book's runnable examples: `quantified-supply-chain.xmile` (the book's stock-and-flow model), `chapter_17_pysd.py` (load and run it with PySD), `chapter_18_sobol.py` (Sobol sensitivity analysis with SALib, about a minute to run), and `chapter_23_graphs.py` (RDF and SPARQL with rdflib). Install with `pip install pysd SALib rdflib`. Variable names in the model keep the book's costume ("Refined Villainium On Hand").

## Querying the graph

`graph.json` has `nodes` (id, type, title, summary, chapters, path) and `edges` (source, relation, target). `graph.ttl` is the same graph as RDF, under the prefixes `st:` (cards), `series:` (concepts shared across the book series) and `rel:` (relations and card types). For example, all procedures and heuristics that diagnose an archetype:

```sparql
PREFIX rel: <https://badass-data-science.github.io/supervillains/rel/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?tool ?archetype WHERE {
  ?p rel:diagnoses ?a . ?a a rel:Archetype .
  ?p rdfs:label ?tool . ?a rdfs:label ?archetype .
}
```

## Provenance

Built from the book's chapter files as of commit `9225c37` (2026-11-09). `evals/` holds 115 scenario-based checks (55 original, 60 held-out) of whether an AI is using these methods; they are new scenarios, not the book's examples.
