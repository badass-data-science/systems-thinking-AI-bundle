---
id: ai-trust-loop
type: concept
title: The trust-and-scrutiny loop
aliases: [automation complacency, trust loop]
summary: Two reinforcing loops share an AI tool's accumulated trust; usage builds trust and trust drives usage, while rising trust lowers scrutiny per output, fewer errors are caught, and trust rises further, with the second loop's output an invisible absence.
chapters: [20, 1, 21, 23]
links:
  part-of: [ai-system-as-a-system]
  related: [shifting-the-burden-to-the-intervenor, break-the-trust-loop, fluency-is-not-correctness]
series: [ai-delegation, reinforcing-dynamics]
structure:
  variables: [usage volume, trust level, scrutiny per output, errors caught]
  links:
    - {from: usage volume, to: trust level, polarity: "+"}
    - {from: trust level, to: usage volume, polarity: "+"}
    - {from: trust level, to: scrutiny per output, polarity: "-"}
    - {from: scrutiny per output, to: errors caught, polarity: "+"}
    - {from: errors caught, to: trust level, polarity: "-"}
  loops:
    - {id: R1, type: R, label: usage builds trust, path: [usage volume, trust level]}
    - {id: R2, type: R, label: trust lowers scrutiny, path: [trust level, scrutiny per output, errors caught]}
---

R1: no minus signs. R2: trust → scrutiny (`−`) → errors caught (`+`) → trust (`−`): two minus signs, reinforcing. Every step is reasonable: a track record is evidence, and checking a trusted tool feels like a poor use of time. But fewer caught errors happens whether or not errors are occurring, and nothing about falling scrutiny produces visible evidence of a problem. Usage shows on every dashboard; R2's output is an absence.

**Trust is a stock**, so trust built over months of good outputs doesn't vanish the week outputs start going wrong. It drains slowly, and scrutiny stays low the whole time.

**A self-generated confidence signal** (an agent's report awarding itself a "confidently diagnosed" badge) is this loop in one graphic: confidence produced by the system being trusted, consumed by an audience with no independent way to check it, discouraging the scrutiny that would catch the gap between "answered this question correctly" and "asked the right question."

**Where to break it**: the loop runs because scrutiny follows trust, so tie scrutiny to something else. See the break-the-trust-loop procedure.
