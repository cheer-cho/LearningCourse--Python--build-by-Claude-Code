def build_report_path(base, name):
    return base / "reports" / f"{name}.txt"


def find_py_files(folder):
    return sorted(folder.glob("*.py"))


def swap_suffix(path, new_suffix):
    return path.with_suffix(new_suffix)
