import subprocess
import sys
import typing
from pathlib import Path

from ex02_collections import index_by_name, pair, scores_tuple, total

THIS_FILE = Path(__file__).resolve().parent / "ex02_collections.py"


def test_total_behaves_correctly():
    assert total([1.5, 2.0, 0.5]) == 4.0
    assert total([]) == 0.0


def test_total_is_annotated():
    hints = typing.get_type_hints(total)
    assert hints.get("prices") == list[float]
    assert hints.get("return") is float


def test_index_by_name_behaves_correctly():
    users = [{"name": "Ada", "age": 36}, {"name": "Bo", "age": 20}]
    assert index_by_name(users) == {
        "Ada": {"name": "Ada", "age": 36},
        "Bo": {"name": "Bo", "age": 20},
    }


def test_index_by_name_is_annotated():
    hints = typing.get_type_hints(index_by_name)
    assert hints.get("users") == list[dict[str, object]]
    assert hints.get("return") == dict[str, dict[str, object]]


def test_pair_behaves_correctly():
    assert pair() == ("Grace", 85)


def test_pair_is_annotated():
    hints = typing.get_type_hints(pair)
    assert hints.get("return") == tuple[str, int]


def test_scores_tuple_behaves_correctly():
    assert scores_tuple(1, 2, 3) == (1, 2, 3)
    assert scores_tuple() == ()


def test_scores_tuple_is_annotated():
    hints = typing.get_type_hints(scores_tuple)
    assert hints.get("scores") is int
    assert hints.get("return") == tuple[int, ...]


def test_ex02_passes_mypy_strict():
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", str(THIS_FILE)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
