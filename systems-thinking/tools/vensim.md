---
id: vensim
type: tool
title: Vensim
summary: Ventana Systems' commercial system dynamics authoring tool, with native stock-and-flow diagramming, numerical integration, and sensitivity and Monte Carlo tooling.
chapters: [17, D]
license: commercial (free Personal Learning Edition)
links:
  related: [stella-and-ithink, xmile, pysd, numerical-integration]
---

What it adds over a spreadsheet: diagrams that read like the book's, a choice of integration methods, built-in sensitivity and Monte Carlo runs (running the model thousands of times over sampled parameter combinations), and a visual language practitioners already share. It runs stock-and-flow models, never CLDs. Vensim's own release notes have described its XMILE reading as experimental; PySD reads its native `.mdl` files with `pysd.read_vensim`.
