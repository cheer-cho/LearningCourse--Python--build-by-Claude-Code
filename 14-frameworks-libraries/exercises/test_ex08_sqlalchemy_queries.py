import pytest

pytest.importorskip("sqlalchemy")

from ex08_sqlalchemy_queries import (
    Project,
    TaskRow,
    complete_and_count,
    make_engine,
    open_tasks,
    rename_task,
    tasks_of,
)
from sqlalchemy.orm import Session


@pytest.fixture
def session():
    engine = make_engine()
    with Session(engine) as session:
        alpha = Project(name="Alpha")
        beta = Project(name="Beta")
        session.add_all(
            [
                alpha,
                beta,
                TaskRow(title="Design schema", done=True, project=alpha),
                TaskRow(title="Write queries", done=False, project=alpha),
                TaskRow(title="Ship it", done=False, project=beta),
            ]
        )
        session.commit()
        yield session


def test_open_tasks_excludes_done(session):
    titles = {task.title for task in open_tasks(session)}
    assert titles == {"Write queries", "Ship it"}


def test_rename_task_updates_title(session):
    task = open_tasks(session)[0]
    renamed = rename_task(session, task.id, "Renamed")
    assert renamed.title == "Renamed"
    assert session.get(TaskRow, task.id).title == "Renamed"


def test_complete_and_count_marks_done_and_counts_all_done(session):
    target = next(t for t in open_tasks(session) if t.title == "Write queries")
    count = complete_and_count(session, target.id)
    assert count == 2  # "Design schema" was already done


def test_complete_and_count_persists_the_change(session):
    target = next(t for t in open_tasks(session) if t.title == "Ship it")
    complete_and_count(session, target.id)
    assert session.get(TaskRow, target.id).done is True


def test_tasks_of_returns_only_that_projects_tasks(session):
    titles = {task.title for task in tasks_of(session, "Alpha")}
    assert titles == {"Design schema", "Write queries"}


def test_tasks_of_unknown_project_returns_empty(session):
    assert tasks_of(session, "Nonexistent") == []
