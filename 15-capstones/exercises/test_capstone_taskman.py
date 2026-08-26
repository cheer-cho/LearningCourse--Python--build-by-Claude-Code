"""Acceptance tests for Capstone A. Exercises the service layer directly
against an in-memory engine, then the CLI end-to-end via CliRunner against
a tmp sqlite file, then a mypy --strict subprocess check on the module
itself (types must be clean even before the logic is correct).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

pytest.importorskip("typer")
pytest.importorskip("sqlalchemy")

from capstone_taskman import (
    TaskNotFound,
    add_task,
    app,
    complete_task,
    list_tasks,
    make_engine,
)
from sqlalchemy.orm import Session
from typer.testing import CliRunner

runner = CliRunner()


@pytest.fixture
def session():
    engine = make_engine("sqlite:///:memory:")
    with Session(engine) as s:
        yield s


# --- service layer ---------------------------------------------------


def test_add_task_sets_fields_and_assigns_id(session):
    task = add_task(session, "Buy milk", priority="high")
    assert task.id is not None
    assert task.title == "Buy milk"
    assert task.priority == "high"
    assert task.done is False


def test_add_task_defaults_priority_to_normal(session):
    task = add_task(session, "Water plants")
    assert task.priority == "normal"


def test_complete_task_marks_done_and_returns_row(session):
    task = add_task(session, "Buy milk")
    completed = complete_task(session, task.id)
    assert completed.done is True
    assert completed.id == task.id


def test_complete_task_missing_id_raises_task_not_found(session):
    with pytest.raises(TaskNotFound):
        complete_task(session, 999)


def test_list_tasks_excludes_done_by_default(session):
    add_task(session, "Pending")
    done = add_task(session, "Finished")
    complete_task(session, done.id)
    titles = [t.title for t in list_tasks(session)]
    assert titles == ["Pending"]


def test_list_tasks_include_done_returns_everything(session):
    add_task(session, "Pending")
    done = add_task(session, "Finished")
    complete_task(session, done.id)
    titles = {t.title for t in list_tasks(session, include_done=True)}
    assert titles == {"Pending", "Finished"}


def test_list_tasks_sort_by_priority_is_ascending(session):
    add_task(session, "Low task", priority="low")
    add_task(session, "High task", priority="high")
    add_task(session, "Medium task", priority="medium")
    priorities = [t.priority for t in list_tasks(session, sort="priority")]
    assert priorities == sorted(priorities)


def test_list_tasks_unknown_sort_falls_back_to_id_order(session):
    add_task(session, "First")
    add_task(session, "Second")
    titles = [t.title for t in list_tasks(session, sort="nonsense")]
    assert titles == ["First", "Second"]


# --- CLI (end-to-end via CliRunner against a tmp sqlite file) --------


def test_cli_add_then_list_shows_the_task(tmp_path):
    db = tmp_path / "tasks.db"
    result = runner.invoke(app, ["--db", str(db), "add", "Buy milk", "--priority", "high"])
    assert result.exit_code == 0, result.output

    result = runner.invoke(app, ["--db", str(db), "list"])
    assert result.exit_code == 0, result.output
    assert "Buy milk" in result.output


def test_cli_done_marks_task_complete_and_hides_it_from_default_list(tmp_path):
    db = tmp_path / "tasks.db"
    runner.invoke(app, ["--db", str(db), "add", "Buy milk"])

    result = runner.invoke(app, ["--db", str(db), "done", "1"])
    assert result.exit_code == 0, result.output

    result = runner.invoke(app, ["--db", str(db), "list"])
    assert "Buy milk" not in result.output

    result = runner.invoke(app, ["--db", str(db), "list", "--all"])
    assert "Buy milk" in result.output


def test_cli_done_on_missing_task_exits_nonzero_with_message(tmp_path):
    db = tmp_path / "tasks.db"
    runner.invoke(app, ["--db", str(db), "add", "Buy milk"])

    result = runner.invoke(app, ["--db", str(db), "done", "999"])
    assert result.exit_code != 0
    assert "999" in result.output


def test_cli_stats_counts_by_priority(tmp_path):
    db = tmp_path / "tasks.db"
    runner.invoke(app, ["--db", str(db), "add", "A", "--priority", "high"])
    runner.invoke(app, ["--db", str(db), "add", "B", "--priority", "high"])
    runner.invoke(app, ["--db", str(db), "add", "C", "--priority", "low"])

    result = runner.invoke(app, ["--db", str(db), "stats"])
    assert result.exit_code == 0, result.output
    assert "high: 2" in result.output
    assert "low: 1" in result.output


def test_cli_list_with_no_tasks_says_so(tmp_path):
    db = tmp_path / "tasks.db"
    result = runner.invoke(app, ["--db", str(db), "list"])
    assert result.exit_code == 0, result.output
    assert "No tasks" in result.output


# --- static typing -----------------------------------------------------


def test_capstone_taskman_passes_mypy_strict():
    target = Path(__file__).parent / "capstone_taskman.py"
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", str(target)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
