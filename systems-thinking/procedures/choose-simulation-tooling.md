---
id: choose-simulation-tooling
type: procedure
title: Choose spreadsheet, simulation software, or PySD
summary: Before opening any software, draw a three-branch decision tree (stay in the spreadsheet, move to dedicated software, go straight to PySD) and write the specific trigger that would justify each.
chapters: [17]
inputs: [A stock-and-flow model, The question it must answer, Who needs to read, run or edit it]
outputs: [A chosen tooling branch, The trigger sentence that justifies it]
links:
  uses: [software-is-escalation-of-commitment]
  related: [vensim, pysd, insight-maker, anylogic]
---

## When to use

When hand iteration starts to strain: a model with dozens of stocks, several analysts on different machines, or a question that needs many parameter combinations.

## Steps

1. **Spreadsheet** branch: write the need it meets (a handful of stocks, one analyst, a few scenarios, readable by anyone).
2. **Dedicated software** (Vensim, Stella; Insight Maker for free and small) branch: write its trigger (native diagramming a team reads, built-in Monte Carlo and sensitivity, many stocks).
3. **PySD** branch: write its trigger (the model must feed a Python pipeline, a formal sensitivity analysis with SALib, or an AI agent that queries it).
4. If the question needs individual actors or discrete events, note that it has left pure system dynamics (AnyLogic, actor-based modeling) and decide that on purpose.
5. Pick the branch your current question is really on, then check it against the escalation-of-commitment costs.

## Checks

- Each branch has a concrete trigger, not "it would be nice."
- Whatever you choose, you'll verify the first run against a known result.

## Common mistakes

- Escalating because it feels more rigorous.
- Treating a model that runs without errors as validated.
