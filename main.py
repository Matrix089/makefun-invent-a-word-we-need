#!/usr/bin/env python3
"""Write one invented word and its definition for make.fun's
Invent a Word We Need bounty.

Why this entry fits the judge's brief: "doorwaynesia" names a real
gap -- the well-documented doorway effect, where walking through a
doorway makes you forget why you went into the room -- and English
has no everyday one-word name for it. The definition lands in one
reading, the word is doorway + amnesia, so it is sayable, spellable
and memorable, and it sounds like English could have grown it.
"""

import os

LINE = (
    "Doorwaynesia \u2014 walking through a doorway and forgetting "
    "why you went there."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-140 characters, a single line.
    # The line was counted at exactly 75 characters; pin that
    # so any accidental wording change fails loudly instead of silently
    # shipping a different (or over-long) entry.
    assert len(line) == 75, f"line is {len(line)} characters, expected 75"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 140, f"line is {len(line)} characters"
    assert line.strip() == line, "line must not have surrounding whitespace"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 75, "entry.txt is not 75 characters"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
