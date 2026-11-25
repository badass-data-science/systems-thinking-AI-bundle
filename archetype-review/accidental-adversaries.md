# Review: Accidental Adversaries

Card: [`systems-thinking/archetypes/accidental-adversaries.md`](../systems-thinking/archetypes/accidental-adversaries.md)  
Chapters: 15  
Attribution on the card: Credited to Jennifer Kemeny; first described in print in The Fifth Discipline Fieldbook (Senge et al., 1994)

**Summary on the card:** Two natural allies, each succeeding when the other does, each fix their own local gap in a way that obstructs the other, and those side effects close a vicious reinforcing loop that overpowers the partnership.

**Diagnostic question:** Are two natural allies each fixing their own problem in a way that quietly hurts the other?

The book's figure: Figure 15.3.

## Machine check

**The card's own loop labels:** every labeled loop is a real cycle of the card's links, and its R/B label matches its minus-sign count.

### Against `accidental-adversaries.cld`

**No differences:** every link, polarity, delay and loop matches under the proposed renaming.

**Independent of the proposed names (comparing only the variables both share):** 1 renaming makes the two diagrams identical, links, polarities and delays alike; the proposed mapping is one of them.

- *Contracted:* the book draws `extra inspection` → `held shipments` (+) → `mining success` (-); the card draws one link with the same net polarity (-). Decide whether dropping `held shipments` loses anything.

| Card link | Book link (in card names) | Result |
|---|---|---|
| A's success → A's contribution to B (+) | A's success → A's contribution to B (+) | match |
| A's contribution to B → B's success (+) | A's contribution to B → B's success (+) | match |
| B's success → B's contribution to A (+) | B's success → B's contribution to A (+) | match |
| B's contribution to A → A's success (+) | B's contribution to A → A's success (+) | match |
| A's success → A's local fix (-) | A's success → A's local fix (-) | match |
| A's local fix → A's success (+) | A's local fix → A's success (+) | match |
| B's success → B's local fix (-) | B's success → B's local fix (-) | match |
| B's local fix → B's success (+) | B's local fix → B's success (+) | match |
| A's local fix → A's contribution to B (-, delay (material)) | A's local fix → A's contribution to B (-, delay) | match |
| B's local fix → A's success (-) | B's local fix → A's success (-) | book draws two links via 'held shipments' |

All feedback loops (every cycle, labeled or not):

| Loop | Card | Book |
|---|---|---|
| A's local fix → A's success | B | B |
| B's local fix → B's success | B | B |
| A's contribution to B → B's success → B's contribution to A → A's success | R | R |
| A's contribution to B → B's success → B's local fix → A's success | R | R |
| A's contribution to B → B's success → B's contribution to A → A's success → A's local fix | R | R |
| A's contribution to B → B's success → B's local fix → A's success → A's local fix | R | R |

2 of these loops are not among the card's labeled loops. They follow from the links; the card isn't wrong to leave them unlabeled, but check none of them changes the story.

## Proposed renaming (judge each)

| Card variable | Book: `accidental-adversaries.cld` | Keeps the meaning? |
|---|---|---|
| A's success | mining success | ☐ |
| A's contribution to B | on-spec ore delivered | ☐ |
| B's success | assembly success | ☐ |
| B's contribution to A | steady orders for mining | ☐ |
| A's local fix | shipment rushing | ☐ |
| B's local fix | extra inspection | ☐ |

## The card's own description (check it agrees with the structure)

> An outer reinforcing partnership loop (each one's success feeds the other's; no minus signs). Each party's local fix is a small balancing loop that works for itself. Each fix's side effect lands on the other party. Those side effects close an inner loop: A's fix → less contribution to B (`−`) → less B success (`+`) → more B fixing (`−`) → less A success (`−`) → more A fixing (`−`). Four minus signs, reinforcing: a vicious loop inside the virtuous one. Once it dominates, neither party can see the whole from its own seat.

## Your verdict

- ☐ Structure matches the book
- ☐ Every rename keeps the meaning
- ☐ The card's description agrees with its structure
- Notes:
