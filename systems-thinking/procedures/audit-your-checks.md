---
id: audit-your-checks
type: procedure
title: Audit your checks for boundary and kind
summary: List every check a piece of work has been through, write each one's boundary (what it looked at) and kind (what it could notice), find something none of them could catch, and add a check of a different kind rather than a wider version of an old one.
chapters: [24]
inputs: [A model, document, codebase or other work product, The checks it has been through (rereads, scripts, tests, AI passes, reviews)]
outputs: [A table of checks with boundary and kind, At least one blind spot no check covers, A new check of a different kind]
links:
  uses: [checking-loop, every-check-has-a-boundary-and-a-kind]
  related: [validate-a-model, standards-specific-enough-to-fail]
series: [model-validation, ai-delegation]
---

## When to use

Before declaring any substantial piece of work done, especially work an AI agent helped produce and check.

## Steps

1. List every check the work has passed: your own rereads, scripts, tests, sensitivity swings, AI reviews, human reviews.
2. For each, write its **boundary**: exactly which files, sections or parts it examined. Was that list generated from the system itself, or typed by hand?
3. For each, write its **kind**: what it can notice (numbering, presence, consistency, existence in the world, match to a definition, whether code runs).
4. Mark at least one thing about the work that none of the checks could have caught (an assumed link nobody has asked about; a citation nobody looked up; code nobody ran).
5. Design one new check that would catch it. Note whether it's a wider version of an old check or a different kind; prefer a different kind.
6. Record the result as "nothing these checks can see is wrong," not "it's right."

## Checks

- Each check has both a boundary and a kind written down.
- At least one blind spot is named.

## Common mistakes

- Running the same kind of check again, harder.
- Boundaries built from hand-typed lists (a renumbering script that never saw the front matter).
- Splitting work into batches that each see only half of a cross-reference.
- Treating an AI agent's confident "done" as a wider check than it was.
