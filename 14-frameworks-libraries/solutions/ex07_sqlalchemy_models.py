from sqlalchemy import Engine, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class TaskRow(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    done: Mapped[bool] = mapped_column(default=False)


def make_engine() -> Engine:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return engine


def add_task(session: Session, title: str) -> TaskRow:
    task = TaskRow(title=title)
    session.add(task)
    session.flush()
    return task


def all_tasks(session: Session) -> list[TaskRow]:
    return list(session.scalars(select(TaskRow)))
