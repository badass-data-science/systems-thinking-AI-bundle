---
id: ai-accelerated-shipping
type: case
title: AI-accelerated shipping, three orders deep
summary: An AI coding agent speeds feature delivery (first order); review depth falls as shipping and review undermine each other (second order, Accidental Adversaries); and first-principles debugging skill atrophies (third order, Shifting the Burden).
chapters: [22, 15, 11]
source_example: "The henchman engineering team's AI-augmented death-ray control software (Chapter 22, Figures 22.1-22.2)"
links:
  uses: [trace-three-orders]
  instance-of: [accidental-adversaries, shifting-the-burden]
  related: [ai-agent-as-intervenor]
structure:
  variables: [shipping success, reviewable changes, review success, timely reviews, AI-assisted shipping volume, review shortcuts, defects reaching production]
  links:
    - {from: shipping success, to: reviewable changes, polarity: "+"}
    - {from: reviewable changes, to: review success, polarity: "+"}
    - {from: review success, to: timely reviews, polarity: "+"}
    - {from: timely reviews, to: shipping success, polarity: "+"}
    - {from: shipping success, to: AI-assisted shipping volume, polarity: "-"}
    - {from: AI-assisted shipping volume, to: shipping success, polarity: "+"}
    - {from: review success, to: review shortcuts, polarity: "-"}
    - {from: review shortcuts, to: review success, polarity: "+"}
    - {from: AI-assisted shipping volume, to: reviewable changes, polarity: "-"}
    - {from: review shortcuts, to: defects reaching production, polarity: "+", delay: material}
    - {from: defects reaching production, to: shipping success, polarity: "-"}
  loops:
    - {id: R1, type: R, label: partnership, path: [shipping success, reviewable changes, review success, timely reviews]}
    - {id: B1, type: B, label: ship more, path: [shipping success, AI-assisted shipping volume]}
    - {id: B2, type: B, label: review faster, path: [review success, review shortcuts]}
    - {id: R2, type: R, label: adversarial, path: [AI-assisted shipping volume, reviewable changes, review success, review shortcuts, defects reaching production, shipping success]}
---

## Situation

An engineering team adopts an AI coding agent for a large share of implementation work on control software.

## Analysis

**First order**: features ship dramatically faster. Real and good.

**Second order**: review capacity didn't grow with shipping volume, so review depth per change falls. Shipping and review are natural allies (reviewable changes let reviewers work well; timely reviews help shipping succeed). Behind schedule, shipping leans on the agent for more volume, which leaves each change harder to review. Swamped, review takes shortcuts, which clears its queue and lets more defects reach production; they come back, after deploy, as hotfix pressure on shipping. The inner loop has four minus signs: Accidental Adversaries, with the delay on the escaped-defects link.

**Third order**, six months out: the person who could debug a control-loop failure from first principles hasn't had to in so long that the skill has measurably atrophied. Shifting the Burden: the AI-generated fix is the ever-available symptomatic option.

## Lesson

Keep the gain, manage the risk with known remedies: count a feature as shipped only once it's reviewed, and grow review capacity (AI-assisted review included) alongside shipping volume; schedule first-principles debugging drills without the agent.
