import pytest

pytest.importorskip("sqlalchemy")

from ex07_sqlalchemy_models import add_task, all_tasks, make_engine
from sqlalchemy.orm import Session


@pytest.fixture
def session():
    engine = make_engine()
    with Session(engine) as session:
        yield session


def test_add_task_assigns_an_id():
    engine = make_engine()
    with Session(engine) as session:
        task = add_task(session, "Buy milk")
        assert task.id is not None
        assert task.title == "Buy milk"
        assert task.done is False


def test_all_tasks_empty_database():
    engine = make_engine()
    with Session(engine) as session:
        assert all_tasks(session) == []


def test_all_tasks_returns_every_task(session):
    add_task(session, "Buy milk")
    add_task(session, "Walk dog")
    titles = {task.title for task in all_tasks(session)}
    assert titles == {"Buy milk", "Walk dog"}


def test_make_engine_gives_independent_databases():
    engine_a = make_engine()
    engine_b = make_engine()
    with Session(engine_a) as session_a:
        add_task(session_a, "Only in A")
    with Session(engine_b) as session_b:
        assert all_tasks(session_b) == []
