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
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(f"{line}\n" for line in lines)


def count_words(path):
    """Return the number of whitespace-separated words in the file at
    `path`.

    Read the whole file, then use `.split()` (no arguments — it splits
    on any run of whitespace and ignores leading/trailing whitespace).

    file containing "the quick brown fox" -> count_words(path) == 4
    """
    # with open(path, encoding="utf-8") as f:
    #     text = f.read()

    # return len(text.split())

    # total = 0
    # with open(path, encoding="utf-8") as f:
    #     for line in f:
    #         total += len(line.split())

    # return total
    with open(path, encoding="utf-8") as f:
        return sum(len(line.split()) for line in f)


def append_log(path, message):
    """Append `message` plus a newline to the file at `path`.

    Create the file if it doesn't exist yet (open mode "a" does this
    automatically). Don't overwrite existing content.

    append_log(path, "started") called twice -> file contains
    "started\\nstarted\\n"
    """
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"{message}\n")
