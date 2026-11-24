#!/usr/bin/env python3
"""make.fun entry: Everyday Things, Two Lines, Longer Run.

Writes two lines to $MAKEFUN_OUTPUT_DIR/entry.txt.
Line 1 explains an escalator to a 10-year-old in one vivid sentence
built on a single analogy; line 2 says in one sentence what that
analogy maps and what it leaves out.
Pure Python standard library only; no third-party imports.
"""

import os

ENTRY = (
    "An escalator is a staircase that got tired of waiting for you, "
    "so it climbs itself and carries you along for the ride.\n"
    "It maps the way the moving steps do the climbing for you, but it "
    "leaves out that real stairs never move on their own, and that you "
    "can still walk up an escalator if you are in a hurry.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
