---
id: growth-and-underinvestment
type: archetype
title: Growth and Underinvestment
summary: Growth runs into a capacity limit that investment could remove, but investment is deferred, and the demand lost to poor performance is read as proof that demand never justified investing, while the performance standard quietly erodes.
chapters: [14]
attribution: Peter Senge, The Fifth Discipline (1990)
diagnostic_question: Is a standing decision not to invest being "confirmed" by the very performance shortfall that decision is causing?
links:
  specializes: [limits-to-growth]
  requires: [delay, reference-point]
  related: [drift-to-low-performance, classify-a-growth-stall]
series: [limits-and-capacity]
structure:
  variables: [growth effort, demand, delivery performance, perceived need to invest, investment, capacity, performance standard]
  links:
    - {from: growth effort, to: demand, polarity: "+"}
    - {from: demand, to: growth effort, polarity: "+"}
    - {from: demand, to: delivery performance, polarity: "-"}
    - {from: delivery performance, to: demand, polarity: "+", delay: material}
    - {from: delivery performance, to: perceived need to invest, polarity: "-"}
    - {from: perceived need to invest, to: investment, polarity: "+"}
    - {from: investment, to: capacity, polarity: "+", delay: material}
    - {from: capacity, to: delivery performance, polarity: "+"}
    - {from: demand, to: perceived need to invest, polarity: "+"}
    - {from: delivery performance, to: performance standard, polarity: "+", delay: information}
    - {from: performance standard, to: perceived need to invest, polarity: "+"}
  loops:
    - {id: R1, type: R, label: growth, path: [growth effort, demand]}
    - {id: B1, type: B, label: capacity limit, path: [demand, delivery performance]}
    - {id: B2, type: B, label: investment, path: [delivery performance, perceived need to invest, investment, capacity]}
    - {id: R2, type: R, label: lost demand justifies underinvestment, path: [demand, perceived need to invest, investment, capacity, delivery performance]}
    - {id: R3, type: R, label: eroding standard, path: [delivery performance, performance standard, perceived need to invest, investment, capacity]}
---

## Signature

Growth (R1) strains capacity, and poor delivery eventually loses demand (B1). An investment loop (B2) is supposed to fix it: falling performance raises the perceived need to invest, and investment adds capacity after a real delay. Two reinforcing spirals turn the fix into a trap. In R2, lost demand lowers the perceived need to invest, so less capacity, worse delivery, more lost demand. In R3, poor performance slowly drags the "acceptable" standard down, which lowers the perceived need to invest. Neither spiral ever requires anyone to admit the original call was wrong.

## Symptoms

- The same don't-invest decision is relitigated and reconfirmed after every failure, using each failure as its evidence ("see, demand isn't reliable enough to build for").
- Capacity takes a long time to build, and the organization waits for proven demand before building it.
- What counted as poor delivery a few years ago is now normal.

## Interventions

- Judge the investment by the growth the system could have, not by the demand its own poor delivery has driven away.
- Given a long build time, invest ahead of demand rather than waiting for orders the current capacity can't fill.
- Hold the performance standard fixed (write it down), so falling performance reads as a problem to solve instead of the new acceptable level.

## Misapplications

- Treating every stall as underinvestment. If the limit isn't the system's own capacity, or the capacity is being expanded in step with demand, it's plain Limits to Growth.
- Explaining the failure as bad luck ("demand just happened to spike while we were stretched").

## Distinguish from

- **Limits to Growth**: there the wall is real and fixed; here it's a standing decision, fully removable.
- **Drift to Low Performance**: R3 is a drifting goal; in Growth and Underinvestment it sits inside a capacity-investment structure.
