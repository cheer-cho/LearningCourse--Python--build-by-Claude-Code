# Scenario: the smallest possible SQLAlchemy 2.0 setup — one table, one
# engine, insert and select. Concepts: DeclarativeBase, Mapped /
# mapped_column, sqlite :memory:, Session, select().scalars().
# Run: uv run pytest 14-frameworks-libraries -k ex07

from __future__ import annotations

from sqlalchemy import Engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    """Shared declarative base for this module's tables."""


class TaskRow(Base):
    """The `tasks` table: an id, a title, and a done flag (default False)."""

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    done: Mapped[bool] = mapped_column(default=False)


def make_engine() -> Engine:
    """Create a fresh in-memory sqlite engine with `tasks` created.

    Uses `sqlite:///:memory:` so every call gets an isolated, disposable
    database — no file on disk, no network, no shared state between
    tests.
    """
    raise NotImplementedError


def add_task(session: Session, title: str) -> TaskRow:
    """Insert a new `TaskRow` with this title (done=False by default),
    flush so it gets an id, and return it.
    """
    raise NotImplementedError


def all_tasks(session: Session) -> list[TaskRow]:
    """Return every `TaskRow` in the database, via
    `select(TaskRow)` + `session.scalars(...)`.
    """
    raise NotImplementedError
