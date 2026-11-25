# Card Schema (pilot, v0.1)

This is the format every card in `systems-thinking/` follows. It's written for the Systems Thinking pilot but is meant to work for every book in the series, so nothing in it is specific to systems thinking except the `archetype` card's `structure` block, which other books can ignore. `tools/build_bundle.py` enforces everything marked *required* and fails the build on a violation.

## Files and IDs

- One card per Markdown file, YAML frontmatter first, then a Markdown body.
- The filename stem is the card's `id` (`balancing-loop.md` → `balancing-loop`). IDs are unique across the whole bundle, whatever folder a card sits in, so links never need a type prefix.
- Folders group cards by type: `concepts/`, `procedures/`, `archetypes/`, `heuristics/`, `cases/`, `tools/`. The `type` field must match the folder.
- Cross-book references use `<book-code>:<id>` (this book's code is `st`). A link to another book's card is allowed to dangle until that book's bundle exists; the build reports it as a warning, not an error.

## Common frontmatter (all card types)

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Same as the filename stem. |
| `type` | yes | `concept`, `procedure`, `archetype`, `heuristic`, `case` or `tool`. |
| `title` | yes | The name the book uses. |
| `summary` | yes | One sentence an AI could use as a definition or a retrieval snippet. |
| `chapters` | yes | Book chapters (integers) or appendices (`A`–`E`) where the idea is taught. The first entry is its home chapter. |
| `aliases` | no | Other names for the same thing, including names used elsewhere in the field. |
| `links` | no | Typed edges to other cards: a map from relation name to a list of IDs (see below). |
| `attribution` | no | Who the idea comes from (Meadows, Senge, Checkland, …), when the book credits someone. Original ideas from this book are marked `this book`. |
| `series` | no | IDs in `../series-concepts.yaml`: the series-level concepts this card is an instance of. This is how books link to each other. |
| `mnemonic` | no | The book's memory hook, kept in the book's own voice. This is the one field where the villainous framing is allowed, because sometimes the joke is what makes the idea stick. |

## Relations (`links`)

Edges read as "this card *relation* target".

| Relation | Meaning | Typical use |
|---|---|---|
| `requires` | You need the target to understand this card. | concept → concept |
| `specializes` | This card is a special case or variant of the target. | Homeostasis → Balancing loop |
| `part-of` | This card is a component of the target. | Reference point → Balancing loop |
| `contrasts-with` | Easily confused with the target; the card body says how to tell them apart. | Stock ↔ Flow |
| `uses` | A procedure or case applies the target concept, procedure or tool. | Build a CLD → Polarity tracing |
| `produces` | A structure that generates the target behavior. | Delay → Oscillation |
| `diagnoses` | A procedure or heuristic that detects the target. | Live-build → archetypes |
| `counters` | A practice that defends against the target failure or bias. | Pre-registered disconfirming result → Confirmation bias |
| `instance-of` | A case is an instance of the target archetype or concept. | case → archetype |
| `related` | Worth reading together; no stronger relation applies. | anything |

`contrasts-with` is symmetric; the build adds the reverse edge, so only one side needs to state it.

## Type-specific fields

### `procedure`

| Field | Required | Meaning |
|---|---|---|
| `inputs` | yes | What you need before starting. |
| `outputs` | yes | What you have when done. |

Body sections, in this order: `## When to use`, `## Steps` (numbered), `## Checks` (how to tell it was done right), `## Common mistakes`. A `## Worked example` section is optional.

### `archetype`

| Field | Required | Meaning |
|---|---|---|
| `diagnostic_question` | yes | The one question that tests for the archetype (from Appendix C). |
| `structure` | yes | The causal loop structure, machine-checkable (below). |

`structure` holds `variables` (a list of names), `links` (each with `from`, `to`, `polarity` of `+` or `-`, optional `delay: information` or `delay: material`, and optional `exogenous: true` for a link that feeds a loop from outside it, such as a goal), and `loops` (each with `id`, `type` of `R` or `B`, `path`, the list of variables in order around the loop, and optional `label`). The build checks that every consecutive pair in each `path`, including last back to first, is a declared link, and that the count of `-` links around the loop matches the declared type: even is `R`, odd is `B`. This is the book's own trace-and-count rule (Chapter 6), applied to the bundle so that an archetype whose structure doesn't close fails the build.

Any other card (a case or a concept) may also carry an optional `structure` block in the same format, and the build checks it the same way. Cases that draw a specific causal loop diagram should include one.

Body sections: `## Signature`, `## Symptoms`, `## Interventions`, `## Misapplications`, `## Distinguish from`.

### `heuristic`

| Field | Required | Meaning |
|---|---|---|
| `when` | yes | The observable situation that triggers it. |
| `then` | yes | What to consider or do. |

The body explains why the heuristic holds and where it stops holding.

### `case`

| Field | Required | Meaning |
|---|---|---|
| `source_example` | yes | The book's name for the example, so a reader of the book can find it. |

The body restates the example in neutral terms: the structure and the reasoning, without the costume. Body sections: `## Situation`, `## Analysis`, `## Lesson`.

### `tool`

Software, notations and standards. Required: `license` (free, open-source, commercial, or a short mix). The body says what it's for and what it doesn't do.

## Evals

`systems-thinking/evals/*.yaml` holds the eval set, a list of items:

```yaml
- id: arch-001
  kind: recognize        # recognize | apply | discriminate | critique | procedure
  prompt: >
    The scenario or question, in neutral terms.
  expected:              # points a good answer makes; a grader checks each one
    - ...
  pitfalls:              # answers that sound right but miss the method
    - ...
  uses: [fixes-that-fail, delay]   # cards an answer should draw on
```

The build checks that every ID in `uses` exists.

## Style

The bundle follows the book's house rules where they apply: no hard-wrapped paragraphs, gender-neutral language, plain-language acronym definitions on first use in each card, and real citations only. The villainous framing is removed everywhere except `mnemonic`, `source_example` and fenced code blocks (code has to match the book's real model and scripts, whose variable names keep the costume). The build lints for the series' recurring names (henchman, villainium, Secret Lab, and so on) everywhere else.

`code/` is a copy of the book's published code. Set `BUNDLE_CODE_SOURCE` to a folder holding that code and the build warns if the two drift apart.
