#!/usr/bin/env python3
"""Negative tests for build_bundle.py: plant known bugs in a copy of the bundle
and check the validator reports each one. Run with:

    python3 test_build_bundle.py

Exits 1 if the clean bundle fails or any planted bug goes unreported.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent / "systems-thinking"
BUILD = HERE / "build_bundle.py"

# (file, old text, new text, error text the build must print)
PLANTED = [
    ("archetypes/escalation.md",
     "{id: R1, type: R, label: escalation",
     "{id: R1, type: B, label: escalation",
     "loop R1 declared B but has 4 minus links, so it is R"),
    ("cases/overtime-and-burnout.md",
     '    - {from: burnout, to: mistakes, polarity: "+", delay: material}\n',
     "",
     "loop R1 needs link burnout -> mistakes, not declared"),
    ("archetypes/limits-to-growth.md",
     "## Signature\n",
     "## Signature\n\nThe henchmen do this.\n",
     "costume word 'henchmen'"),
    ("archetypes/shifting-the-burden.md",
     "related: [fixes-that-fail]",
     "related: [fixes-that-fial]",
     "unknown card `fixes-that-fial`"),
    ("procedures/catwoe.md",
     "## Common mistakes",
     "## Mistakes",
     "missing body section `## Common mistakes`"),
]


def run(bundle: Path) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(BUILD), str(bundle)], capture_output=True, text=True)


def main() -> int:
    failures = 0
    with tempfile.TemporaryDirectory() as tmp:
        clean = Path(tmp) / "clean"
        shutil.copytree(BUNDLE, clean)
        result = run(clean)
        if result.returncode != 0:
            print("FAIL clean bundle does not build:\n" + result.stdout)
            return 1
        print("ok   clean bundle builds")

        broken = Path(tmp) / "broken"
        shutil.copytree(BUNDLE, broken)
        for rel, old, new, _ in PLANTED:
            path = broken / rel
            text = path.read_text(encoding="utf-8")
            if old not in text:
                print(f"FAIL test setup: {old!r} not found in {rel}")
                failures += 1
                continue
            path.write_text(text.replace(old, new, 1), encoding="utf-8")
        result = run(broken)
        if result.returncode == 0:
            print("FAIL broken bundle built without errors")
            failures += 1
        for rel, _, _, expected in PLANTED:
            if expected in result.stdout:
                print(f"ok   caught in {rel}: {expected}")
            else:
                print(f"FAIL not caught in {rel}: {expected}")
                failures += 1
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
