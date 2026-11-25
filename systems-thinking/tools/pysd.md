---
id: pysd
type: tool
title: PySD
summary: An open-source Python library that loads a Vensim or XMILE model and simulates it as ordinary Python, returning a pandas DataFrame.
chapters: [17, 18, D]
license: free, open-source
links:
  related: [xmile, vensim, salib, verify-after-translation]
series: [knowledge-representation]
---

```python
import pysd
model = pysd.read_xmile("quantified-supply-chain.xmile")   # or pysd.read_vensim("model.mdl")
results = model.run()                                      # a pandas.DataFrame
print(results[["Refined Villainium On Hand", "Warhead Stockpile"]].head(9))
```

The output reproduces the hand-iterated table (row 0 is the starting state; rows 1 to 8 are the eight weeks), which is the point of running the check. Results as a DataFrame mean sensitivity sweeps, Monte Carlo, plotting, and AI agents querying the model are one import away.

**PySD translates structure, not judgment.** A structurally unsound model simulates as smoothly in Python as in its tool of origin. After any import, spot-check its output against the original tool's run on identical inputs. PySD also translates the model to Python on first load, creating a generated `.py` file and `__pycache__` that are safe to delete.

Runnable copy: `code/chapter_17_pysd.py`.
