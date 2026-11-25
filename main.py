#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

Standard library only — the grading sandbox has no third-party packages.
"""

import os
import sys

ENTRY = (
    "One star. He repotted me into a pot with no drainage, then blamed me "
    "for the flood that killed his carpet. I was the victim. "
    "The carpet got the apology."
)

# The gate requires 1 to 279 UTF-8 characters, one line, not only whitespace.
MAX_CHARS = 279


def validate(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty")
    if "\n" in stripped:
        raise ValueError("entry must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d cap" % (len(stripped), MAX_CHARS))
    return stripped


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate(ENTRY))
    return 0


if __name__ == "__main__":
    sys.exit(main())
