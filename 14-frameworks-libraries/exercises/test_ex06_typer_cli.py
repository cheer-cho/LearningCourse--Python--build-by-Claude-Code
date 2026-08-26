import pytest

pytest.importorskip("typer")

from ex06_typer_cli import _TODOS, app, reset_todos
from typer.testing import CliRunner

runner = CliRunner()


@pytest.fixture(autouse=True)
def _clean_state():
    reset_todos()
    yield
    reset_todos()


def test_add_prints_confirmation_and_exits_zero():
    result = runner.invoke(app, ["add", "Buy milk"])
    assert result.exit_code == 0
    assert "Added: Buy milk" in result.output


def test_add_stores_priority_default_one():
    runner.invoke(app, ["add", "Buy milk"])
    assert _TODOS[0]["priority"] == 1


def test_add_stores_given_priority():
    runner.invoke(app, ["add", "Buy milk", "--priority", "3"])
    assert _TODOS[0]["priority"] == 3


def test_list_default_shows_only_pending():
    runner.invoke(app, ["add", "Buy milk"])
    runner.invoke(app, ["add", "Walk dog"])
    _TODOS[0]["done"] = True
    result = runner.invoke(app, ["list"])
    assert "Buy milk" not in result.output
    assert "Walk dog" in result.output


def test_list_done_shows_only_done():
    runner.invoke(app, ["add", "Buy milk"])
    runner.invoke(app, ["add", "Walk dog"])
    _TODOS[0]["done"] = True
    result = runner.invoke(app, ["list", "--done"])
    assert "Buy milk" in result.output
    assert "Walk dog" not in result.output


def test_list_all_shows_everything():
    runner.invoke(app, ["add", "Buy milk"])
    runner.invoke(app, ["add", "Walk dog"])
    _TODOS[0]["done"] = True
    result = runner.invoke(app, ["list", "--all"])
    assert "Buy milk" in result.output
    assert "Walk dog" in result.output
