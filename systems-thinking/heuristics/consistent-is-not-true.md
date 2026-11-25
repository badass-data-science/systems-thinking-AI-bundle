---
id: consistent-is-not-true
type: heuristic
title: A consistent diagram isn't a true one
summary: A causal diagram can pass every notation check and still tell a story nobody who works in the system believes, so say it aloud to them before building on it.
chapters: [10, 18, 25]
when: A CLD or model is internally consistent and looks right, especially on the first draft.
then: Read each loop aloud as a single sentence to the people who work in the part of the system each link describes. Treat a wince as a bad or missing link. Be more suspicious of a clean first draft, not less.
links:
  related: [build-cld-from-story, structural-and-behavioral-validity]
series: [model-validation]
---

Narrative truth only shows up in speech. Automated tools (loop detection in Kumu, for instance) can confirm a loop exists but not that its story survives a room of skeptics; that check stays a human job.
