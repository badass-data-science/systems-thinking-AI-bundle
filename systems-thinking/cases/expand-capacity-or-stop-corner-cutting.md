---
id: expand-capacity-or-stop-corner-cutting
type: case
title: Expand capacity, or stop cutting corners?
summary: The model recommends expanding assembly capacity over stopping corner-cutting by 60 tons, but the recommendation flips if an unmeasured quality-loss guess is 15% too low, or only 3% too low if transit is also faster than guessed.
chapters: [18]
source_example: "Chapter 18's sensitivity analysis of the Doomsday Device model (tornado chart and Sobol indices; chapter_18_sobol.py)"
links:
  uses: [one-at-a-time-swing-test, sobol-analysis, validate-a-model]
  related: [quantified-supply-chain-model, anchoring]
---

## Situation

Two candidate interventions on the quantified supply chain: expand assembly capacity 10% (labor hours are the bottleneck) or stop cutting corners on rushed material (the vicious loop). Test: a six-week shortage removing 10 tons a week from assembly, measured 26 weeks out. Outcome: expansion's lead, the tons by which expansion leaves the stockpile closer to schedule. At the guesses, 60 tons: expansion gets fully back on schedule; stopping corner-cutting leaves it 60 behind.

## Analysis

**Hand swing**: yield and transit time don't move the lead at all. Quality loss: −25% no change; +25% flips it; the flip point is 0.57, 15% above the guess of 0.5, and the parameter has never been measured.

**Why so lopsided**: the outcome is switch-like. Either extra capacity absorbs the shortage, the stockpile catches up and urgency dies away, or the shortage outlasts it, urgency stays high, more rushed material arrives damaged, and the vicious loop takes over, leaving the stockpile hundreds of tons behind. Expansion's best case is "fully back on schedule," so any swing that leaves the switch on the good side shows no change.

**Sobol** (quality loss and transit time, each ±25%, 6,144 runs): S1 = [0.55, 0.15], ST = [0.85, 0.44], S2 = 0.30. About one run in five flips the recommendation. Quality loss dominates. Transit time, harmless in the hand swing, matters in combination: if rushed material arrives 25% faster than guessed, quality loss needs to be only about 3% too high for the flip. Transit time's S1 of 0.15 comes from the runs where quality loss is high, which the hand swing (holding quality loss at 0.5) never visited.

## Lesson

Go measure quality loss from corner-cutting first, and transit time second, before committing to expansion. The two methods answer different questions; use the hand swing everywhere and Sobol when guesses may be wrong together.
