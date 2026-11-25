---
id: accidental-adversaries
type: archetype
title: Accidental Adversaries
summary: Two natural allies, each succeeding when the other does, each fix their own local gap in a way that obstructs the other, and those side effects close a vicious reinforcing loop that overpowers the partnership.
chapters: [15]
attribution: Credited to Jennifer Kemeny; first described in print in The Fifth Discipline Fieldbook (Senge et al., 1994)
diagnostic_question: Are two natural allies each fixing their own problem in a way that quietly hurts the other?
links:
  requires: [reinforcing-loop, balancing-loop]
  related: [fixes-that-fail, escalation]
series: [unintended-consequences, stakeholder-worldviews]
structure:
  variables: [A's success, "A's contribution to B", B's success, "B's contribution to A", "A's local fix", "B's local fix"]
  links:
    - {from: "A's success", to: "A's contribution to B", polarity: "+"}
    - {from: "A's contribution to B", to: "B's success", polarity: "+"}
    - {from: "B's success", to: "B's contribution to A", polarity: "+"}
    - {from: "B's contribution to A", to: "A's success", polarity: "+"}
    - {from: "A's success", to: "A's local fix", polarity: "-"}
    - {from: "A's local fix", to: "A's success", polarity: "+"}
    - {from: "B's success", to: "B's local fix", polarity: "-"}
    - {from: "B's local fix", to: "B's success", polarity: "+"}
    - {from: "A's local fix", to: "A's contribution to B", polarity: "-", delay: material}
    - {from: "B's local fix", to: "A's success", polarity: "-"}
  loops:
    - {id: R1, type: R, label: partnership, path: ["A's success", "A's contribution to B", "B's success", "B's contribution to A"]}
    - {id: B1, type: B, label: "A's local fix", path: ["A's success", "A's local fix"]}
    - {id: B2, type: B, label: "B's local fix", path: ["B's success", "B's local fix"]}
    - {id: R2, type: R, label: adversarial, path: ["A's local fix", "A's contribution to B", "B's success", "B's local fix", "A's success"]}
---

## Signature

An outer reinforcing partnership loop (each one's success feeds the other's; no minus signs). Each party's local fix is a small balancing loop that works for itself. Each fix's side effect lands on the other party. Those side effects close an inner loop: A's fix → less contribution to B (`−`) → less B success (`+`) → more B fixing (`−`) → less A success (`−`) → more A fixing (`−`). Four minus signs, reinforcing: a vicious loop inside the virtuous one. Once it dominates, neither party can see the whole from its own seat.

## Symptoms

The diagnostic tell, remarkably consistent: both sides describe the *other* as "the problem," while each can accurately narrate its own behavior as a reasonable response to something the other did first. Both accounts are true; neither, told alone, explains the loop. Trying harder at one's own job makes it worse.

## Interventions

- The way out runs through the outer partnership loop, not either local fix.
- Get both parties looking at the whole structure together.
- Choose fixes that don't buy one side's numbers with the other's: a speed metric that counts only on-spec deliveries; an inspection that rejects a batch without holding up the next one.

## Misapplications

- Including every nearby problem. The archetype holds two parties, each harming the other through its own fix. A third party causing damage while not fixing anything of its own or reacting to either is outside the archetype, even if it lowers the same numbers. Draw an archetype's boundary as deliberately as a model's.
- Assigning blame to one side.

## Distinguish from

- **Escalation**: the parties are rivals responding to relative position; here they're allies whose interests align.
- **Fixes That Fail**: one party's fix harms itself later; here each fix harms the *other* party.
