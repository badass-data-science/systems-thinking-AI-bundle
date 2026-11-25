---
id: fixes-that-fail
type: archetype
title: Fixes That Fail
aliases: [fixes that backfire]
summary: A quick fix relieves a symptom genuinely and immediately, but has a delayed side effect that makes the underlying problem worse, often triggering the same fix again, harder.
chapters: [11, 1, 20]
attribution: Peter Senge, The Fifth Discipline (1990)
diagnostic_question: Does the problem keep coming back, worse, after each round of the same fix, as if the fix were feeding it?
links:
  requires: [balancing-loop, reinforcing-loop, delay]
  contrasts-with: [shifting-the-burden]
  related: [emilys-laws-of-system-complexity, specification-gaming]
series: [unintended-consequences]
structure:
  variables: [performance, quick fix, immediate relief, side effect, underlying damage]
  links:
    - {from: performance, to: quick fix, polarity: "-"}
    - {from: quick fix, to: immediate relief, polarity: "+"}
    - {from: immediate relief, to: performance, polarity: "+"}
    - {from: quick fix, to: side effect, polarity: "+"}
    - {from: side effect, to: underlying damage, polarity: "+", delay: material}
    - {from: underlying damage, to: performance, polarity: "-"}
  loops:
    - {id: B1, type: B, label: quick fix, path: [performance, quick fix, immediate relief]}
    - {id: R1, type: R, label: unintended consequence, path: [performance, quick fix, side effect, underlying damage]}
---

## Signature

A fast balancing loop closing the gap on a symptom, sitting on top of a slower reinforcing loop that the fix itself feeds. Trace B1: one minus, balancing. Trace R1: performance → fix (`−`), fix → side effect (`+`), side effect → damage (`+`, delayed), damage → performance (`−`): two minuses, reinforcing.

## Symptoms

- The same fix is applied every period, each time with good short-term results.
- The fix's dose keeps increasing to get the same relief.
- The baseline problem gets slowly worse even as each application "works."
- People defend the fix with true statements ("it worked last time").

## Interventions

- The leverage is in the problem the fix keeps relieving, not in the fix. Use the quick fix only as a bridge that buys time to work on why performance slipped.
- Before reaching for any fix, ask what it will do a few rounds out, not just this period.
- Shorten or expose the delay on the side effect (measure burnout, debt or damage directly) so it shows up before several rounds have stacked up.

## Misapplications

- Calling any failed fix "Fixes That Fail." The archetype needs a *side effect of the fix itself* that feeds the problem; a fix that simply didn't work is something else.
- Assuming "greater" harm is guaranteed. With a short enough delay or a weak enough side effect, the fix just works. (This is the Second Law caveat.)

## Distinguish from

- **Shifting the Burden**: there the fix's side effect erodes the *ability to apply a better fix*; here it makes the *problem itself* worse.
- **Specification gaming**: the AI version. Once the neglected goal's damage reaches the measured proxy, it has this exact structure.

## Why it's dangerous

It works, immediately, every time it's tried, which is what makes it addictive. A fix that failed instantly would be abandoned. Two features make the backlash "greater" than the fix: the delay (several rounds of fix pile up before the side effect shows) and a mismatch of ceilings (the fix's lever is bounded, such as hours in a shift, while the reinforcing loop compounds without one). This archetype is the traceable mechanism behind the First Law of System Complexity.
