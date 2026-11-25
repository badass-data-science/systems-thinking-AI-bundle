# Pilot progress log

Working notes for the Systems Thinking pilot, kept so that the work can resume after an interruption. Newest entry at the bottom.

Book source version: chapter files as of commit 9225c37 in the book's private manuscript repository (last commit touching the book, 2026-11-09).

## Plan

1. Read the book chapter by chapter and write cards as I go (concepts, procedures, archetypes, heuristics, cases, tools). Commit after each batch of chapters.
2. Write the eval set.
3. Write SKILL.md (routing) and README.md (what this is, how to use it, how it was built).
4. Get `tools/build_bundle.py` passing with zero errors; generate graph.json, graph.ttl, INDEX.md.
5. Optional: a small MCP server over the bundle (`find_concept`, `get_procedure`, `match_archetype`, ...).
6. Write PILOT-NOTES.md: what the schema needed, what didn't fit, recommendations for the other books.

## Log

- 2026-11-21: Schema, build script and series concept list written. Chapters 1-3 carded.
- 2026-11-21: Chapters 4-7 carded. Optional `structure` blocks now allowed (and checked) on cases. Dangling links to cards not yet written are expected until Part III is done.
- 2026-11-21: Chapters 8-9 carded. Added `exogenous: true` for goal links feeding a loop from outside, and typed delays.
- 2026-11-21: Chapters 10-15 carded: all ten archetypes (plus the intervenor variant) with machine-checked structures, a growth-stall classifier, and a general archetype-diagnosis procedure.
- 2026-11-21: Chapters 16-17 carded, with tool cards. `code/` copies the book's published code (build warns on drift); fenced code is exempt from the costume lint.
- 2026-11-21: Chapters 18-23 carded (validation and sensitivity, leverage, AI trust loop, Cynefin delegation, second-order effects, knowledge graphs).
- 2026-11-21: Chapters 24-26 carded. All 26 chapters done: 176 cards, build passes with 0 errors; graph.json/graph.ttl/INDEX.md generated. Next: negative tests of the validator, evals, SKILL.md, README, MCP server, pilot notes.
- 2026-11-21: Validator negative tests (tools/test_build_bundle.py) pass. 55 evals written; build has 0 errors, 0 warnings (every procedure and archetype has an eval). graph.ttl parses in rdflib.
- 2026-11-21: SKILL.md written (build checks its routes). MCP server (tools/bundle_mcp_server.py) smoke-tested over stdio; match_archetype benchmarked on the recognition evals: 7/11 top-1, 9/11 top-3 (keyword-based; returns all diagnostic questions as a backstop). Remaining: README, PILOT-NOTES.
- 2026-11-21: Style pass (dash summaries, pronouns). Ran all three code scripts: outputs match the cards. README.md and PILOT-NOTES.md written. Pilot complete; open items are listed in PILOT-NOTES.md.
- 2026-11-23: Routing fixes from the retest. `SKILL.md`'s description now names incident follow-ups and postmortems (fresh-004) and groups disagreeing on what the problem is (fresh-029), trimmed elsewhere to stay within 1,024 characters (now 1,023); two routing rows added (incident under pressure → pressure-shrinks-the-iceberg, iceberg-analysis; contested problem → hard-and-soft-systems-thinking, soft-systems-methodology, catwoe, tame-messy-wicked-problems). The build now errors if the description is missing or over 1,024 characters. Not yet tested: fresh-004 and fresh-029 shaped these changes, so testing needs new held-out items.
- 2026-11-23: Retested the routing fixes on 30 new held-out items (`eval-results/2026-11-23-routing-retest/`). New 0.85, previous 0.82, no skill 0.70; both descriptions loaded on 30 of 30. New vs. previous +0.03 (interval −0.01 to +0.06). The new routing rows were used on the contested-problem and incident items and helped most on held-007 (0.62 vs. 0.38).
