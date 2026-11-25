---
id: success-to-the-successful
type: archetype
title: Success to the Successful
aliases: [rich get richer, cumulative advantage, competency trap]
summary: Two competitors draw from one limited resource, and an early edge for one, however it arose, is reinforced by the allocation rule itself, starving the other of what it would need to catch up regardless of merit.
chapters: [15, 19]
attribution: Peter Senge, The Fifth Discipline (1990)
diagnostic_question: Is an early, possibly arbitrary edge being reinforced by the resource-allocation rule itself, regardless of ongoing merit?
links:
  requires: [reinforcing-loop]
  related: [escalation, tragedy-of-the-commons, leverage-points]
series: [competing-for-shared-resources]
structure:
  variables: ["A's share of the resource", "A's resources", "A's performance", "B's resources", "B's performance"]
  links:
    - {from: "A's share of the resource", to: "A's resources", polarity: "+"}
    - {from: "A's resources", to: "A's performance", polarity: "+"}
    - {from: "A's performance", to: "A's share of the resource", polarity: "+"}
    - {from: "A's share of the resource", to: "B's resources", polarity: "-"}
    - {from: "B's resources", to: "B's performance", polarity: "+"}
    - {from: "B's performance", to: "A's share of the resource", polarity: "-"}
  loops:
    - {id: R1, type: R, label: "A's success", path: ["A's share of the resource", "A's resources", "A's performance"]}
    - {id: R2, type: R, label: "B's starvation", path: ["A's share of the resource", "B's resources", "B's performance"]}
---

## Signature

Two reinforcing loops sharing one allocation node. A's side: bigger share → more resources → better performance → bigger share (no minus signs). B's side: bigger share for A → fewer resources for B (`−`) → weaker B performance (`+`) → bigger share for A (`−`): two minus signs, reinforcing too. Performance lines diverge.

## Symptoms

- An early win (partly skill, partly luck) earned a bigger share, and the gap has widened every round since.
- The loser was not measurably less capable at the start.
- Past performance is used to justify the next allocation.
- Leaders explain the outcome as proof the winner was simply better all along.

## Interventions

The leverage is in the allocation rule, not in either competitor:

- Allocate by what each needs to reach a shared goal, or guarantee each a floor, so an early edge can't compound into the other's starvation.
- Break the coupling: give each its own budget, so one's win no longer comes out of the other's share.
- When using past performance to allocate, discount the part of it that the allocation rule itself produced.

## Misapplications

- Reading the outcome as evidence of merit. Under this structure, past performance is partly a record of the allocation rule's accumulated effect.
- Assuming any unequal outcome is this archetype; check that the resource is shared and the allocation rule feeds on performance.

## Distinguish from

- **Tragedy of the Commons**: everyone draws down the shared resource; here a rule allocates it.
- **Escalation**: competitors respond to each other; here the allocation rule does the reinforcing.
