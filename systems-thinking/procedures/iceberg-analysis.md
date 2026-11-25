---
id: iceberg-analysis
type: procedure
title: Run the iceberg on an incident
summary: Write one honest sentence for each of the iceberg's four bands (event, pattern, structure, mental model) before accepting any fix.
chapters: [5]
inputs: [A specific incident or failure, Records of similar past incidents (not memory alone)]
outputs: [Four sentences, one per band, A candidate structure to draw as a causal loop diagram, The belief that keeps the structure in place]
links:
  uses: [iceberg-model]
  related: [recurring-causes-mean-structure, build-cld-from-story]
---

## When to use

After any incident where the obvious explanation arrives fast. Especially under time pressure, which is when analysis naturally stops at the event.

## Steps

1. **Event.** State what happened, once, plainly: who, what, when. No interpretation.
2. **Pattern.** Look across a window long enough to contain several occurrences (months, quarters). Has this kind of event happened before? How often, and is there a regular timing, such as "always about ten weeks after a major release"? Use records, not recollection.
3. **Structure.** Ask: what in the way this system is arranged makes this the *kind* of thing that happens here? Name the stocks that accumulate (attention, backlog, debt), how fast they drain, and what decision rule fails to check them. Phrase it so it can become a causal loop diagram.
4. **Mental model.** Ask what belief made that structure seem reasonable. Write it as the sentence people would say ("we've always run at this pace and mostly gotten away with it").
5. Decide which band your fix acts on. A fix that acts only on the event will not change the pattern.

## Checks

- The pattern sentence cites more than one event.
- The structure sentence names a mechanism (an accumulation, a delay, a missing check), not a person or a single cause.
- The mental-model sentence is something a reasonable person would have believed, not an accusation.

## Common mistakes

- Stopping at the event because the event already has a satisfying cause.
- Writing the structure band as "human error" or "bad luck," which are event-level explanations.
- Treating the mental model as a moral failing, which makes people defend it rather than update it.

## Worked example

A regulator inspects one of an organization's units. Event: an inspection last Tuesday. Pattern: the fourth in eighteen months, each about ten weeks after a major operation. Structure: every operation adds to a stock of regulatory attention that decays slowly (months), while operations happen weeks apart and the tempo is never set by checking current attention against a threshold. Mental model: "we've always run at this pace and mostly gotten away with it," which was true until attention began accumulating faster than it decayed.
