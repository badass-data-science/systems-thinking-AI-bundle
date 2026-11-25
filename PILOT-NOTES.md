# Pilot notes: compiling a book into a skill

Findings from compiling *Systems Thinking for Supervillains* into the bundle in `systems-thinking/`, written for deciding whether and how to do the same for the other books. The pilot was run end to end by an AI agent while the author was away, so the "Decisions made" section lists every call that would normally have been the author's.

*Written during the pilot, while the bundle still lived beside the book's private manuscript. Where these notes refer to that layout, the current one is described in `README.md` and `CHANGELOG.md`.*

## Results in one paragraph

All 26 chapters and the appendices became 176 cards (53 concepts, 21 procedures, 11 archetypes, 41 heuristics, 38 cases, 12 tools), about 43,000 words, plus 55 evals. The card format proposed in the discussion held for the whole book with two small additions. The validator passes with no errors or warnings, every procedure and archetype has at least one eval, the RDF graph parses and answers SPARQL, the copied book code runs and reproduces the numbers the cards quote, and a book-agnostic MCP server works over stdio. **The evals were run after the pilot** (`eval-results/2026-11-21-sonnet-graded-by-opus/`). On the 37 items where Sonnet loaded the skill, its mean score rose from 0.78 to 0.96, better on 26 items and worse on none. On the 18 items where it didn't load the skill, the difference was +0.01, which is the noise floor. The rubric and the cards share an author, so the gain may be overstated. A revised `SKILL.md` description then raised loading on 30 held-out items, written by a separate session, from 19 to 29. It also raised the mean gain over no skill from +0.09 to +0.14 (`eval-results/2026-11-22-description-retest/`).

## What the schema needed

The schema in `SCHEMA.md` is the one sketched in the discussion, written down. Over 26 chapters it needed only these changes:

1. **`structure` on any card, not just archetypes.** Many cases draw a specific causal loop diagram (the supply chain's urgency loop, the regulatory-attention loop, the AI trust loop, specification gaming). Letting them carry a checked structure turned out to be one of the most useful features. Twenty-one cards carry one: the eleven archetypes and ten others.
2. **Typed delays and exogenous links.** `delay: information | material` mirrors the book's own distinction. `exogenous: true` marks a goal feeding a loop from outside, so the validator doesn't warn that it sits on no loop. This is the book's point that a balancing loop seeks its goal but never sets it.
3. **Fenced code is exempt from the costume lint.** The book's model has a variable called `Refined Villainium On Hand`, and code must match the real file.

Nothing else changed. In particular, no new card types were needed. The original six covered everything, including the history chapters (as concepts and cases) and the meta case study in Chapter 24 (as a concept, a procedure, four heuristics and a case).

## What each check caught

In keeping with Chapter 24's lesson that every check sees only what it was built to see:

- **The YAML parse** caught four cards whose summaries contained a colon. A helper now quotes those values.
- **The costume lint** caught two real leaks: the model variable name (which led to the code exemption) and the word "villain" in a sentence of `live-build-technique.md`.
- **The archetype structure check** caught nothing during writing; every structure closed and matched its labels first time. The negative tests show it works. But it has the limit Chapter 24 names: a correct trace isn't a correct archetype. The eleven structures were written from the book's own figure descriptions and Toolkit boxes, and **no one but the agent that wrote them has compared them against the book's figures or against Senge.** That is the most valuable human review this bundle could get.
- **Link checking** found dangling links while cards for later chapters were still unwritten. All resolved.
- **Different-kind checks run at the end:** running all three code scripts (all reproduce the quoted numbers: the eight-week table, the SPARQL results, S1 = [0.55, 0.15], ST = [0.85, 0.44], S2 = 0.30); parsing and querying `graph.ttl`; greps for spaced-hyphen dashes (five summaries fixed), gendered pronouns (two rewritten) and filler words (25 left, about one per seven cards).
- **The archetype-matching benchmark** found the first version of `match_archetype` was poor (2 of 11 right at rank 1). Restricting it to the parts of each card that describe what the archetype looks like from outside, weighted by rarity, brought it to 7 of 11 at rank 1 and 9 of 11 in the top three. It stopped there deliberately. Tuning further against the same eleven evals would be fitting to history, which is Chapter 18's warning. Instead the tool returns every diagnostic question so the model can ask them all.

## What converted well and what didn't

- **Procedures and heuristics are the core, as predicted.** The book is dense with "if you see X, do Y" guidance; 41 heuristics was more than expected, and they carry much of its judgment. The Common mistakes sections of procedures carry the rest.
- **Archetypes convert best of all**, because the book already teaches them as structure plus diagnostic question plus leverage. The checkable `structure` block is the single most distinctive thing the bundle adds over the prose.
- **History chapters (2-3) convert to concepts and real-world cases** with little procedural content. That's fine: an AI needs to know what cybernetics or Soft Systems Methodology is, and the cases (the 1972 *Limits to Growth* study, Minsky, the pandemic delays) are good worked examples.
- **Neutralizing the costume was easy almost everywhere.** The recurring scenarios restate cleanly ("a regulator's accumulated attention," "a four-stage supply chain"). Each case keeps the book's name for its example in `source_example`, so a reader can find it. The `mnemonic` field was used on only nine cards, where the joke is the memory hook (the self-awarded "✓ Confidently Diagnosed" badge, "10, 30, 90, 270").
- **A few things can't be fully neutralized**: model variable names, Omen (a real tool, kept by name), and the name "Emily's Laws of System Complexity", kept verbatim, profanity included, since it is the book's authorized named model.
- **Not carded:** front matter, the dedication, the AI use statement, the bibliography as a list, and the figures themselves. Figures matter: several are the clearest statement of an idea. A future version could link cards to figure IDs.

## Weak points and recommendations

1. **Run the evals.** Grade a model's answers with and without the skill loaded, against each item's `expected` and `pitfalls`. Done after the pilot with `tools/run_evals.py`. See the results folder for the numbers and their limits. Still worth doing: a human grade of a sample, repeat runs, new items written by someone else, The two follow-ups the first retest found (incident follow-ups, contested problem definitions) were made and retested on 30 new items on 2026-11-23: the new routing rows were used and helped where they applied, but the previous description already loaded on all 30, so the incident wording's effect on loading is still unmeasured (`eval-results/2026-11-23-routing-retest/`).
2. **Human review of the eleven archetype structures** against the book's figures (see above).
3. **Provenance is chapter-level only.** Edits to the book won't flag the affected cards. The discussion suggested moving to source markup once the schema settles. It now has settled for one book. The cheap next step is section anchors (`chapters: [11#shifting-the-burden]`), and later `[PROCEDURE: id]`-style tags next to the existing `[IMAGE]` and `[CAPTION]` tags so the build can diff them.
4. **Matching belongs to the model, determinism to the server.** The MCP server's value is in what an LLM can't do reliably by itself: `check_loops` (deterministic polarity checking), exact card retrieval and graph traversal. Fuzzy matching is better done by the model reading `SKILL.md`'s routing table.
5. **The schema and tools are book-agnostic but live in this book's folder.** If a second book gets a bundle, move `SCHEMA.md`, `series-concepts.yaml` and `tools/` to a series-level location. Only the `VALID_CHAPTERS` range and the `st:` prefix in `build_bundle.py` are book-specific; both should become per-bundle settings.

## For the other books

- **Strategy for Supervillains.** Judging only from its chapter titles (not read for this pilot), likely series links are escalation ("The Ladder With No Top"), unintended consequences ("The Fix That Recruits"), systems ("War Is a System") and stakeholder worldviews. Expect a heavier share of heuristics and cases, since strategy is more judgment than procedure, exactly as the discussion predicted. Resist adding a new card type until a real chapter doesn't fit the six.
- **Agentic Time Series Forecasting for Supervillains.** Procedures there can name the Omen MCP tools they call, so the bundle complements the software rather than duplicating it. Its Chapter 21 (deterministic gates) is already referenced here as a series link.
- **Series concepts.** `series-concepts.yaml` has 19 provisional, domain-neutral concepts proposed from this book alone. Each new book should map its cards to them and add to the list instead of duplicating.

## Decisions made without the author

Logged so each can be reversed:

- Put the bundle in an `ai-bundle/` folder beside the book's manuscript, with the skill itself in `ai-bundle/systems-thinking/`. (Since 2026-11-25 it has its own repository.)
- IDs are filename stems, unique bundle-wide; cross-book IDs use a `st:` prefix.
- Copied the book's published code into the skill so it is self-contained, with a drift check, rather than linking to it.
- Named the author in `SKILL.md`'s description by the pen name the code README uses ("Lady Napalm"); no publication year, because none was verified.
- Added a few citation details the chapter text doesn't give (Meadows' "Leverage Points," 1999; Rittel and Webber in *Policy Sciences*, 1973). Both match Appendix E.
- Committed the generated files (`graph.json`, `graph.ttl`, `INDEX.md`) so the folder works without running the build.
- Did not edit any book chapter or the book's planning notes.
- Committed and pushed each step to the `artifact-discussion` branch. No pull request opened.

## Open questions for the author

1. Should the bundle be published alongside the book's code in the public `books` repository, and under what license? *(Answered 2026-11-25: in its own public repository, under the MIT License.)*
2. Is the edition stamp enough (a commit hash), or should bundles carry the book's published edition and date?
3. Keep the `mnemonic` field? Nine uses suggests it's worth having but easy to overuse.
4. Open a pull request from this branch, or keep iterating here first? *(Answered: merged before the move.)*
