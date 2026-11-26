#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist.

Writes a single one-line deadpan lightning forecast for the invented
city of Copperleaf to the output directory.

Usage:
    python3 main.py

The entry is written to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when that
environment variable is set, otherwise to ``/output/entry.txt``.
The output is exactly one line, 1-160 characters, with no trailing
newline.
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "In Copperleaf, lightning strikes at 4:17 pm, twelve bolts, "
    "as scheduled. The council reminds residents to wave politely "
    "and file any singed umbrellas by Friday."
)

MAX_CHARS = 160


def validate(entry: str) -> None:
    """Check the entry meets the competition gate."""
    if not entry or not entry.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be exactly one line")
    entry.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def main() -> int:
    validate(ENTRY)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8", newline="")
    written = out_path.read_bytes()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("written entry.txt does not round-trip byte-identical")
    print(f"Wrote {len(ENTRY)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
