---
id: shifting-the-burden-to-the-intervenor
type: archetype
title: Shifting the Burden to the Intervenor
aliases: [single point of expertise, key-person dependency]
summary: Shifting the Burden where the symptomatic fix is a specific outside fixer available on demand (a consultant, the one expert, an AI agent), so internal capability erodes faster than in the ordinary case.
chapters: [11, 20]
attribution: Peter Senge, The Fifth Discipline (1990)
diagnostic_question: Is one on-demand fixer (a person, a vendor, an AI agent) becoming the only thing in the organization that can do the job?
links:
  specializes: [shifting-the-burden]
  related: [ai-trust-loop]
series: [ai-delegation]
structure:
  variables: [problem, calls to intervenor, internal capability, internal fixing]
  links:
    - {from: problem, to: calls to intervenor, polarity: "+"}
    - {from: calls to intervenor, to: problem, polarity: "-"}
    - {from: problem, to: internal fixing, polarity: "+"}
    - {from: internal fixing, to: problem, polarity: "-", delay: material}
    - {from: calls to intervenor, to: internal capability, polarity: "-", delay: material}
    - {from: internal capability, to: internal fixing, polarity: "+"}
  loops:
    - {id: B1, type: B, label: call the intervenor, path: [problem, calls to intervenor]}
    - {id: B2, type: B, label: fix it ourselves, path: [problem, internal fixing]}
    - {id: R1, type: R, label: capability erosion, path: [problem, calls to intervenor, internal capability, internal fixing]}
---

## Signature

Same three loops as Shifting the Burden. The intervenor's on-demand availability gives every short-term incentive to keep calling them rather than train a second capable person, so the erosion loop runs fast.

## Symptoms

- Only one person (or one vendor, or one agent) can describe the problem properly, let alone fix it.
- That intervenor's absence (a vacation, an outage, a contract ending) is an operational risk that appears on no risk register.
- Internal staff route around the problem to the intervenor reflexively.

## Interventions

- Train a second capable person while the intervenor is still available, and have the intervenor teach rather than do.
- Put the dependency on the risk register by name.
- With an AI agent as the intervenor: keep humans exercising the capability, set review by the decision's domain rather than by the agent's record (see Cynefin as a delegation guide), and make the agent's work checkable (see Graphs, not just chats).

## Misapplications

- Treating any use of an expert or tool as this archetype. It requires internal capability actually eroding because of the reliance.

## Distinguish from

- **Shifting the Burden** in general: there the symptomatic fix can be an internal workaround; here it is a specific external fixer, and the erosion is faster.
- **The AI trust loop** (Ch. 20): rising trust reducing scrutiny is a related but separate reinforcing loop; the two often run together.
