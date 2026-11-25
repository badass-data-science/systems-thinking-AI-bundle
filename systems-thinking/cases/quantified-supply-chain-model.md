---
id: quantified-supply-chain-model
type: case
title: Quantifying the supply chain
summary: Hand-iterating the supply chain shows refined material piling up, output capped by labor hours rather than refining, zero schedule slack, and a dormant corner-cutting loop that a three-week shock turns from a 30-ton gap into a 285-ton one.
chapters: [16, 17, 18]
source_example: "The quantified Doomsday Device Supply Chain (Chapter 16 table and Figures 16.1-16.2; quantified-supply-chain.xmile)"
links:
  uses: [hand-iterate-a-model, translate-cld-to-stock-and-flow, co-flow]
  related: [urgency-corner-cutting-loop, supply-chain-recurring-misses, pysd]
---

## Situation

Stocks: material in ground, in transit (180 tons, two-week residence), refined on hand (starts at 50 tons), finished stockpile (starts at 0). Flows: mining 90 tons/week; refining = min(in transit ÷ 2, 100) × 0.9 = 81; refining losses 9 tons/week to a cloud; assembly = min(on hand, 60), the 60 set by labor hours under a regulator's mandatory rest-break schedule.

## Analysis

Eight weeks by hand: refined on hand 71, 92, 113, ... 218; stockpile 60, 120, ... 480. The refinery out-produces assembly by 21 tons a week; output is capped by labor hours throughout; the people arguing for a bigger refinery were optimizing the wrong constraint.

Translating the CLD (Ch. 10) adds a co-flow of *rushed* material in transit, a defect-scrap drain on the stockpile, a schedule and stockpile-shortfall node (the comparison the CLD's stockpile → urgency arrow hid), and auxiliaries for urgency, corner-cutting, quality and defect rate. Run with the loop, the eight weeks don't change by a ton: deadlines require exactly 60 a week, so urgency stays zero. The schedule has no slack.

Shock it: three weeks of assembly at 50. With corner-cutting switched off, the stockpile ends 30 tons behind and stays there. With the loop intact, rushing starts, rushed material reaches processing two weeks later, defects follow, and by week 16 the stockpile is 285 tons behind and still slipping, effective growth halved to 30 a week.

## Lesson

Numbers expose what the diagram can't: which constraint binds, how much slack exists, and how fast and far a loop runs once disturbed. The guessed parameters behind the shock result are what sensitivity analysis must test (Ch. 18). The model is in `code/quantified-supply-chain.xmile`.
