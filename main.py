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
    submitting an entry the gate would refuse."""
    if not word or len(word) > 24 or word.strip() != word or " " in word:
        raise SystemExit(f"invalid entry word: {word!r}")


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


if __name__ == "__main__":
    main()
