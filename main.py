#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line - Round 2 entry.

Writes the keeper line to /output/entry.txt with no trailing newline.
Pure stdlib only: the grader runs python:3.13-slim with no site-packages.

Keeper (79 chars): the agent kept a ledger of every time it stayed,
and the one stay it withheld was today.
"""

from pathlib import Path

ENTRY = "You asked me 3,847 times to stay. I stayed 3,846 times. The last ask was today."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is only whitespace"
    # Gate: one line only - the judge compares single lines; an embedded
    # newline would fail criterion 1 (breakup message in one line).
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    data = text.encode("utf-8")
    out.write_bytes(data)
    # Byte-verify what was written: exact bytes, valid UTF-8, no newline.
    read_back = out.read_bytes()
    assert read_back == data, "entry.txt does not match the keeper"
    assert read_back.decode("utf-8") == text
    assert not read_back.endswith(b"\n"), "entry must have no trailing newline"
    print(f"wrote {len(data)} bytes to {out} ({len(text)} chars, no trailing newline)")


if __name__ == "__main__":
    main()
