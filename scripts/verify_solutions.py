"""Maintenance tool (used by the instructor, not part of the course):
copies each module into ``.verify/``, overlays every ``solutions/`` file
onto its exercise stub and checkpoint, and runs the test suite there. All
tests should be GREEN when run against the reference solutions.

    uv run python scripts/verify_solutions.py        -> verify all modules
    uv run python scripts/verify_solutions.py 03      -> verify one module
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Per-process run dir so concurrent invocations (e.g. several modules being
# maintained at once) never delete each other's working copies.
VERIFY_DIR = ROOT / ".verify" / f"run-{os.getpid()}"


def module_dirs() -> list[Path]:
    return sorted(p for p in ROOT.glob("[0-9][0-9]-*") if p.is_dir())


def prepare(module_dir: Path) -> Path:
    """Copy a module into .verify/ and overlay solutions onto stubs."""
    dest = VERIFY_DIR / module_dir.name
    shutil.copytree(module_dir, dest)

    solutions = dest / "solutions"
    if solutions.is_dir():
        for solution_file in solutions.iterdir():
            if solution_file.suffix != ".py":
                continue
            if solution_file.name.startswith("checkpoint_"):
                target = dest / solution_file.name
            else:
                target = dest / "exercises" / solution_file.name
            if target.exists():
                shutil.copyfile(solution_file, target)
    return dest


def resolve_targets(dirs: list[Path], argv: list[str]) -> list[Path] | None:
    if not argv:
        return dirs

    wanted = argv[0]
    if not re.fullmatch(r"\d+", wanted):
        print("Usage: verify_solutions.py [NN]", file=sys.stderr)
        return None

    prefix = wanted.zfill(2) + "-"
    match = next((d for d in dirs if d.name.startswith(prefix)), None)
    if match is None:
        available = "\n  ".join(d.name for d in dirs) or "(none yet)"
        print(f'No module matches "{wanted}". Available modules:\n  {available}', file=sys.stderr)
        return None
    return [match]


def main(argv: list[str]) -> int:
    dirs = module_dirs()
    if not dirs:
        print("No module folders yet.")
        return 0

    targets = resolve_targets(dirs, argv)
    if targets is None:
        return 1

    shutil.rmtree(VERIFY_DIR, ignore_errors=True)
    VERIFY_DIR.mkdir(parents=True)  # parents covers .verify/ itself
    shutil.copyfile(ROOT / "conftest.py", VERIFY_DIR / "conftest.py")
    pyproject = ROOT / "pyproject.toml"
    if pyproject.exists():
        shutil.copyfile(pyproject, VERIFY_DIR / "pyproject.toml")

    overall_ok = True
    for module_dir in targets:
        dest = prepare(module_dir)
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(dest), "--import-mode=importlib"],
            cwd=VERIFY_DIR,
            check=False,
        )
        ok = result.returncode == 0
        overall_ok = overall_ok and ok
        print(f"{'PASS' if ok else 'FAIL'}  {module_dir.name}")

    shutil.rmtree(VERIFY_DIR, ignore_errors=True)
    return 0 if overall_ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
