---
id: building-this-book-with-an-agent
type: case
title: Building a book with an AI agent
summary: A human author and an AI coding agent built a book together; the decision loop (options, a choice, done) worked, while the checking loop kept stopping early because each check saw only its own boundary and kind.
chapters: [24]
source_example: "Our Heroine and Her AI Henchman: the making of Systems Thinking for Supervillains (Chapter 24, Figure 24.1)"
links:
  uses: [audit-your-checks, iceberg-analysis]
  instance-of: [checking-loop]
  related: [convenience-boundary-trap, unrun-code-is-an-unchecked-citation, a-trace-is-not-a-definition, standards-specific-enough-to-fail]
series: [ai-delegation, model-validation]
---

## Situation

An AI coding agent worked directly in a book's files (drafting chapters, writing figure code, running scripts that renumber, assemble and check the book) while the author set direction, made decisions, reviewed results and wrote prose.

## Analysis

**The loop that worked.** When the agent reached a question only the author could settle, it stopped, laid out two to four real options with trade-offs, and recommended one; the author chose. A balancing loop: open questions → options (`+`) → choices (`+`) → open questions (`−`). The answer came back in the same conversation, so there was no delay and no wobble.

**The loop that stopped early.** The outline was declared consistent at least four times; each later pass found a different class of problem. Each pass had a defensible scope and felt complete until something just outside it mattered: the convenience trap, applied to checks. More instances: a knowledge graph of the draft built in two parallel batches lost a cross-reference whose two ends sat in different batches; a renumbering script worked from a hand-typed list of chapter files that omitted the front matter, and a full audit missed it because it never opened the front matter. The agent that wrote that script had already drafted the diagnosis of this trap.

**Wrong kind of check.** A reference by position ("last chapter") is invisible to a search for "Chapter N"; a script that shifted numbers inside a historical description kept the arithmetic consistent while making the history false; a nonexistent citation looked like its real neighbors; printed results came from no model; archetype diagrams traced correctly but weren't the archetype; a figure description too vague to fail passed a wrong layout. What found these was a different *kind* of check: running a model, looking up a source, reading the literature, comparing with a specific description. Even one of the agent's own review findings was wrong, caught when it reopened the tool's documentation before changing anything.

## Lesson

Humans mostly supplied the new sensors (is this citation real? does this diagram match its archetype?); the agent then checked quickly and thoroughly. When something gets past a check, fix the check. Replace "a clean pass means it's right" with "a clean pass means nothing this check can see is wrong."
