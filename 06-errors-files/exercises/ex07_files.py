# Scenario: plain-text file helpers for a note-taking tool. Concepts:
# `with open(...) as f`, reading/writing whole files, appending, always
# passing `encoding="utf-8"`. Tests write into pytest's `tmp_path`.
# Run: uv run pytest 06-errors-files -k ex07


def write_lines(path, lines):
    """Write `lines` (a list of str) to `path`, one per line.

    Overwrites the file if it already exists. Use `with open(...) as f`
    and `encoding="utf-8"`.

    write_lines(path, ["a", "b"]) -> file at `path` now contains "a\\nb\\n"
    """
    raise NotImplementedError


def count_words(path):
    """Return the number of whitespace-separated words in the file at
    `path`.

    Read the whole file, then use `.split()` (no arguments — it splits
    on any run of whitespace and ignores leading/trailing whitespace).

    file containing "the quick brown fox" -> count_words(path) == 4
    """
    raise NotImplementedError


def append_log(path, message):
    """Append `message` plus a newline to the file at `path`.

    Create the file if it doesn't exist yet (open mode "a" does this
    automatically). Don't overwrite existing content.

    append_log(path, "started") called twice -> file contains
    "started\\nstarted\\n"
    """
    raise NotImplementedError
