# Review: Fixes That Fail

Card: [`systems-thinking/archetypes/fixes-that-fail.md`](../systems-thinking/archetypes/fixes-that-fail.md)  
Chapters: 11, 1, 20  
Attribution on the card: Peter Senge, The Fifth Discipline (1990)

**Summary on the card:** A quick fix relieves a symptom genuinely and immediately, but has a delayed side effect that makes the underlying problem worse, often triggering the same fix again, harder.

**Diagnostic question:** Does the problem keep coming back, worse, after each round of the same fix, as if the fix were feeding it?

The book's figure: Figure 11.1.

## Machine check

**The card's own loop labels:** every labeled loop is a real cycle of the card's links, and its R/B label matches its minus-sign count.

### Against `fixes-that-fail-overtime-pay.cld`

**No differences:** every link, polarity, delay and loop matches under the proposed renaming.

**Independent of the proposed names:** 1 renaming makes the two diagrams identical, links, polarities and delays alike; the proposed mapping is one of them.

| Card link | Book link (in card names) | Result |
|---|---|---|
| performance → quick fix (-) | performance → quick fix (-) | match |
| quick fix → immediate relief (+) | quick fix → immediate relief (+) | match |
| immediate relief → performance (+) | immediate relief → performance (+) | match |
| quick fix → side effect (+) | quick fix → side effect (+) | match |
| side effect → underlying damage (+, delay (material)) | side effect → underlying damage (+, delay) | match |
| underlying damage → performance (-) | underlying damage → performance (-) | match |

All feedback loops (every cycle, labeled or not):

| Loop | Card | Book |
|---|---|---|
| immediate relief → performance → quick fix | B | B |
| performance → quick fix → side effect → underlying damage | R | R |

## Proposed renaming (judge each)

| Card variable | Book: `fixes-that-fail-overtime-pay.cld` | Keeps the meaning? |
|---|---|---|
| performance | heist success rate | ☐ |
| quick fix | overtime pay | ☐ |
| immediate relief | effort | ☐ |
| side effect | henchman burnout | ☐ |
| underlying damage | long-run mistake rate | ☐ |

## The card's own description (check it agrees with the structure)

> A fast balancing loop closing the gap on a symptom, sitting on top of a slower reinforcing loop that the fix itself feeds. Trace B1: one minus, balancing. Trace R1: performance → fix (`−`), fix → side effect (`+`), side effect → damage (`+`, delayed), damage → performance (`−`): two minuses, reinforcing.

## Your verdict

- ☐ Structure matches the book
- ☐ Every rename keeps the meaning
- ☐ The card's description agrees with its structure
- Notes:
