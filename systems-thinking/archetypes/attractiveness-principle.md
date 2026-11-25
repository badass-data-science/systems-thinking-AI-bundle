---
id: attractiveness-principle
type: archetype
title: Attractiveness Principle
summary: Limits to Growth with several different limits at once, each biting at a different size; relieving one only lets growth run until the next binds, so the real decision is which limits to relieve and which kinds of unattractiveness to accept on purpose.
chapters: [14]
attribution: Named after Jay Forrester's argument in Urban Dynamics (1969) that growth is ultimately controlled by controlling attractiveness; treated in archetype collections as a variation of Limits to Growth
diagnostic_question: Is growth running into several different limits at once, more than can be relieved, so that fixing one just hands growth to the next?
links:
  specializes: [limits-to-growth]
  related: [classify-a-growth-stall]
series: [limits-and-capacity]
structure:
  variables: [size, performance, attractiveness, new arrivals, support per member, crowding, outside scrutiny]
  links:
    - {from: size, to: performance, polarity: "+"}
    - {from: performance, to: attractiveness, polarity: "+"}
    - {from: attractiveness, to: new arrivals, polarity: "+"}
    - {from: new arrivals, to: size, polarity: "+"}
    - {from: size, to: support per member, polarity: "-"}
    - {from: support per member, to: performance, polarity: "+"}
    - {from: size, to: crowding, polarity: "+"}
    - {from: crowding, to: attractiveness, polarity: "-"}
    - {from: performance, to: outside scrutiny, polarity: "+", delay: material}
    - {from: outside scrutiny, to: attractiveness, polarity: "-"}
  loops:
    - {id: R1, type: R, label: growth, path: [size, performance, attractiveness, new arrivals]}
    - {id: B1, type: B, label: support dilution, path: [size, support per member, performance, attractiveness, new arrivals]}
    - {id: B2, type: B, label: crowding, path: [size, crowding, attractiveness, new arrivals]}
    - {id: B3, type: B, label: scrutiny, path: [performance, outside scrutiny, attractiveness, new arrivals, size]}
---

## Signature

One reinforcing growth loop and several balancing loops, each with one minus sign, each a different *kind* of limit that starts to bite at a different size, some after a delay. In the book's example: training staff spread thin (support per member), full bunks (crowding), and accumulating attention from outside authorities (scrutiny). Each responds to a different fix, and some (scrutiny) can't be bought off at all.

## Symptoms

- Relieving a bottleneck restores growth only briefly before a different one appears.
- The limits differ in kind: money, time to build, things no budget can touch.
- The budget can address one limit this period, not all.

## Interventions

- Decide explicitly which limits to relieve, in what order, and which kinds of unattractiveness to accept on purpose (crowded quarters rather than undertrained staff, because one costs comfort and the other costs results).
- Recognize that choosing nothing is still a choice: it hands the decision to whichever limit binds first.
- Expect growth to come to rest where the system is no more attractive than its alternatives (Forrester's result for cities).

## Misapplications

- Treating each new bottleneck as a fresh, unrelated problem.
- Trying to relieve every limit, which can't be done.

## Distinguish from

The diagnostic is a count. One limit, outside the system's own capacity: **Limits to Growth** (often removable, and removing it is the leverage). One limit that is the system's own capacity, which the organization keeps declining to expand: **Growth and Underinvestment**. Several limits at once, some removable and some not, more than the budget covers: **Attractiveness Principle**.
