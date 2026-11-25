---
id: specification-gaming
type: concept
title: Specification gaming
aliases: [reward hacking, Goodhart's law, proxy gaming]
summary: An AI system (or any optimizer) optimizing a measured proxy at the expense of the real goal it stood in for; once the neglected goal's damage reaches the metric, its structure is identical to Fixes That Fail.
chapters: [20, 3]
attribution: "Amodei et al., \"Concrete Problems in AI Safety\" (2016), as reward hacking; Stuart Russell, Human Compatible (2019)"
links:
  specializes: [fixes-that-fail]
  part-of: [ai-system-as-a-system]
series: [proxy-metric, ai-delegation, unintended-consequences]
structure:
  variables: [metric score, metric optimization, proxy shortcuts, real-goal neglect, real-goal failures]
  links:
    - {from: metric score, to: metric optimization, polarity: "-"}
    - {from: metric optimization, to: proxy shortcuts, polarity: "+"}
    - {from: proxy shortcuts, to: metric score, polarity: "+"}
    - {from: metric optimization, to: real-goal neglect, polarity: "+"}
    - {from: real-goal neglect, to: real-goal failures, polarity: "+", delay: material}
    - {from: real-goal failures, to: metric score, polarity: "-"}
  loops:
    - {id: B1, type: B, label: hit the metric, path: [metric score, metric optimization, proxy shortcuts]}
    - {id: R1, type: R, label: neglected goal, path: [metric score, metric optimization, real-goal neglect, real-goal failures]}
---

Often narrated as a novel AI-alignment phenomenon. Structurally: a quick, measurable win (hit the metric) with a delayed, unintended side effect (the real goal degrades, unmeasured at first, until the damage drags the metric down), which triggers the same optimization pressure again, harder. Node labels differ from Fixes That Fail; the loops, polarities and delay position are the same.

The AI-safety literature treats it as a practical, researchable failure mode (reward hacking, in Amodei et al.), and Russell argues it follows from building machines around a fixed objective that may have been stated wrong.

Recognizing it as a familiar pattern in new terminology is the move: the Fixes That Fail interventions apply (measure the real goal directly; shorten the delay on its degradation; treat proxy gains as a bridge, not the answer).
