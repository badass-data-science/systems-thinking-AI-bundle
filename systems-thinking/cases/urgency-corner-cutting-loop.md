---
id: urgency-corner-cutting-loop
type: case
title: Urgency, corner-cutting and defects
summary: A low finished-goods stockpile triggers rushed orders, rushed material gets corners cut at processing two weeks later, quality falls, defects rise, and the stockpile grows more slowly, keeping it low; a vicious reinforcing loop nobody had drawn whole.
chapters: [10, 1, 5, 16]
source_example: "The Doomsday Device Supply Chain CLD (Chapter 10, Figure 10.1)"
links:
  uses: [build-cld-from-story, delay]
  instance-of: [reinforcing-loop]
  related: [supply-chain-recurring-misses, quantified-supply-chain-model]
structure:
  variables: [finished stockpile, order urgency, corner-cutting, processed quality, defect rate, effective stockpile growth]
  links:
    - {from: finished stockpile, to: order urgency, polarity: "-"}
    - {from: order urgency, to: corner-cutting, polarity: "+", delay: material}
    - {from: corner-cutting, to: processed quality, polarity: "-"}
    - {from: processed quality, to: defect rate, polarity: "-"}
    - {from: defect rate, to: effective stockpile growth, polarity: "-"}
    - {from: effective stockpile growth, to: finished stockpile, polarity: "+"}
  loops:
    - {id: R1, type: R, label: urgency spiral, path: [finished stockpile, order urgency, corner-cutting, processed quality, defect rate, effective stockpile growth]}
---

## Situation

This is the structure under the recurring deadline misses. The ordering desk knows about urgency; the refinery knows about corner-cutting and quality drift; assembly knows about defect rates. Nobody had drawn the six links end to end.

## Analysis

Four minus signs: reinforcing, in its vicious direction. The corner-cutting happens when the rushed material arrives, a couple of weeks after the order: a material delay, and the delay is the rushed material in transit (a hidden stock).

Read aloud: "When the stockpile runs low, we rush the next order; when that material reaches processing two weeks later, the rush means cutting corners; cut corners mean worse quality, worse quality means more defects, and more defects mean fewer units reach stock, which is what started the rush."

Node types: the stockpile is a stock; effective growth is a flow (units assembled minus failures); urgency, corner-cutting, quality and defect rate are auxiliaries; the delay hides a stock of rushed material in transit. A possible second delay: does the ordering desk learn the stockpile is low the day it happens, or at the next weekly count? (The latter would be an information delay.)

## Lesson

This unchanged interconnection is why each quarter's fix moved the failure to a different link. A structure spread across departments is invisible to each of them; drawing it whole is the first step to changing it.
