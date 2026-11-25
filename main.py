#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original office-life joke.

The program writes a single one-line joke about office life to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set, for local tests).
Python 3.13 standard library only, no network.
"""

import os
from pathlib import Path

# One fresh, original office-life one-liner. The observation is true
# (the office printer almost never works); the turn is the last beat —
# a working printer treated like a newborn, photographed for the
# company newsletter.
JOKE = (
    "The office printer worked today, so we all gathered around it "
    "like a newborn and took a photo for the company newsletter."
)


def main() -> None:
    # Guard the gate before writing: one line, 1-200 chars including
    # the trailing newline the file carries.
    assert "\n" not in JOKE and 1 <= len(JOKE) + 1 <= 200
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
