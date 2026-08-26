# Scenario: a `todo` command-line app backed by an in-memory list
# standing in for a save file. Concepts: typer.Typer, arguments vs
# options, CliRunner testing exit codes and output.
# Run: uv run pytest 14-frameworks-libraries -k ex06

from __future__ import annotations

import typer

app = typer.Typer()

_TODOS: list[dict[str, object]] = []


def reset_todos() -> None:
    """Test-only helper: clear all todos back to an empty list."""
    _TODOS.clear()


@app.command()
def add(text: str, priority: int = typer.Option(1, "--priority")) -> None:
    """Add a todo.

    `text` is a positional ARGUMENT (what to do); `--priority` is an
    OPTION (defaults to 1). Prints "Added: <text>" on success.

    $ todo add "Buy milk" --priority 2
    Added: Buy milk
    """
    raise NotImplementedError


@app.command(name="list")
def list_todos(
    show_all: bool = typer.Option(False, "--all"),
    show_done: bool = typer.Option(False, "--done"),
) -> None:
    """List todos, one per line as "[ ] text" (pending) or "[x] text"
    (done).

    Default (no flags): only pending todos. `--done`: only done todos.
    `--all`: every todo regardless of status. `--all` and `--done`
    together behave like `--all` (nothing to narrow down).
    """
    raise NotImplementedError
