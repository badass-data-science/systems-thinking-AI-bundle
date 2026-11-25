---
id: structural-and-behavioral-validity
type: concept
title: Structural and behavioral validity
summary: Structural validity asks whether each mechanism in a model corresponds to something real, checked link by link without looking at output; behavioral validity asks whether the output reproduces observed history; passing one never implies passing the other.
chapters: [18]
links:
  related: [validate-a-model, confirmation-bias, consistent-is-not-true]
series: [model-validation]
---

A model that runs without error has proved only that its equations compute.

**Structural validity**: can the people who work where a link lives point to that mechanism and defend it? Or did it go in because it made the output match what the modeler already suspected?

**Behavioral validity**: run forward from a known past starting state, does the model reproduce what was recorded?

Why check structure separately instead of trusting a good fit: fit is easy to manufacture. Every model has guessed parameters, and nudging them until the run matches history proves only that the model can be tuned. Wrong mechanisms that fit the past can go badly astray under conditions that haven't happened yet, which are the only conditions anyone builds a model to ask about. The tuning needn't be deliberate; it is confirmation bias acting on modeling choices.
