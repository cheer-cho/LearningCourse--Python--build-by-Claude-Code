from pathlib import Path

from ex06_pathlib import build_report_path, find_py_files, swap_suffix


def test_build_report_path_joins_reports_and_filename():
    result = build_report_path(Path("/tmp"), "q1")
    assert result == Path("/tmp/reports/q1.txt")


def test_build_report_path_does_not_touch_filesystem(tmp_path):
    result = build_report_path(tmp_path, "q1")
    assert not result.exists()


def test_find_py_files_returns_sorted_py_files(tmp_path):
    (tmp_path / "b.py").write_text("", encoding="utf-8")
    (tmp_path / "a.py").write_text("", encoding="utf-8")
    (tmp_path / "notes.txt").write_text("", encoding="utf-8")

    result = find_py_files(tmp_path)

    assert result == [tmp_path / "a.py", tmp_path / "b.py"]


def test_find_py_files_ignores_subfolder_contents(tmp_path):
    (tmp_path / "top.py").write_text("", encoding="utf-8")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "nested.py").write_text("", encoding="utf-8")

    result = find_py_files(tmp_path)

    assert result == [tmp_path / "top.py"]


def test_find_py_files_empty_folder(tmp_path):
    assert find_py_files(tmp_path) == []


def test_swap_suffix_replaces_extension():
    assert swap_suffix(Path("data/report.csv"), ".json") == Path("data/report.json")


def test_swap_suffix_on_path_with_no_suffix():
    assert swap_suffix(Path("data/report"), ".txt") == Path("data/report.txt")
