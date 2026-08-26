import subprocess
import sys
import typing
from pathlib import Path

from ex06_generics import Box, T, first, last_or

THIS_FILE = Path(__file__).resolve().parent / "ex06_generics.py"


def test_first_behaves_correctly():
    assert first([1, 2, 3]) == 1
    assert first(["a", "b"]) == "a"


def test_first_is_annotated_with_typevar():
    hints = typing.get_type_hints(first)
    assert hints.get("items") == list[T]
    assert hints.get("return") is T


def test_last_or_behaves_correctly():
    assert last_or([1, 2, 3], 0) == 3
    assert last_or([], 0) == 0


def test_last_or_is_annotated_with_typevar():
    hints = typing.get_type_hints(last_or)
    assert hints.get("items") == list[T]
    assert hints.get("default") is T
    assert hints.get("return") is T


def test_box_behaves_correctly():
    box = Box(5)
    assert box.get() == 5
    box.put(6)
    assert box.get() == 6


def test_box_is_annotated_with_typevar():
    init_hints = typing.get_type_hints(Box.__init__)
    assert init_hints.get("value") is T
    get_hints = typing.get_type_hints(Box.get)
    assert get_hints.get("return") is T
    put_hints = typing.get_type_hints(Box.put)
    assert put_hints.get("value") is T
    assert put_hints.get("return") is type(None)


def test_ex06_passes_mypy_strict():
    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", str(THIS_FILE)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_box_rejects_wrong_type_for_its_typevar(tmp_path):
    """The `Box` above must genuinely tie `put`/`get` to T — not quietly
    accept anything via `Any`. Copy the current source, add a small probe
    that puts a str into a Box[int], and confirm mypy catches it. If this
    test fails, `Box` type-checks but doesn't actually enforce T.
    """
    source = THIS_FILE.read_text()
    probe = (
        "\n\n"
        "def _type_error_probe() -> None:\n"
        '    int_box: Box[int] = Box(5)\n'
        '    int_box.put("not an int")\n'
    )
    probe_file = tmp_path / "ex06_generics_probe.py"
    probe_file.write_text(source + probe)

    result = subprocess.run(
        [sys.executable, "-m", "mypy", "--strict", str(probe_file)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0, "mypy should reject Box[int].put('not an int')"
    assert "put" in result.stdout
