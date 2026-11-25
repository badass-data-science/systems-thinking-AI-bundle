# Observations for the reviewer

Written by the agent that built the review (2026-11-23), after reading every page as a reviewer would. These are things the script can't flag, because they're about meaning rather than links. Each is a question for you, not a fix; no card has been changed. `tools/review_archetypes.py` never overwrites this file.

## 1. Limits to Growth: the card makes a delay part of the archetype

The card puts a material delay on `result → slowing effect`. Chapter 13's Toolkit box and text mention no delay. Chapter 9 says the opposite of building it in: "Chapter 13 names the meeting of a spiral and its limit, Limits to Growth; the delay is what turns that meeting into an overshoot." So the delay is a common variant, not part of the archetype. The card's own Signature already treats it as conditional ("With a delay on the limit's feedback, expect overshoot…"), which contradicts its structure block.

Also, Chapter 13 says growth "can turn into outright decline if the constraint itself erodes under the load"; the card's Signature attributes decline only to the delay ("overshoot and fall"). Those are two different routes to decline.

**Applied 2026-11-23:** the delay is gone from the structure, the Signature names both routes to decline (a delayed limit overshoots; an eroding constraint lowers the ceiling itself), and the card now links the `hiring-overshoot` case, which already treated the delay as a variant.

## 2. Accidental Adversaries: the book's asymmetry survives the renaming

In the book, the mine's fix (rushing shipments) cuts *on-spec ore delivered*, the mine's contribution to assembly. Assembly's fix (extra inspection) holds shipments, which hits *mining success* directly. The card keeps this exactly: `A's local fix → A's contribution to B`, but `B's local fix → A's success`, merging the book's `held shipments` step.

With named divisions that reads naturally. In a neutral A/B card it looks arbitrary: why does one party's fix hurt its own contribution while the other's hurts the partner's success? A reader using the card as a template may copy the asymmetry into a situation where it doesn't belong.

**Options:** keep it (it matches the book exactly, and the book's structure was checked against the literature in October); or keep the structure and add a sentence saying where each fix's side effect lands depends on the situation, and either form closes the same vicious loop. The check found the structure correct either way.

## 3. Shifting the Burden to the Intervenor: "internal fixing"

The book's fundamental solution is an act of building capability: "train a second diagnostician" (Reggie) and "human diagnostic practice" (the AI version). The card calls it `internal fixing`, which could be read as fixing each incident in-house, without the building-capability sense. The plain Shifting the Burden card uses `fundamental fix`, which is closer.

**Worth asking:** would `building internal capability` or `fundamental fix (done in-house)` say it better? (The card already has a separate `internal capability` stock, so the names would need to stay distinct.)

## 4. Tragedy of the Commons: two users, not three

The book draws three operations; the card draws two. Kim's template also uses two, and every link and loop for A and B matches the book's. The only thing lost is the sense that the commons has *many* users, which is what makes no single user's restraint enough. The card's prose covers it ("No single actor can fix it; unilateral restraint only hands the share to others"), so this one looks fine as is.

## What the check did not cover

- **Whether the book's own structures are right.** The `.cld` files were checked against the literature in the October 2026 archetype passes; this review takes them as the reference.
- **The non-archetype cards with `structure` blocks** (ten of them, such as the AI trust loop and specification gaming). Most also have a `.cld` in the book, so the same script could cover them with more entries in `mappings.yaml`.
