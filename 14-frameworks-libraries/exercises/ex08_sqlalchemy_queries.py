# Scenario: a slightly bigger schema — tasks now belong to a project
# (one-to-many) — with everyday query/update operations. Concepts:
# relationship(), foreign keys, session.get, targeted select() filters,
# aggregate select(func.count()).
# Run: uv run pytest 14-frameworks-libraries -k ex08

from __future__ import annotations

from sqlalchemy import Engine, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship


class Base(DeclarativeBase):
    """Shared declarative base for this module's tables."""


class Project(Base):
    """The `projects` table. Each project owns many tasks."""

    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    tasks: Mapped[list[TaskRow]] = relationship(back_populates="project")


class TaskRow(Base):
    """The `tasks` table. `project_id` is nullable — a task may be
    unassigned.
    """

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    done: Mapped[bool] = mapped_column(default=False)
    project_id: Mapped[int | None] = mapped_column(ForeignKey("projects.id"), default=None)
    project: Mapped[Project | None] = relationship(back_populates="tasks")


def make_engine() -> Engine:
    """Create a fresh in-memory sqlite engine with `projects` and `tasks`
    created.
    """
    raise NotImplementedError


def open_tasks(session: Session) -> list[TaskRow]:
    """Return every `TaskRow` where `done` is False."""
    raise NotImplementedError


def rename_task(session: Session, task_id: int, title: str) -> TaskRow:
    """Fetch the task with this id (`session.get`), set its `title`,
    flush, and return it. Assumes the task exists.
    """
    raise NotImplementedError


def complete_and_count(session: Session, task_id: int) -> int:
    """Mark the task with this id as done, then return the total number
    of done tasks across the whole `tasks` table (use
    `select(func.count())`, not `len(...)`).
    """
    raise NotImplementedError


def tasks_of(session: Session, project_name: str) -> list[TaskRow]:
    """Return every `TaskRow` belonging to the project named
    `project_name` (empty list if no project has that name).
    """
    raise NotImplementedError
