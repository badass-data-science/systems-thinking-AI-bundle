# Systems Thinking AI Bundle: notes for AI agents

This repository is public. It holds the AI bundle for *Systems Thinking for Supervillains* by Lady Napalm: an Agent Skill (`systems-thinking/`) of 176 cards, its evals and eval results, the archetype structure review, and the tools that validate and build them. `README.md` describes the layout; `SCHEMA.md` is the card format. Read both before changing anything.

## Privacy: the book stays private

The book's manuscript lives in a separate private repository. This repository must never depend on it or leak it.

- **No build, test or review script may read the book's files.** Everything here must run from a fresh clone of this repository alone. The two places that used to reach into the manuscript now use local copies: `archetype-review/cld/` (copies of the book's archetype `.cld` diagram sources) and `systems-thinking/code/` (the book's code, already public in <https://github.com/badass-data-science/books>).
- **Never copy the book's prose here.** Cards restate the book's methods in neutral terms and cite chapters by number; they don't quote paragraphs. Short quoted phrases a card needs (a named model, a mnemonic) are fine; sections of chapter text are not. `review_archetypes.py` once quoted a whole Chapter 13 section into `archetype-review/limits-to-growth.md`; that was removed in the move to this repository, so don't reintroduce it.
- **No private paths, names or links.** Don't write local file paths (`/home/...`, `/tmp/claude-...`), the manuscript repository's paths or branch names, or private notes into anything committed. `tools/run_evals.py` records the scratch folder in each answer's tool calls, so before committing a new eval run, replace those paths:

  ```bash
  grep -rlE '/tmp/claude-[0-9]+/[^/"]+/[0-9a-f-]{36}/scratchpad' eval-results \
    | xargs -r sed -i -E 's#/tmp/claude-[0-9]+/[^/"]+/[0-9a-f-]{36}/scratchpad#<scratch>#g'
  grep -rniE '/home/|/tmp/claude' eval-results   # should print nothing
  ```

- The author is credited as **Lady Napalm**, her pen name. The name "Emily" appears only as part of "Emily's Laws of System Complexity," the book's authorized named model; don't use it anywhere else.

## Git: who commits

All commits and pushes here are made as the GitHub user **badass-data-science**. The repository's local git config sets that identity (`user.name badass-data-science`, with the account's GitHub noreply address) and pushes over SSH through the `github-badass` host alias. Check `git config user.name` before committing, and never commit with a global identity that differs from it.

Commit and push each fix as it's made. Branch and open a pull request for substantial changes; small fixes may go straight to `main`.

## Before every commit

```bash
python3 tools/build_bundle.py                # 0 errors expected; regenerates graph.json, graph.ttl, INDEX.md
python3 tools/test_build_bundle.py           # every planted bug still caught
python3 tools/review_archetypes.py --check   # archetype cards still match the book's diagrams
python3 tools/test_review_archetypes.py
```

Commit the regenerated `graph.json`, `graph.ttl` and `INDEX.md` together with the cards that changed them. Then add an entry to `CHANGELOG.md`.

## Conventions

- **Cards follow `SCHEMA.md`.** The build enforces required fields, body sections, typed links, chapter numbers (1–26 and appendices A–E), and that every archetype's loops close with the polarity they claim.
- **No costume.** The book's villainous framing (villains, henchmen, lairs, Interpol and so on) may appear only in a card's `mnemonic` and `source_example` fields and in fenced code; the build lints for it.
- **Gender-neutral language** in cards and evals ("chair," not "chairman"), apart from pronouns that refer to a specific person.
- **Write "AI agent" or "AI assistant,"** never bare "agent" or "assistant," when the meaning is the AI.
- **`SKILL.md`'s description must stay within 1,024 characters**; the build errors otherwise. Any routing row it adds must point to a card that exists.
- **`archetype-review/`:** running `tools/review_archetypes.py` without `--check` rewrites every page and erases any ticks or notes a reviewer has made. Use `--check` after editing a card, and copy reviewers' notes out before regenerating. If the book redraws an archetype diagram, copy its new `.cld` into `archetype-review/cld/` (the author supplies it; don't reconstruct it).
- **`systems-thinking/code/` mirrors the public `books` repository's `systems-thinking-for-supervillains/` folder.** Don't edit these files here alone: a change belongs in the book's code first. To check for drift, clone `books` and run the build with `BUNDLE_CODE_SOURCE` pointing at that folder.
- **Eval results are records.** Don't edit a past run's answers or grades; add a new dated folder for a new run, with a README giving the setup and caveats.
- **No word-wrapping inside a paragraph or list item** in Markdown: each is one line.
- Don't fabricate citations. Every source a card names must be real and match the book's bibliography.

## Where the companion volume fits

A separate, private companion book documents how to install, use and maintain this bundle. When you change something it describes (card counts, eval results, tool names or behavior, install steps), mention it in `CHANGELOG.md` so the companion volume can be updated to match.
