# Scenario: file-path bookkeeping for a report generator. Concepts:
# `Path` construction and joining with `/`, `.glob`, `.stem`, `.suffix`,
# `.with_suffix`. Tests build real (temporary) directory trees.
# Run: uv run pytest 06-errors-files -k ex06


def build_report_path(base, name):
    """Return the Path for a report file inside a "reports" subfolder of
    `base`, named `f"{name}.txt"`.

    `base` is a Path. Don't touch the filesystem — just build the path
    with `/`.

    build_report_path(Path("/tmp"), "q1") -> Path("/tmp/reports/q1.txt")
    """
    raise NotImplementedError


def find_py_files(folder):
    """Return every ".py" file directly inside `folder` (not
    subfolders), as a list of Path objects sorted by name.

    `folder` is a Path that exists. Use `.glob("*.py")` and `sorted`.

    find_py_files(folder containing b.py, a.py, notes.txt)
        -> [folder / "a.py", folder / "b.py"]
    """
    raise NotImplementedError


def swap_suffix(path, new_suffix):
    """Return a new Path equal to `path` but with its suffix replaced by
    `new_suffix` (which includes the leading dot, e.g. ".json").

    swap_suffix(Path("data/report.csv"), ".json") -> Path("data/report.json")
    """
    raise NotImplementedError
