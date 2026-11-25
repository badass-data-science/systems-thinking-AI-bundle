# Changelog

Notable changes to the bundle, newest first. Dates are absolute. Entries before 2026-11-25 summarize work done while the bundle lived beside the book's private manuscript; that history wasn't carried over.

## 2026-11-25: search ranking

- The MCP server's `search_cards` now ranks a card first when the query is its title, an alias or its id (ignoring case and punctuation), gives words in a card's title more weight than words in its summary, weights words by how rare they are across cards, counts each query word once, and keeps two-letter words such as "AI". Ties go to the shorter title. Searching each card's title now puts that card first for all 176 cards (was 153); without the exact-name rule, the weighting alone puts it first for 173 and in the top three for all 176. `match_archetype` is unchanged.
- `tools/test_bundle_mcp_server.py`'s floors raised to the new rates, with checks for partial titles, ids, apostrophes, two-letter words and repeated words.

## 2026-11-25: tests and CI

- New tests: `tools/test_bundle_mcp_server.py` (52 checks: every MCP tool, planted errors for `check_loops`, and floors on search and archetype matching at today's rates) and `tools/test_run_evals.py` (29 checks, offline: a stand-in `claude` script plays the answering model and the grader).
- New CI workflow (`.github/workflows/ci.yml`) running all six checks on Python 3.10 and 3.14, plus checks that the generated files are up to date, that `graph.ttl` parses, and that `eval-results/` has no local paths. Badges added to `README.md`.
- New `requirements.txt`. `mcp` is now held below version 2: version 2 renamed `FastMCP`, so `pip install mcp` installed a version the MCP server couldn't import. Install steps in `README.md` changed to `pip install -r requirements.txt`.
- Fix: the MCP server's `check_loops` raised an exception when given text that parsed as YAML but wasn't a mapping (a sentence or a list); it now returns a message.
- `README.md`'s archetype-matching figures corrected to the current 23 recognition evals: 10 right at rank 1, 15 in the top three (it said 7 and 9 of 11).
- The "before every commit" list in `AGENTS.md` and `README.md` gains the two new tests.

## 2026-11-25: moved to its own public repository

- The bundle now lives in this repository instead of an `ai-bundle/` folder in the book's private manuscript repository. It was copied as a snapshot; the earlier commit history stays private.
- **No script reads the book any more.** `tools/review_archetypes.py` reads copies of the book's eleven archetype `.cld` files in `archetype-review/cld/` instead of the manuscript's image folder. It no longer embeds the book's figures (each page names the figure number instead) or quotes the book's text: the Limits to Growth page, which had quoted a whole Chapter 13 section, now names that section to read instead. The machine check's results are unchanged (all eleven archetypes as before).
- `tools/build_bundle.py`'s code-drift check is now opt-in. Set `BUNDLE_CODE_SOURCE` to a folder holding the book's published code, for example the `systems-thinking-for-supervillains/` folder of <https://github.com/badass-data-science/books>; without it, the check is skipped. Generated files (`graph.json`, `graph.ttl`, `INDEX.md`) are byte-identical to before.
- Local scratch-folder paths recorded in the 2026-11-23 eval run's tool calls are replaced with `<scratch>`.
- References to the manuscript's private paths, branch and planning notes removed from `README.md`, `PILOT-NOTES.md`, `PROGRESS.md` and `SCHEMA.md`.
- New: `AGENTS.md`, this changelog and `.gitignore`. `README.md` rewritten for the repository, with stale counts corrected (115 evals, 899 graph edges).

## 2026-11-23

- Routing fixes: `SKILL.md`'s description names incident follow-ups and postmortems, and groups disagreeing on what the problem is; two routing rows added. The build errors if the description is missing or over 1,024 characters.
- Retested on 30 new held-out items: 0.85 with the new description, 0.82 with the previous one, 0.70 without the skill (`eval-results/2026-11-23-routing-retest/`).
- Archetype structure review added (`archetype-review/`, `tools/review_archetypes.py` and its tests): every archetype card's structure checked against the book's diagrams; all match, two by simplifying the book's diagram.
- Limits to Growth cards: the limit is often removable, and a delay is a variant, not part of the archetype.

## 2026-11-22

- `SKILL.md` description revised and retested on 30 held-out items written before the change: the skill loaded on 29 of 30 and scored 0.84, against 0.70 without it (`eval-results/2026-11-22-description-retest/`).

## 2026-11-21

- First version, built by an AI agent in one session: 176 cards from all 26 chapters and the appendices, 55 evals, `SKILL.md`, the build and its negative tests, the MCP server, and `tools/run_evals.py`.
- First eval run: Sonnet's mean score rose from 0.78 without the skill to 0.96 with it (`eval-results/2026-11-21-sonnet-graded-by-opus/`).
