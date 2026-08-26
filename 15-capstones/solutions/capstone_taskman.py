# Capstone A: a task-manager CLI over SQLite. Concepts: SQLAlchemy 2.0
# typed ORM, a service layer decoupled from the CLI, Typer commands, and
# full type hints checked with `mypy --strict`.
# Run: uv run pytest 15-capstones -k capstone_taskman

from __future__ import annotations

from pathlib import Path

import typer
from sqlalchemy import Engine, String, create_engine, func, select
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
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    return engine


def add_task(session: Session, title: str, *, priority: str = "normal") -> TaskRow:
    """Insert a new task and flush so its ``id`` is assigned.

    Does not commit — the caller controls the transaction boundary.

    add_task(session, "Buy milk", priority="high") -> TaskRow(title="Buy milk", ...)
    """
    task = TaskRow(title=title, priority=priority, done=False)
    session.add(task)
    session.flush()
    return task


def complete_task(session: Session, task_id: int) -> TaskRow:
    """Mark the task with `task_id` as done and return it.

    Raises TaskNotFound if no task with that id exists.
    """
    task = session.get(TaskRow, task_id)
    if task is None:
        raise TaskNotFound(f"no task with id {task_id}")
    task.done = True
    session.flush()
    return task


def list_tasks(
    session: Session, *, include_done: bool = False, sort: str = "id"
) -> list[TaskRow]:
    """Return tasks ordered by `sort` (one of "id", "priority", "title").

    By default only pending (not-done) tasks are returned; pass
    `include_done=True` to include completed ones. Unknown `sort` values
    fall back to ordering by id.
    """
    order_columns = {
        "id": TaskRow.id,
        "priority": TaskRow.priority,
        "title": TaskRow.title,
    }
    stmt = select(TaskRow)
    if not include_done:
        stmt = stmt.where(TaskRow.done.is_(False))
    stmt = stmt.order_by(order_columns.get(sort, TaskRow.id))
    return list(session.scalars(stmt).all())


app = typer.Typer(help="A tiny task manager backed by SQLite.")


@app.callback()
def main(
    ctx: typer.Context,
    db: Path = typer.Option(Path("tasks.db"), "--db", help="SQLite database file."),  # noqa: B008
) -> None:
    """Open (creating if needed) the task database at `db` for this run."""
    ctx.obj = make_engine(f"sqlite:///{db}")


@app.command()
def add(
    ctx: typer.Context,
    title: str,
    priority: str = typer.Option("normal", "--priority", help="e.g. low/normal/high"),
) -> None:
    """Add a new task titled `title` with the given `priority`."""
    engine: Engine = ctx.obj
    with Session(engine) as session:
        task = add_task(session, title, priority=priority)
        session.commit()
        typer.echo(f"Added task #{task.id}: {task.title} [{task.priority}]")


@app.command("done")
def done_cmd(ctx: typer.Context, task_id: int) -> None:
    """Mark the task with id `task_id` as complete."""
    engine: Engine = ctx.obj
    with Session(engine) as session:
        try:
            complete_task(session, task_id)
            session.commit()
        except TaskNotFound:
            typer.echo(f"No task with id {task_id}", err=True)
            raise typer.Exit(code=1) from None
        typer.echo(f"Completed task #{task_id}")


@app.command("list")
def list_cmd(
    ctx: typer.Context,
    all_: bool = typer.Option(False, "--all", help="Include completed tasks."),
    sort: str = typer.Option("id", "--sort", help="Sort by id/priority/title."),
) -> None:
    """Print pending tasks (or all, with --all) as a simple text table."""
    engine: Engine = ctx.obj
    with Session(engine) as session:
        tasks = list_tasks(session, include_done=all_, sort=sort)
        if not tasks:
            typer.echo("No tasks.")
            return
        for task in tasks:
            mark = "x" if task.done else " "
            typer.echo(f"[{task.id}] ({mark}) {task.priority:<6} {task.title}")


@app.command()
def stats(ctx: typer.Context) -> None:
    """Print task counts grouped by priority."""
    engine: Engine = ctx.obj
    with Session(engine) as session:
        stmt = select(TaskRow.priority, func.count()).group_by(TaskRow.priority)
        for priority, count in session.execute(stmt).all():
            typer.echo(f"{priority}: {count}")


if __name__ == "__main__":
    app()
