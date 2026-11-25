---
id: shifting-the-burden
type: archetype
title: Shifting the Burden
summary: A fast symptomatic fix and a slower fundamental fix compete to close the same gap, and reliance on the symptomatic fix erodes the capability to apply the fundamental one, so the quick fix keeps winning.
chapters: [11, 20]
attribution: Peter Senge, The Fifth Discipline (1990)
diagnostic_question: Is a symptomatic fix crowding out a fundamental one, and is the capability to apply the fundamental fix quietly atrophying?
links:
  requires: [balancing-loop, reinforcing-loop, delay]
  related: [fixes-that-fail]
series: [unintended-consequences, ai-delegation]
structure:
  variables: [problem symptom, symptomatic fix, fundamental fix, fundamental capability]
  links:
    - {from: problem symptom, to: symptomatic fix, polarity: "+"}
    - {from: symptomatic fix, to: problem symptom, polarity: "-"}
    - {from: problem symptom, to: fundamental fix, polarity: "+"}
    - {from: fundamental fix, to: problem symptom, polarity: "-", delay: material}
    - {from: symptomatic fix, to: fundamental capability, polarity: "-", delay: material}
    - {from: fundamental capability, to: fundamental fix, polarity: "+"}
  loops:
    - {id: B1, type: B, label: symptomatic fix, path: [problem symptom, symptomatic fix]}
    - {id: B2, type: B, label: fundamental fix, path: [problem symptom, fundamental fix]}
    - {id: R1, type: R, label: capability erosion, path: [problem symptom, symptomatic fix, fundamental capability, fundamental fix]}
---

## Signature

Two balancing loops close the same gap: B1, fast and always available; B2, slower (delayed) and able to resolve the root cause. A reinforcing loop connects them: more symptomatic fixing → less fundamental capability (delayed, through disuse) → less fundamental fixing → more symptom → more symptomatic fixing. Trace R1: `+`, `−`, `+`, `−`: two minuses, reinforcing.

The reinforcing capability-erosion loop is part of Senge's original diagram and the piece quick summaries most often drop. It's the engine: it explains *why* the fundamental fix keeps losing the comparison.

## Symptoms

- Every complaint is closed by the same fast workaround, for months or years.
- The proper fix is always "next quarter."
- Few people still know how to do the fundamental fix, and the number is shrinking.
- Each time the fundamental fix is considered, it looks harder than it did last time.

## Interventions

- Rebuild the fundamental capability before it's gone. Keep the symptomatic fix (the symptom is real) but treat it as a stopgap and spend the time it buys exercising the fading capability.
- Start now: the longer the quick fix runs alone, the more expensive the fundamental one gets, so the cheapest moment is always the present.
- Make the capability visible: who still has it, and for how much longer?

## Misapplications

- Calling any quick fix "shifting the burden." It needs a fundamental alternative *and* an erosion of the capability to apply it.
- Abolishing the symptomatic fix outright. The symptom still needs relief while the capability is rebuilt.

## Distinguish from

- **Fixes That Fail**: the side effect worsens the problem itself, with no competing fundamental fix.
- **Shifting the Burden to the Intervenor**: a variant where the symptomatic fix is a specific outside fixer (a consultant, a single expert, an AI agent), which runs faster and harder.
