# Systems Thinking AI Bundle

*Systems Thinking for Supervillains: Feedback, Causality, and Mental Models for the Age of Agentic AI* by Lady Napalm, compiled into a structured bundle that an AI agent can load, query and be tested against, with the book's villainous framing removed. It holds the book's methods, not its prose.

The main thing here is **`systems-thinking/`**, an Agent Skill: a `SKILL.md` entry point that routes the agent to the right one of 176 cards (concepts, procedures, archetypes, heuristics, cases and tools), each a Markdown file with YAML frontmatter.

## Status

- **Done and checked:** all 26 chapters and the appendices are carded. The build passes with no errors or warnings, and the validator's negative tests pass. The book's three scripts run from `systems-thinking/code/` and reproduce the numbers the cards quote. `graph.ttl` parses and answers SPARQL, and the MCP server works over stdio.
- **Evals run:** with the skill loaded, Sonnet's mean score on the 55 core evals rose from 0.78 to 0.96, and it loaded the skill on 37 of 55 items. After the `SKILL.md` description was revised, it loaded the skill on 29 of 30 held-out items and scored 0.84, against 0.70 without the skill. A 2026-11-23 retest of two routing fixes on 30 more held-out items scored 0.85 against 0.70 without the skill. See `eval-results/`.
- **Archetype review:** a script has checked the eleven archetype structures against the book's own causal loop diagrams (`archetype-review/`), but no person has yet judged whether the neutral variable names keep the book's meaning.

## Quick start

```bash
pip install pyyaml mcp                   # build and MCP server
pip install pysd SALib rdflib            # only to run the book's code
cp -r systems-thinking ~/.claude/skills/ # install as a Claude Code skill
```

Then ask Claude Code about a recurring problem, a feedback loop or what to delegate to an AI agent, and it will load the skill.

## What's here

| Path | What it is |
|---|---|
| `systems-thinking/` | **The downloadable artifact.** An Agent Skill: `SKILL.md` (entry point and routing) plus 176 cards. Copy or zip this folder. |
| `systems-thinking/concepts/` (53) | Definitions, distinctions, typed links. |
| `systems-thinking/procedures/` (21) | Step-by-step methods with inputs, outputs, checks and common mistakes. |
| `systems-thinking/archetypes/` (11) | The ten archetypes plus the intervenor variant, each with a machine-checked causal loop structure. |
| `systems-thinking/heuristics/` (41) | "When you see X, do Y" rules. |
| `systems-thinking/cases/` (38) | Worked examples, mostly the book's restated in neutral terms, plus the real-world cases it cites. |
| `systems-thinking/tools/` (12) | Software and standards (PySD, SALib, XMILE, Vensim, Kumu, RDF stores, Neo4j, ...). |
| `systems-thinking/evals/` (115) | Scenario-based evals, all new scenarios, with expected points and pitfalls for grading: 55 core items plus 60 held-out items written for the retests. |
| `systems-thinking/code/` | The book's published code: the XMILE model and the PySD, SALib and rdflib scripts, also at <https://github.com/badass-data-science/books/tree/main/systems-thinking-for-supervillains>. |
| `systems-thinking/graph.json`, `graph.ttl`, `INDEX.md` | Generated: the card graph as JSON and RDF (176 nodes, 899 edges), and a catalog. |
| `SCHEMA.md` | The card format, written to work for every book in the series. |
| `series-concepts.yaml` | Provisional series-level concepts that cards in different books link to. |
| `archetype-review/` | The archetype structure review: one page per archetype, the proposed name mapping (`mappings.yaml`) and copies of the book's archetype diagram sources (`cld/`). |
| `eval-results/` | One folder per eval run: answers, grades, summary and caveats. |
| `tools/build_bundle.py` | Validates every card and eval, checks archetype loops close with the polarity claimed, lints for leftover costume words, checks `SKILL.md` routes and (optionally) code drift, then writes the generated files. |
| `tools/test_build_bundle.py` | Plants five known bugs in a copy of the bundle and confirms the validator reports each one. |
| `tools/review_archetypes.py` | Compares each archetype card's structure with the book's diagram and writes `archetype-review/`. |
| `tools/test_review_archetypes.py` | Plants known errors and confirms the review script reports each one. |
| `tools/bundle_mcp_server.py` | A book-agnostic MCP server over any bundle (search, cards, graph neighbours, archetype matching, evals, and `check_loops`). |
| `tools/run_evals.py` | Runs the evals with and without the skill through headless `claude -p` and grades the answers blind with a second model. |
| `tools/bench_match_archetype.py` | Measures the MCP server's archetype matching against the recognition evals. |
| `tools/quote_frontmatter.py` | Quotes frontmatter values containing `: ` so YAML parses them. |
| `PILOT-NOTES.md` | What the pilot found, decisions made, and recommendations for the other books. |
| `PROGRESS.md` | The working log kept during the build. |

## Using it

**As an Agent Skill (Claude Code, Claude apps, or any agent that reads skills).** Copy `systems-thinking/` into a skills directory, for example `~/.claude/skills/systems-thinking/`. `SKILL.md`'s description tells the agent when to load it, and its routing table points to the right card for the situation. To make a single file to hand someone:

```bash
zip -r systems-thinking-skill.zip systems-thinking
```

**As an MCP server.** Needs `pip install mcp pyyaml`.

```bash
claude mcp add systems-thinking -- python3 /full/path/to/tools/bundle_mcp_server.py /full/path/to/systems-thinking
```

The most useful tool is `check_loops`, which runs the book's trace-and-count rule on a diagram the agent has drawn, so loop labels come from a deterministic check rather than the agent's feel. `match_archetype` is keyword-based (7 of 11 recognition evals right at rank 1, 9 of 11 in the top three); it returns every archetype's diagnostic question so the agent can ask them all.

**As plain files.** Every card is Markdown with YAML frontmatter, readable by a person and loadable by any retrieval system. `graph.ttl` loads into any RDF store or `rdflib`; `SKILL.md` has an example SPARQL query.

## Rebuilding

Everything here builds from this repository alone; nothing reads the book's text. After editing any card or eval:

```bash
python3 tools/build_bundle.py                # validate and regenerate; exits 1 on any error
python3 tools/test_build_bundle.py           # confirm the validator still catches planted bugs
python3 tools/review_archetypes.py --check   # archetype cards still match the book's diagrams
python3 tools/test_review_archetypes.py      # confirm the review script still catches planted errors
```

To check that `systems-thinking/code/` still matches the book's published code, point the build at a checkout of it:

```bash
git clone https://github.com/badass-data-science/books.git
BUNDLE_CODE_SOURCE=books/systems-thinking-for-supervillains python3 tools/build_bundle.py
```

Without `BUNDLE_CODE_SOURCE`, that check is skipped.

## How it was made

An AI agent (Claude Code) built the bundle in one unattended session, reading the book chapter by chapter; `PROGRESS.md` is its working log and `PILOT-NOTES.md` its findings. It was developed alongside the book's private manuscript and moved to this repository on 2026-11-25; see `CHANGELOG.md`.

## License

MIT; see `LICENSE`. The book itself is not part of this repository.
