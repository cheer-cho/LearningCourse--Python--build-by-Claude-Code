import math
import subprocess
import sys
import typing
from collections.abc import Iterable
from pathlib import Path

import pytest
from ex07_protocols import Circle, HasArea, Square, total_area

THIS_FILE = Path(__file__).resolve().parent / "ex07_protocols.py"


def test_circle_area():
    assert total_area([Circle(1.0)]) == pytest.approx(math.pi)


def test_square_area():
    assert total_area([Square(2.0)]) == 4.0


def test_total_area_sums_mixed_shapes():
    assert total_area([Square(2.0), Square(1.0)]) == 5.0


def test_total_area_is_annotated():
    hints = typing.get_type_hints(total_area)
    assert hints.get("shapes") == Iterable[HasArea]
    assert hints.get("return") is float


def test_has_area_declares_area_method():
    assert hasattr(HasArea, "area")
    hints = typing.get_type_hints(HasArea.area)
    assert hints.get("return") is float


def test_circle_and_square_do_not_inherit_has_area():
    assert HasArea not in Circle.__bases__
    assert HasArea not in Square.__bases__


def test_ex07_passes_mypy_strict():
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", str(THIS_FILE)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
