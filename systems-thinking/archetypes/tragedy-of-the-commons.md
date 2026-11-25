---
id: tragedy-of-the-commons
type: archetype
title: Tragedy of the Commons
aliases: [commons dilemma, overgrazing]
summary: Several independent actors share a finite, unpriced resource; each is individually incentivized to take more than a sustainable share because holding back only cedes it to others, so the resource degrades for everyone.
chapters: [13]
attribution: Garrett Hardin, "The Tragedy of the Commons," Science (1968); archetype in Peter Senge, The Fifth Discipline (1990); governance evidence from Elinor Ostrom, Governing the Commons (1990)
diagnostic_question: Are multiple independent actors individually incentivized to over-consume one shared, finite resource?
links:
  requires: [reinforcing-loop, balancing-loop, stock, delay]
  related: [escalation, limits-to-growth, success-to-the-successful]
series: [competing-for-shared-resources, limits-and-capacity]
structure:
  variables: [A's consumption, A's gains, B's consumption, B's gains, shared resource]
  links:
    - {from: "A's consumption", to: "A's gains", polarity: "+"}
    - {from: "A's gains", to: "A's consumption", polarity: "+"}
    - {from: "B's consumption", to: "B's gains", polarity: "+"}
    - {from: "B's gains", to: "B's consumption", polarity: "+"}
    - {from: "A's consumption", to: shared resource, polarity: "-"}
    - {from: "B's consumption", to: shared resource, polarity: "-"}
    - {from: shared resource, to: "A's gains", polarity: "+", delay: material}
    - {from: shared resource, to: "B's gains", polarity: "+", delay: material}
  loops:
    - {id: R1, type: R, label: "A's growth", path: ["A's consumption", "A's gains"]}
    - {id: R2, type: R, label: "B's growth", path: ["B's consumption", "B's gains"]}
    - {id: B1, type: B, label: "A's commons limit", path: ["A's consumption", shared resource, "A's gains"]}
    - {id: B2, type: B, label: "B's commons limit", path: ["B's consumption", shared resource, "B's gains"]}
---

## Signature

Each actor has its own reinforcing loop (consumption → gains → more consumption, no minus signs) and its own balancing loop through the commons (consumption → less resource `−` → fewer gains `+` → less consumption `+`; one minus). Every actor's brake runs through a stock all of them share, and acts late, so each feels the cost of its own consumption only after everyone else's has arrived too. Draw two actors or ten; the shape is the same.

The shared node is usually a stock (a fishery, an aquifer, a pool of willing workers, a CI cluster, a senior reviewer's time). No single period of overuse wrecks it, but every period adds damage, which is why collapse arrives late and seemingly all at once.

## Symptoms

- A shared resource nobody owns is degrading, and every user can explain why the others are the problem.
- Users race to claim the resource before others do, then overbuild or over-consume.
- The heaviest users are hurt along with everyone else.

## Interventions

- No single actor can fix it; unilateral restraint only hands the share to others. The way out is collective: rules about the shared resource that every user agrees to, can see being kept, and can enforce.
- The enforcer can be a formal regulator or the users themselves; Ostrom showed communities often build working commons governance without an outside authority.
- Price or meter the resource, so each user's draw shows up in their own loop promptly instead of through the shared delayed stock.

## Misapplications

- Assuming the actors are shortsighted or greedy. The archetype requires neither: each can correctly foresee collective ruin and still rationally over-consume.
- Prescribing education or appeals to restraint as the fix.

## Distinguish from

- **Escalation**: actors respond to each other's relative position; here they respond to a shared resource. Both share the relative-incentive trap.
- **Limits to Growth**: one actor's growth meets its own constraint. A commons is a limit shared by several actors.
- **Success to the Successful**: the shared resource is *allocated* by a rule that reinforces the leader, rather than drawn down by everyone.
