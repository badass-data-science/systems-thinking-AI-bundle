---
id: sobol-analysis
type: concept
title: Sobol analysis (S1, ST, S2)
aliases: [Sobol indices, variance-based sensitivity analysis, global sensitivity analysis]
summary: A global sensitivity analysis that varies every uncertain parameter at once across its range, runs the model on thousands of combinations, and divides the variance of the result among the parameters, alone (S1), in total (ST) and in pairs (S2).
chapters: [18]
links:
  part-of: [sensitivity-analysis]
  contrasts-with: [one-at-a-time-swing-test]
  related: [morris-screening, salib]
series: [uncertainty]
---

Variance is the average squared distance of each run's result from the overall average.

- **S1, first-order index**: the share of the variance a parameter causes on its own, averaged over all values of the others. Practically, the share of the spread you'd expect to disappear if you measured this parameter exactly.
- **ST, total-order index**: the share the parameter has any part in, alone or in combination. Practically, the share that would remain if you measured every *other* parameter exactly.
- **S2, second-order index**: the share produced by a pair acting together beyond what either does alone.
- **ST − S1** is the parameter's influence that appears only in combination.

With two parameters the bookkeeping closes: S1 + S1 + S2 ≈ 1, and each ST ≈ its S1 + S2. Indices are sample estimates (about ±0.1 at a base sample of 1,024).

**Cost**: Saltelli sampling for two parameters with a base sample of N=1,024 with second-order indices gives N × (2D + 2) = 6,144 model runs, versus six for a two-parameter hand swing. Run counts grow with every parameter. For slow models, use Morris screening.

**What it sees that a hand swing can't**: two guesses being wrong together. A parameter that does nothing at the other's guessed value can decide the outcome once the other is off. A hand swing asks what happens near the guesses; Sobol asks what happens across the whole range of what you don't know. Neither is wrong.

```python
from SALib.sample import sobol as sobol_sample
from SALib.analyze import sobol as sobol_analyze
import numpy as np

problem = {
    "num_vars": 2,
    "names": ["quality_loss_from_corner_cutting", "transit_time"],
    "bounds": [[0.375, 0.625], [1.5, 2.5]],  # each guess, plus or minus 25%
}
param_values = sobol_sample.sample(problem, 1024, seed=42)
Y = np.array([run_doomsday_model(quality_loss_from_corner_cutting=p[0], transit_time=p[1])
              for p in param_values])
Si = sobol_analyze.analyze(problem, Y, seed=42)
```

Full script with the model wrapper: `code/chapter_18_sobol.py`.
