# Review: Tragedy of the Commons

Card: [`systems-thinking/archetypes/tragedy-of-the-commons.md`](../systems-thinking/archetypes/tragedy-of-the-commons.md)  
Chapters: 13  
Attribution on the card: Garrett Hardin, "The Tragedy of the Commons," Science (1968); archetype in Peter Senge, The Fifth Discipline (1990); governance evidence from Elinor Ostrom, Governing the Commons (1990)

**Summary on the card:** Several independent actors share a finite, unpriced resource; each is individually incentivized to take more than a sustainable share because holding back only cedes it to others, so the resource degrades for everyone.

**Diagnostic question:** Are multiple independent actors individually incentivized to over-consume one shared, finite resource?

The book's figure: Figure 13.1.

## Machine check

**The card's own loop labels:** every labeled loop is a real cycle of the card's links, and its R/B label matches its minus-sign count.

### Against `volcano-lair-rush.cld`

**No differences:** every link, polarity, delay and loop matches under the proposed renaming.

**Independent of the proposed names (comparing only the variables both share):** 2 renamings make the two diagrams identical, links, polarities and delays alike; the proposed mapping is one of them.
 More than one usually means the diagram is symmetric (A and B swap).

- *Book only:* `Operation C lair gains`, `Operation C overbuilding`, with 4 links and 2 loops through them. Decide whether the card's generalization drops anything.

| Card link | Book link (in card names) | Result |
|---|---|---|
| A's consumption → A's gains (+) | A's consumption → A's gains (+) | match |
| A's gains → A's consumption (+) | A's gains → A's consumption (+) | match |
| B's consumption → B's gains (+) | B's consumption → B's gains (+) | match |
| B's gains → B's consumption (+) | B's gains → B's consumption (+) | match |
| A's consumption → shared resource (-) | A's consumption → shared resource (-) | match |
| B's consumption → shared resource (-) | B's consumption → shared resource (-) | match |
| shared resource → A's gains (+, delay (material)) | shared resource → A's gains (+, delay) | match |
| shared resource → B's gains (+, delay (material)) | shared resource → B's gains (+, delay) | match |

All feedback loops (every cycle, labeled or not):

| Loop | Card | Book |
|---|---|---|
| A's consumption → A's gains | R | R |
| B's consumption → B's gains | R | R |
| A's consumption → shared resource → A's gains | B | B |
| B's consumption → shared resource → B's gains | B | B |

## Proposed renaming (judge each)

| Card variable | Book: `volcano-lair-rush.cld` | Keeps the meaning? |
|---|---|---|
| A's consumption | Operation A overbuilding | ☐ |
| A's gains | Operation A lair gains | ☐ |
| B's consumption | Operation B overbuilding | ☐ |
| B's gains | Operation B lair gains | ☐ |
| shared resource | regional volcano-lair viability | ☐ |

## The card's own description (check it agrees with the structure)

> Each actor has its own reinforcing loop (consumption → gains → more consumption, no minus signs) and its own balancing loop through the commons (consumption → less resource `−` → fewer gains `+` → less consumption `+`; one minus). Every actor's brake runs through a stock all of them share, and acts late, so each feels the cost of its own consumption only after everyone else's has arrived too. Draw two actors or ten; the shape is the same.
> 
> The shared node is usually a stock (a fishery, an aquifer, a pool of willing workers, a CI cluster, a senior reviewer's time). No single period of overuse wrecks it, but every period adds damage, which is why collapse arrives late and seemingly all at once.

## Your verdict

- ☐ Structure matches the book
- ☐ Every rename keeps the meaning
- ☐ The card's description agrees with its structure
- Notes:
