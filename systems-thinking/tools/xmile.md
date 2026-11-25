---
id: xmile
type: tool
title: XMILE
summary: The OASIS-standardized, vendor-neutral XML format for exchanging system dynamics models between tools; it guarantees the structure travels, not that the model is correct.
chapters: [17, D]
license: open standard (OASIS)
links:
  related: [vensim, stella-and-ithink, pysd]
series: [knowledge-representation]
---

Good for portability and archival stability: build once, open in the tool each analyst prefers. It does not validate the model, document its assumptions, or replace boundary work.

A round trip between tools can change numbers through different default time steps or integration methods. Format equivalence isn't numerical equivalence; verify on any model that matters. Support varies: Stella opens XMILE directly; Vensim's support has been described as experimental.
