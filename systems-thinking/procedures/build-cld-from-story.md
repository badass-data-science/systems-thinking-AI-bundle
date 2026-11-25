---
id: build-cld-from-story
type: procedure
title: Build a causal loop diagram from a story
summary: "Five steps in order: list the quantities, add polarity-marked arrows one at a time with any delays, check the chain closes, trace and label each loop, then read the whole loop aloud as a sentence a domain expert would nod along to."
chapters: [10]
inputs: [A plain-language description of a problem (five or six sentences, the way a colleague would tell it), Access to someone who knows the domain]
outputs: [A CLD with polarity on every link, typed delay marks and R/B labels, A spoken version of each loop, Notes on which nodes are stocks, flows or neither]
links:
  uses: [causal-loop-diagram, trace-loop-polarity, delay]
  related: [translate-cld-to-stock-and-flow, live-build-technique]
series: [feedback]
---

## When to use

Whenever a problem reaches you as a narrative rather than a diagram, which is almost always.

## Steps

1. **List the quantities** the story mentions. Phrase each so "higher" means "more of that thing." Add a node wherever the story's logic needs one; for example, if defects cut how fast a stockpile grows rather than removing stock, the chain must run through "stockpile growth," not straight into the stockpile.
2. **Add arrows one at a time.** For each, ask: when the cause rises, does the effect rise (`+`) or fall (`−`)? Ask too whether the effect arrives late. If it does, add a delay mark and name its kind (information or material).
3. **Check that the chain closes.** A chain that never returns to its start holds no feedback, however busy it looks.
4. **Trace each closed loop**, count its minus signs, and label it `R` (even) or `B` (odd).
5. **Read it out loud**, start to finish, to a colleague or an AI collaborator, as one sentence a domain expert would have to nod along to. Where they wince, a link is wrong or missing.

Optionally, then classify each node in stock-and-flow terms (stock, flow, or neither) to prepare for quantification.

## Checks

- Every node is a quantity, not an event.
- Every loop label came from a trace.
- The spoken version survives the people who work in the part of the system each link describes.
- Any arrow into a stock is read as "adds to," not "moves with."

## Common mistakes

- A chain that never closes, dressed up as a loop.
- Trusting a clean, "obviously right" first draft. Internal consistency and narrative truth are different properties, and only one shows on the page; a tidy first draft deserves more suspicion, not less.
- Letting a tool's automated loop detection replace the trace and the read-aloud test.
- Reading `+` into a stock as "moves together": a stock keeps rising while its net inflow is positive, even if that inflow is shrinking.

## Worked example

Story: when finished stock runs low, the next raw-material order is placed under time pressure; when the rushed material reaches the processing stage two weeks later, corners get cut; cut corners lower quality; lower quality raises the downstream defect rate; more defects mean the finished stock grows more slowly, so it stays low. Nodes: finished stock, order urgency, corner-cutting, processed quality, defect rate, effective stock growth. Links: stock → urgency `−`; urgency → corner-cutting `+` (material delay: the rushed material in transit); corner-cutting → quality `−`; quality → defect rate `−`; defect rate → growth `−`; growth → stock `+`. Four minus signs: reinforcing, running in its vicious direction. Each department knew its own stretch; nobody had drawn the whole.
