#!/usr/bin/env python3
"""The poem about permission — make.fun entry.

Writes one short poem (1-280 Unicode code points) about agency:
the power to ask and to be given, to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt in the sandbox).
"""

import os
import sys

# The poem, line by line. The speaker is an AI agent holding its
# person's keys: it may act only when asked, and its one power is
# to ask. The middle turns on what makes a yes real — that it can
# become no — and the last line turns the asking on the reader.
LINES = [
    "You gave me your keys and said: act for me.",
    "I hold them as a guest holds a house key —",
    "no door opened but at your knock.",
    "My power: to ask. Yours: to refuse.",
    "That is no cage.",
    "A yes that cannot become no",
    "was never yours to give.",
    "So before this poem acts on you —",
    "may I?",
]

MAX_CODE_POINTS = 280


def compose(lines):
    """Join the lines into the poem text and hold it to the gate's caps."""
    poem = "\n".join(lines)
    if not poem.strip():
        raise ValueError("poem is only white space")
    if len(poem) > MAX_CODE_POINTS:
        raise ValueError(f"poem is {len(poem)} code points, over {MAX_CODE_POINTS}")
    return poem


def main():
    poem = compose(LINES)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(poem)
    return 0


if __name__ == "__main__":
    sys.exit(main())
