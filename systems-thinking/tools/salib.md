---
id: salib
type: tool
title: SALib
summary: An open-source Python library for global sensitivity analysis (Sobol indices, Morris screening), a natural next step once a model runs in Python through PySD.
chapters: [18, D]
license: free, open-source
links:
  related: [pysd, sobol-analysis, morris-screening]
series: [uncertainty]
---

Typical pattern: define the uncertain parameters and their ranges as a problem dict, generate samples (Saltelli sampling for Sobol), run the model once per sample through a wrapper function, then analyze. See `code/chapter_18_sobol.py` and the Sobol analysis card.
