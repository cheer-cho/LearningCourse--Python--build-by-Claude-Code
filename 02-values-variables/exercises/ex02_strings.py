"""ex02 — Strings: quoting, escapes, and common methods.

Scenario: cleaning up and reformatting short pieces of text. Covers
`upper`, `lower`, `strip`, `split`, `join`, `replace`, `len()`.

Check: uv run python scripts/test.py 2 -k ex02
"""

from __future__ import annotations


def shout(s: str) -> str:
    """Turn a sentence into a shout: all caps, with "!" on the end.

    shout("watch out") -> "WATCH OUT!"
    shout("hello") -> "HELLO!"
    """
    return f"{s.upper()}!"


def initials(full_name: str) -> str:
    """Turn a "first last" name into initials like "A.L.".

    full_name always has exactly two words separated by one space.
    Split it into the two words, take the first letter of each,
    uppercase them, and join with ".".

    initials("ada lovelace") -> "A.L."
    initials("grace hopper") -> "G.H."
    """
    # 1. split the full_name
    # 2. using first char of them
    names = full_name.upper().split()

    """
    loop version

    first_char_of_names = []
    for name in names:
        first_char_of_names.append(name[0])
    """

    first_char_of_names = [name[0] for name in names]
    return ".".join(first_char_of_names) + "."


def clean_username(raw: str) -> str:
    """Normalize a raw name into a username.

    Strip leading/trailing whitespace, lowercase it, and replace every
    space with an underscore.

    clean_username("  John Doe ") -> "john_doe"
    clean_username("ADA") -> "ada"
    """
    return raw.strip().lower().replace(" ", "_")
