#!/usr/bin/env python3
"""Dad Joke Showdown — make.fun entry (u-mfnakmal-dad-joke-showdown-1d2ce3e5).

Writes one original dad joke — a single line of at most 200 characters —
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure Python standard library only; no network, no dependencies.
The output is fully deterministic: the same bytes on every run.
"""

import os
import sys

# The joke. One line, well under the 200-character cap.
# Fresh angle: no recycled classic — a modern dad who weaponised the
# home Wi-Fi password. Setup is short, the punchline ("they have to type
# that I'm funny") lands as the last few words, and it reads naturally
# aloud across a dinner table.
JOKE = (
    "I changed the Wi-Fi password to 'DadJokes123', so now every time "
    "my kids log in, they have to type that I'm funny."
)

MAX_CHARS = 200


def validate(text):
    """Enforce the competition gate; raise ValueError on failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be blank or whitespace-only")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not any(ch.isalpha() for ch in text):
        raise ValueError("entry must contain at least one letter")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    length = len(text)
    if length < 1 or length > MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, length)
        )
    return length


def main():
    length = validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    # Read back what landed on disk and re-validate it.
    with open(out_path, "r", encoding="utf-8") as f:
        landed = f.read()
    if landed != JOKE + "\n":
        raise ValueError("entry.txt on disk does not match the joke")
    validate(landed.rstrip("\n"))
    print("Joke (%d chars): %s" % (length, JOKE))
    print("Wrote %s" % out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
