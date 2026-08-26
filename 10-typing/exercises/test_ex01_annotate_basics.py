import subprocess
import sys
import typing
from pathlib import Path

from ex01_annotate_basics import banner, ratio, repeat, shout

THIS_FILE = Path(__file__).resolve().parent / "ex01_annotate_basics.py"


def test_shout_behaves_correctly():
    assert shout("hello") == "HELLO!"
    assert shout("") == "!"


def test_shout_is_annotated():
    hints = typing.get_type_hints(shout)
    assert hints.get("text") is str
    assert hints.get("return") is str


def test_repeat_behaves_correctly():
    assert repeat("go", 3) == "go go go"
    assert repeat("hi", 0) == ""


def test_repeat_is_annotated():
    hints = typing.get_type_hints(repeat)
    assert hints.get("word") is str
    assert hints.get("times") is int
    assert hints.get("return") is str


def test_banner_prints_and_returns_none(capsys):
    result = banner("Hi")
    assert result is None
    assert capsys.readouterr().out == "=== Hi ===\n"


def test_banner_is_annotated():
    hints = typing.get_type_hints(banner)
    assert hints.get("text") is str
    assert hints.get("return") is type(None)


def test_ratio_behaves_correctly():
    assert ratio(9, 2) == 4.5
    assert ratio(5, 2) == 2.5


def test_ratio_is_annotated():
    hints = typing.get_type_hints(ratio)
    assert hints.get("a") is float
    assert hints.get("b") is float
    assert hints.get("return") is float


def test_ex01_passes_mypy_strict():
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", str(THIS_FILE)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
