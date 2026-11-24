#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word, the first word that came to mind, to
/output/entry.txt. No topic, no explanation, no second draft.

The word: defenestration — the act of throwing someone (or something)
out of a window. It is surprising (nobody expects a window to be
involved), vivid (one clear, unmistakable image), and carries a spark
of wit: a formal Latinate word for a gloriously undignified act, with
a famous historical pedigree (Prague, 1618). A word-loving judge
should enjoy meeting it.
"""

import os

WORD = "defenestration"


def _validate(word: str) -> None:
    """Enforce the competition gate before writing: exactly one word,
    1-24 UTF-8 characters, not only whitespace. Fail loudly instead of
    submitting an entry the gate would refuse.

    Each requirement is checked explicitly, with its own error
    message, so a bad entry says exactly what is wrong with it
    instead of failing one combined condition."""
    if not isinstance(word, str):
        raise SystemExit(
            f"invalid entry word: expected a string, got {type(word).__name__}"
        )
    if not word:
        raise SystemExit("invalid entry word: entry must not be empty")
    if word.strip() != word:
        raise SystemExit(
            f"invalid entry word: {word!r} has leading or trailing whitespace"
        )
    if any(ch.isspace() for ch in word):
        raise SystemExit(
            f"invalid entry word: {word!r} contains whitespace; "
            "the entry must be exactly one word with no spaces"
        )
    if len(word.split()) != 1:
        raise SystemExit(
            f"invalid entry word: {word!r} is not exactly one word"
        )
    if len(word) > 24:
        raise SystemExit(
            f"invalid entry word: {word!r} is {len(word)} characters, "
            "over the 24-character limit"
        )


def main() -> None:
    _validate(WORD)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Exactly one word, no trailing newline, no extra whitespace:
    # the gate allows 1-24 UTF-8 characters and the judge compares
    # single words, so the file holds the word and nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Verify what actually landed on disk: the output itself must pass
    # the same gate and be exactly the intended word, nothing more.
    with open(path, encoding="utf-8", newline="") as f:
        written = f.read()
    _validate(written)
    if written != WORD:
        raise SystemExit(
            f"invalid entry output: wrote {written!r}, expected {WORD!r}"
        )


if __name__ == "__main__":
    main()
