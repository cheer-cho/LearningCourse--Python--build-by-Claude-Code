from sqlalchemy import Engine, ForeignKey, String, create_engine, func, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    tasks: Mapped[list["TaskRow"]] = relationship(back_populates="project")


class TaskRow(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    done: Mapped[bool] = mapped_column(default=False)
    project_id: Mapped[int | None] = mapped_column(ForeignKey("projects.id"), default=None)
    project: Mapped[Project | None] = relationship(back_populates="tasks")


def make_engine() -> Engine:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return engine


def open_tasks(session: Session) -> list[TaskRow]:
    return list(session.scalars(select(TaskRow).where(TaskRow.done.is_(False))))


def rename_task(session: Session, task_id: int, title: str) -> TaskRow:
    task = session.get(TaskRow, task_id)
    assert task is not None
    task.title = title
    session.flush()
    return task


def complete_and_count(session: Session, task_id: int) -> int:
    task = session.get(TaskRow, task_id)
    assert task is not None
    task.done = True
    session.flush()
    return session.scalar(select(func.count()).select_from(TaskRow).where(TaskRow.done.is_(True))) or 0


def tasks_of(session: Session, project_name: str) -> list[TaskRow]:
    return list(
        session.scalars(select(TaskRow).join(Project).where(Project.name == project_name))
    )
