---
id: attention-decay-and-tempo
type: case
title: Regulatory attention that decays slower than operations repeat
summary: Inspections landing about ten weeks after each major operation, produced by a slowly decaying stock of regulatory attention and an operating tempo that never checks it.
chapters: [5, 6, 8, 9]
source_example: "Interpol Attention Level ('Interpol heat'), introduced with the Chapter 5 raid"
links:
  uses: [iceberg-analysis, stock, delay]
  related: [balancing-loop, oscillation-and-overshoot]
mnemonic: "'Heat' here is Interpol's attention, never temperature. No thermometer could read it."
---

## Situation

An organization's units are inspected by an outside authority: four inspections in eighteen months, each roughly ten weeks after a major operation. Each was handled as a one-off.

## Analysis

Iceberg bands: the event is one inspection. The pattern is the regular ten-week lag. The structure is a stock (the authority's accumulated attention) that every operation adds to and that drains slowly over months, while operations happen weeks apart and the organization never sets its tempo by checking current attention against a threshold. The mental model is "we've always run at this pace and mostly gotten away with it."

Later chapters reuse this system: Ch. 6 draws its loops, Ch. 8 adds a balancing loop with an implicit goal ("acceptable attention"), and Ch. 9 shows how the slow decay makes that loop oscillate.

## Lesson

A slow-draining stock plus a decision rule that doesn't look at it produces a regular pattern that no single event explains. "Mostly gotten away with it" and "the structure is safe" feel identical until the stock accumulates faster than it drains.
