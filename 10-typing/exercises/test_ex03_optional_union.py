import subprocess
import sys
import typing
from pathlib import Path

from ex03_optional_union import describe, find_user, first_non_none

THIS_FILE = Path(__file__).resolve().parent / "ex03_optional_union.py"


def test_find_user_returns_match():
    assert find_user([{"name": "Ada"}], "Ada") == {"name": "Ada"}


def test_find_user_returns_none_when_missing():
    assert find_user([{"name": "Ada"}], "Bo") is None


def test_find_user_is_annotated():
    hints = typing.get_type_hints(find_user)
    assert hints.get("users") == list[dict[str, object]]
    assert hints.get("name") is str
    assert hints.get("return") == dict[str, object] | None


def test_describe_handles_int():
    assert describe(5) == "int: 5"


def test_describe_handles_str():
    assert describe("hi") == "str: 'hi'"


def test_describe_is_annotated():
    hints = typing.get_type_hints(describe)
    assert hints.get("x") == int | str
    assert hints.get("return") is str


def test_first_non_none_prefers_a():
    assert first_non_none(5, None) == 5


def test_first_non_none_falls_back_to_b():
    assert first_non_none(None, 3) == 3


def test_first_non_none_is_annotated():
    hints = typing.get_type_hints(first_non_none)
    assert hints.get("a") == int | None
    assert hints.get("b") == int | None
    assert hints.get("return") is int


def test_ex03_passes_mypy_strict():
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", str(THIS_FILE)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
