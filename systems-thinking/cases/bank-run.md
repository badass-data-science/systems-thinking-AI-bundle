---
id: bank-run
type: case
title: Bank run
summary: "Fear that a bank will fail drives withdrawals, which make failure likelier, which drives more fear: a vicious cycle with the same structure as a virtuous one."
chapters: [7]
source_example: "Chapter 7's real-world vicious cycle"
links:
  instance-of: [reinforcing-loop]
  related: [snowballing]
series: [reinforcing-dynamics]
structure:
  variables: [depositor fear, withdrawals, likelihood of failure]
  links:
    - {from: depositor fear, to: withdrawals, polarity: "+"}
    - {from: withdrawals, to: likelihood of failure, polarity: "+"}
    - {from: likelihood of failure, to: depositor fear, polarity: "+"}
  loops:
    - {id: R1, type: R, path: [depositor fear, withdrawals, likelihood of failure]}
---

## Situation

Depositors fear a bank may fail and withdraw their money.

## Analysis

The withdrawals themselves make failure likelier, which increases fear. All three links are `+`, so the loop is reinforcing. Run in the other direction, confidence begets deposits, which beget stability and more confidence.

## Lesson

Virtuous and vicious cycles are one structure. The question is never only "is this loop reinforcing?" but "which way is it running, and what could flip it?"
