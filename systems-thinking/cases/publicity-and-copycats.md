---
id: publicity-and-copycats
type: case
title: Publicity draws copycats, which draw attention
summary: A publicized operation attracts imitators into the same territory, whose activity raises the authorities' total attention there, which makes the next operation more visible and more publicized.
chapters: [7]
source_example: "The reinforcing side of Interpol Attention Level: copycat rivals (Chapter 7)"
links:
  instance-of: [reinforcing-loop]
  related: [attention-decay-and-tempo]
structure:
  variables: [publicity, copycats, regional attention]
  links:
    - {from: publicity, to: copycats, polarity: "+"}
    - {from: copycats, to: regional attention, polarity: "+"}
    - {from: regional attention, to: publicity, polarity: "+"}
  loops:
    - {id: R1, type: R, path: [publicity, copycats, regional attention]}
---

## Situation

A well-publicized operation in a region draws imitators into the same territory.

## Analysis

Publicity → copycats → regional attention from authorities → publicity of the next operation. Every link `+`, reinforcing. Different actors and a different currency from the recruitment loop, same mechanism.

## Lesson

The same stock of attention (see the regulatory-attention case) can sit on both a reinforcing loop and a balancing one. Look for both before predicting its trajectory.
