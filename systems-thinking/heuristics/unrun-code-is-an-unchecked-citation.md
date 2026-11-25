---
id: unrun-code-is-an-unchecked-citation
type: heuristic
title: Unrun code is a citation nobody looked up
summary: Plausible-looking output (a citation, a code example, printed results) that was generated rather than verified looks exactly like the real thing, and only running or looking it up catches it.
chapters: [24, 18, 17]
when: Text includes references, code, or numeric results that an AI agent (or anyone) produced without running or retrieving them.
then: Look up every citation at its source and run every code example against a real model or file before publishing or acting on it.
links:
  related: [every-check-has-a-boundary-and-a-kind, verify-after-translation]
series: [model-validation, ai-delegation]
---

In the making of the book, an Appendix E citation to an Ackoff essay that doesn't exist (its title apparently blended Ackoff with C. West Churchman's *The Systems Approach and Its Enemies*) sat beside accurate ones for seven weeks. Its printed SALib results came from no model, and a PySD example loaded a file nobody had made. Each looked right until it was looked up or run.
