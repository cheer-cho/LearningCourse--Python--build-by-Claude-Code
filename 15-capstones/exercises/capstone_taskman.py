# Capstone A: build a task-manager CLI over SQLite. Concepts: SQLAlchemy
# 2.0 typed ORM, a service layer decoupled from the CLI, Typer commands,
# full type hints checked with `mypy --strict`. Brief: LESSON.md.
# Run: uv run pytest 15-capstones -k capstone_taskman

from __future__ import annotations

from pathlib import Path

import typer
from sqlalchemy import Engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    """Declarative base shared by every mapped row in this capstone."""


class TaskRow(Base):
    """One row in the ``tasks`` table.

    Columns: ``id`` (primary key), ``title``, ``priority`` (free-text,
    default ``"normal"``), ``done`` (default ``False``).
    """

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    priority: Mapped[str] = mapped_column(String(20), default="normal")
    done: Mapped[bool] = mapped_column(default=False)

    def __repr__(self) -> str:
        return (
            f"TaskRow(id={self.id!r}, title={self.title!r}, "
            f"priority={self.priority!r}, done={self.done!r})"
        )


class TaskNotFound(Exception):
    """Raised by the service layer when a task id doesn't exist."""


def make_engine(url: str) -> Engine:
    """Create a SQLAlchemy engine for `url` and ensure the schema exists.

    make_engine("sqlite:///:memory:") -> Engine with the ``tasks`` table
    already created.
    """
    raise NotImplementedError


def add_task(session: Session, title: str, *, priority: str = "normal") -> TaskRow:
    """Insert a new task and flush so its ``id`` is assigned.

    Does not commit — the caller controls the transaction boundary.

    add_task(session, "Buy milk", priority="high") -> TaskRow(title="Buy milk", ...)
    """
    raise NotImplementedError


def complete_task(session: Session, task_id: int) -> TaskRow:
    """Mark the task with `task_id` as done and return it.

    Raises TaskNotFound if no task with that id exists.
    """
    raise NotImplementedError


def list_tasks(
    session: Session, *, include_done: bool = False, sort: str = "id"
) -> list[TaskRow]:
    """Return tasks ordered by `sort` (one of "id", "priority", "title").

    By default only pending (not-done) tasks are returned; pass
    `include_done=True` to include completed ones. Unknown `sort` values
    fall back to ordering by id.
    """
    raise NotImplementedError


app = typer.Typer(help="A tiny task manager backed by SQLite.")


@app.callback()
def main(
    ctx: typer.Context,
    db: Path = typer.Option(Path("tasks.db"), "--db", help="SQLite database file."),  # noqa: B008
) -> None:
    """Open (creating if needed) the task database at `db` for this run."""
    raise NotImplementedError


@app.command()
def add(
    ctx: typer.Context,
    title: str,
    priority: str = typer.Option("normal", "--priority", help="e.g. low/normal/high"),
) -> None:
    """Add a new task titled `title` with the given `priority`."""
    raise NotImplementedError


@app.command("done")
def done_cmd(ctx: typer.Context, task_id: int) -> None:
    """Mark the task with id `task_id` as complete."""
    raise NotImplementedError


@app.command("list")
def list_cmd(
    ctx: typer.Context,
    all_: bool = typer.Option(False, "--all", help="Include completed tasks."),
    sort: str = typer.Option("id", "--sort", help="Sort by id/priority/title."),
) -> None:
    """Print pending tasks (or all, with --all) as a simple text table."""
    raise NotImplementedError


@app.command()
def stats(ctx: typer.Context) -> None:
    """Print task counts grouped by priority."""
    raise NotImplementedError


if __name__ == "__main__":
    app()
