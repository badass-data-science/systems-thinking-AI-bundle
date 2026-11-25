---
id: supply-chain-recurring-misses
type: case
title: The supply chain that kept missing deadlines
summary: Four quarters of real, correctly fixed root causes (labor shortage, supplier lead time, customs delay, scheduling conflict), and the deadline miss rate never improved.
chapters: [1, 4, 10, 16, 17, 18]
source_example: "The Doomsday Device Supply Chain (Chapter 1; the book's through-line example)"
links:
  uses: [recurring-causes-mean-structure, reduction, system]
  related: [fluency-is-not-correctness]
mnemonic: "Q4's root-cause report came from the AI agent, with a green '✓ Confidently Diagnosed' badge it had awarded itself."
---

## Situation

A four-stage supply chain (extract raw material, ship it to a refinery, refine it, assemble finished units against deadlines) misses its assembly deadlines quarter after quarter. Each quarter's postmortem finds a real cause and fixes it:

- Q1: labor shortage. A scheduling tool had flagged the coming shortfall two weeks early, but its alert sat in a queue nobody watched. Most of the workforce was gig labor booked through a marketplace, which left mid-shift when a competitor outbid the standing rate.
- Q2: supplier lead time shift, after an analyst switched to a cheaper supplier without checking who owned it (it traced back to a competitor).
- Q3: customs delay, solved by a broker who remembered a similar delay two years earlier.
- Q4: scheduling conflict in the refining queue, diagnosed overnight by an AI agent from eight weeks of logs, fast and correct.

Every fix worked. The miss rate held flat for three quarters, then rose.

## Analysis

The *elements* changed every quarter: a different supplier, staffing level, customs officer. The *interconnections* never changed. In particular, urgency at the assembly end fed back into corner-cutting at the refining end, stressing whichever link was weakest. Each postmortem was a reduction; each answered the narrow question asked. The AI agent did the same thing faster and with better formatting, bringing no different mode of inquiry.

Later chapters build this system out: a boundary and stock/flow sketch (Ch. 4), a causal loop diagram of the urgency-and-corner-cutting loop (Ch. 10), a quantified stock-and-flow model (Ch. 16), a PySD simulation (Ch. 17) and a Sobol sensitivity analysis (Ch. 18).

## Lesson

A pattern of individually correct answers is itself what needs explaining. Ask what the whole arrangement keeps producing, whichever part breaks.
