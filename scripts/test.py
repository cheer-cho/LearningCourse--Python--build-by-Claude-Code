"""Course test runner.

    uv run python scripts/test.py           -> run every module
    uv run python scripts/test.py 3          -> module 03 only ("3" or "03" work)
    uv run python scripts/test.py 3 -k ex02  -> one exercise within module 03

Extra pytest flags pass straight through after the module number.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def module_dirs() -> list[Path]:
    return sorted(p for p in ROOT.glob("[0-9][0-9]-*") if p.is_dir())


def main(argv: list[str]) -> int:
    dirs = module_dirs()

    if not argv or argv[0].startswith("-"):
        return pytest.main([str(ROOT), *argv])

    wanted, *rest = argv
    if not re.fullmatch(r"\d+", wanted):
        return pytest.main([str(ROOT), *argv])

    prefix = wanted.zfill(2) + "-"
    match = next((d for d in dirs if d.name.startswith(prefix)), None)
    if match is None:
        available = "\n  ".join(d.name for d in dirs) or "(none yet)"
        print(f'No module matches "{wanted}". Available modules:\n  {available}', file=sys.stderr)
        return 1

    return pytest.main([str(match), *rest])


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
