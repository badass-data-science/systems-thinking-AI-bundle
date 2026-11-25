---
id: trace-loop-polarity
type: procedure
title: Trace and count a loop's polarity
summary: Mark every link + or -, trace the loop once and count the minus signs; even (including zero) is reinforcing, odd is balancing.
chapters: [6]
inputs: [A closed loop in a causal loop diagram, with nodes phrased as quantities]
outputs: [A polarity on every link, An R or B label for the loop, A check against your prior expectation]
links:
  uses: [causal-loop-diagram, feedback-loop]
  diagnoses: [reinforcing-loop, balancing-loop]
series: [feedback]
---

## When to use

Every time you label a loop, however obvious it looks. The book calls this its single most load-bearing technique.

## Steps

1. Check every node is phrased as a quantity where "higher" means "more of that thing." Rephrase any that aren't.
2. For each link, ask: if the cause rises, does the effect rise (`+`) or fall (`−`)? Mark it.
3. Before counting, write down what you *expect* the loop to be.
4. Trace the loop once around and count the `−` links.
5. Even count (0, 2, 4, ...): **reinforcing**. Odd count: **balancing**. Write `R` or `B` inside the loop.
6. If the result differs from your expectation, find the link that surprised you and recheck it.

## Checks

Why counting works: follow a single rise around the loop. A `+` passes it on unchanged; a `−` flips it. Two flips cancel. With an even count the rise returns as more rise (amplification); with an odd count it returns as pressure to fall (opposition).

Verify on a known case: success → reputation (`+`) → applicants (`+`) → success (`+`): zero minuses, R. Headcount → training time per person (`−`) → execution quality (`+`) → success (`+`) → reputation (`+`) → applicants (`+`) → headcount (`+`): one minus, B.

## Common mistakes

- Labeling by gut feel. A loop that "feels" like a growth spiral can hide one `−` link that flips the verdict.
- Assigning polarity to the loop from one striking link. Polarity belongs to the whole loop.
- Mixed node phrasing ("training shortfall" next to "training time"), which silently inverts signs.
- Reading R as good and B as bad. Neither carries a value judgment.
