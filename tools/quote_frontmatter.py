#!/usr/bin/env python3
"""Quote scalar frontmatter values that contain ": " so YAML parses them.

Usage: python3 quote_frontmatter.py BUNDLE_DIR   (rewrites cards in place)
"""
import re, sys, pathlib
root = pathlib.Path(sys.argv[1])
keys = ("summary", "when", "then", "title", "diagnostic_question", "source_example", "mnemonic", "attribution")
for p in root.rglob("*.md"):
    text = p.read_text()
    if not text.startswith("---\n"):
        continue
    end = text.index("\n---\n", 4)
    fm, rest = text[4:end], text[end:]
    out = []
    changed = False
    for line in fm.split("\n"):
        m = re.match(r"^(%s): (.*)$" % "|".join(keys), line)
        if m and ": " in m.group(2) and not m.group(2)[:1] in "\"'":
            v = m.group(2).replace("\\", "\\\\").replace('"', '\\"')
            line = f'{m.group(1)}: "{v}"'
            changed = True
        out.append(line)
    if changed:
        p.write_text("---\n" + "\n".join(out) + rest)
        print("quoted", p.relative_to(root))
