import subprocess
import sys
import typing
from pathlib import Path

from ex08_overload_cast import load_scores, scale

THIS_FILE = Path(__file__).resolve().parent / "ex08_overload_cast.py"


def test_scale_int_behaves_correctly():
    assert scale(3, 2) == 6


def test_scale_list_behaves_correctly():
    assert scale([1, 2, 3], 2) == [2, 4, 6]


def test_scale_has_two_overloads_typed_int_and_list():
    overloads = typing.get_overloads(scale)
    assert len(overloads) == 2

    signatures = [typing.get_type_hints(f) for f in overloads]
    int_sig = next((s for s in signatures if s.get("x") is int), None)
    list_sig = next((s for s in signatures if s.get("x") == list[int]), None)

    assert int_sig is not None, "expected an overload with x: int"
    assert int_sig.get("k") is int
    assert int_sig.get("return") is int

    assert list_sig is not None, "expected an overload with x: list[int]"
    assert list_sig.get("k") is int
    assert list_sig.get("return") == list[int]


def test_scale_implementation_is_annotated():
    hints = typing.get_type_hints(scale)
    assert hints.get("x") == int | list[int]
    assert hints.get("k") is int
    assert hints.get("return") == int | list[int]


def test_load_scores_behaves_correctly():
    assert load_scores("[1, 2, 3]") == [1, 2, 3]


def test_load_scores_is_annotated():
    hints = typing.get_type_hints(load_scores)
    assert hints.get("raw") is str
    assert hints.get("return") == list[int]


def test_ex08_passes_mypy_strict():
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", str(THIS_FILE)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
