# Scenario: TDD from the consumer seat. `slugify` ships with real bugs.
# The tests in `test_ex07_tdd_bugfix.py` ARE the spec — they're all red
# right now. Make them green by fixing `slugify` below; there are no
# other hints. Concepts: TDD's red -> green loop, reading failures as
# a spec, fixing behavior without a docstring rewrite.
# Run: uv run pytest 13-testing-quality -k ex07

import re


def slugify(title: str) -> str:
    """Convert `title` into a URL-safe slug: lowercase, words joined by
    single hyphens, punctuation stripped, accented letters replaced by
    their closest ASCII equivalent, no leading/trailing hyphens.

    This implementation has 3 real bugs. `test_ex07_tdd_bugfix.py` is
    the spec: run it, read each failure, fix the bug it describes.

    slugify("Hello, World!") -> "hello-world"
    slugify("Already--Slugged   Here") -> "already-slugged-here"
    slugify("Café München") -> "cafe-munchen"
    """
    text = title.strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text
