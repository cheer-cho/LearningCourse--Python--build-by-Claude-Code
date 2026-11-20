"""What is pytest's `tmp_path` fixture?

Run: uv run pytest playground/06-errors-files/test_tmp_path_demo.py -s
"""

from pathlib import Path


def test_what_is_tmp_path(tmp_path: Path) -> None:
    # 1. It's a plain pathlib.Path — same type as ex06.
    print(f"\ntype:   {type(tmp_path).__name__}")
    print(f"where:  {tmp_path}")

    # 2. The folder already exists, and it starts empty.
    assert tmp_path.is_dir()
    assert list(tmp_path.iterdir()) == []

    # 3. Use it like any Path: build file paths with /.
    notes = tmp_path / "notes.txt"
    notes.write_text("hello\n", encoding="utf-8")
    assert notes.read_text(encoding="utf-8") == "hello\n"


def test_each_test_gets_its_own_folder(tmp_path: Path) -> None:
    # notes.txt from the test above is NOT here — fresh folder per test.
    print(f"\nwhere:  {tmp_path}")
    assert not (tmp_path / "notes.txt").exists()
