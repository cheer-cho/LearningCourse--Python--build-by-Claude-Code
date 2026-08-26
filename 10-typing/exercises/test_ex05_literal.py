import subprocess
import sys
import typing
from pathlib import Path
from typing import Literal

from ex05_literal import day_number, sort_scores

THIS_FILE = Path(__file__).resolve().parent / "ex05_literal.py"


def test_sort_scores_ascending():
    assert sort_scores([3, 1, 2], "asc") == [1, 2, 3]


def test_sort_scores_descending():
    assert sort_scores([3, 1, 2], "desc") == [3, 2, 1]


def test_sort_scores_is_annotated():
    hints = typing.get_type_hints(sort_scores)
    assert hints.get("scores") == list[int]
    assert hints.get("direction") == Literal["asc", "desc"]
    assert hints.get("return") == list[int]


def test_day_number_monday_is_one():
    assert day_number("Mon") == 1


def test_day_number_sunday_is_seven():
    assert day_number("Sun") == 7


def test_day_number_is_annotated():
    hints = typing.get_type_hints(day_number)
    assert hints.get("day") == Literal["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    assert hints.get("return") is int


def test_ex05_passes_mypy_strict():
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", str(THIS_FILE)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
