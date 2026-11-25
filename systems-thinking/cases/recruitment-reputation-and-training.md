---
id: recruitment-reputation-and-training
type: case
title: Recruitment reputation and training capacity
summary: A reinforcing reputation loop and a balancing training-capacity loop sharing a path, where the reinforcing loop dominates while the workforce is small and the balancing loop takes over once headcount outgrows the trainers.
chapters: [6, 7, 13]
source_example: "The Henchman Recruitment & Morale Pipeline (Chapter 6, Figure 6.1; run forward in Chapter 7)"
links:
  uses: [trace-loop-polarity, causal-loop-diagram]
  instance-of: [limits-to-growth]
  related: [snowballing]
structure:
  variables: [success rate, recruiting reputation, applicants, headcount, training time per person, execution quality]
  links:
    - {from: success rate, to: recruiting reputation, polarity: "+"}
    - {from: recruiting reputation, to: applicants, polarity: "+"}
    - {from: applicants, to: success rate, polarity: "+"}
    - {from: applicants, to: headcount, polarity: "+"}
    - {from: headcount, to: training time per person, polarity: "-"}
    - {from: training time per person, to: execution quality, polarity: "+"}
    - {from: execution quality, to: success rate, polarity: "+"}
  loops:
    - {id: R1, type: R, label: reputation, path: [success rate, recruiting reputation, applicants]}
    - {id: B1, type: B, label: training capacity, path: [success rate, recruiting reputation, applicants, headcount, training time per person, execution quality]}
---

## Situation

An organization's project successes improve its reputation as an employer, which attracts more and better applicants, which produces more successes. Those applicants also become headcount, and a fixed training staff is spread thinner across more people, so execution quality falls.

## Analysis

Trace R1: three `+` links, zero minus signs, reinforcing. Trace B1: six links with one `−` (headcount → training time per person), balancing. The loops share the path success → reputation → applicants. Three consecutive successes tripled the applicant pool, which let the organization select better people, which produced more successes: the reinforcing loop running forward. A live public rating of the employer shortens each round of the loop and so speeds it up.

## Lesson

Loop type comes from the trace, not the story. Two loops sharing a path is normal, and which loop dominates shifts as the system grows; here, the training staff is the limit that the reinforcing loop eventually runs into.
