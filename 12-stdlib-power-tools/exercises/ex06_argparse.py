# Scenario: a tiny `notes` command-line tool — add a note with tags, or
# list the most recent ones. Concepts: argparse parser -> add_argument
# -> parse_args(argv); a testable CLI takes argv as a parameter instead
# of reading sys.argv itself.
# Run: uv run pytest 12-stdlib-power-tools -k ex06

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Build the parser for the `notes` CLI:
    - positional `action`: "add" or "list"
    - positional `text` (optional; the note body, used by "add")
    - `--tag`: repeatable, collected into a list (default: none given)
    - `--limit`: int, default 10 (max notes to show, used by "list")

    build_parser().parse_args(["add", "milk", "--tag", "shop"])
        -> Namespace(action="add", text="milk", tag=["shop"], limit=10)
    """
    raise NotImplementedError


def run(argv: list[str], notes: list[dict[str, object]] | None = None) -> str:
    """Parse `argv` with build_parser() and dispatch:
    - "add": append {"text": text, "tags": tags} to `notes` (a list the
      caller owns so calls can be chained; defaults to a fresh list
      when omitted) and return "Added: {text}".
    - "list": return up to `limit` notes, one per line, as
      "{text} [{tag1,tag2}]" (empty brackets if no tags), or
      "No notes." if `notes` is empty.

    notes = []
    run(["add", "milk", "--tag", "shop"], notes) -> "Added: milk"
    run(["list"], notes) -> "milk [shop]"

    Also: build_parser().parse_args(["--help"]) must exit cleanly via
    SystemExit (argparse's built-in behavior) — don't catch it here.
    """
    raise NotImplementedError
