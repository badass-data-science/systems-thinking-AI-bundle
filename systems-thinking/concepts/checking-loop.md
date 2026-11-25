---
id: checking-loop
type: concept
title: The checking loop and its sensor
aliases: [verification loop, every check sees only what it was built to see]
summary: Checking work is a balancing loop whose sensor is the check itself, so it comes to rest when the check finds nothing, whether or not the work is right; errors outside the check's boundary or kind accumulate undrained.
chapters: [24]
links:
  specializes: [balancing-loop]
  related: [audit-your-checks, every-check-has-a-boundary-and-a-kind, system-boundary]
series: [model-validation, ai-delegation]
structure:
  variables: [errors the check can find, fixes]
  links:
    - {from: errors the check can find, to: fixes, polarity: "+"}
    - {from: fixes, to: errors the check can find, polarity: "-"}
  loops:
    - {id: B1, type: B, label: check and fix, path: [errors the check can find, fixes]}
---

A *check* is any step taken to find out whether work is right rather than to add to it (a script, a search, a reread, a review). A check is a model of "everything that could be wrong," so like any model it has a **boundary** (what it looks at) and a **kind** (what it is able to notice).

The loop reads not the errors in the work but the errors the check can find. When that count reaches zero, someone declares the work done. Anything the check can't see never enters the loop; it sits in a stock nothing drains.

Two aggravations:

- **Delay**: news that a check missed something can arrive weeks after "done" (an information delay).
- **Speed without a better sensor**: an AI agent runs the loop far faster than a person, and its "done" sounds just as sure whether the check was wide or narrow (fluency).

The mental model holding the loop in place: "a clean pass means it's right." It needs to become: "a clean pass means nothing this check can see is wrong."
