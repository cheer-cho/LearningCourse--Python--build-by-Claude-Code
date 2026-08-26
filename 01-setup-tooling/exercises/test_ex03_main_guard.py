"""Tests for ex03_main_guard.

Run: uv run pytest 01-setup-tooling -k ex03
"""

import subprocess
import sys
from pathlib import Path

from ex03_main_guard import main

EXERCISES_DIR = Path(__file__).resolve().parent


def test_importing_the_module_prints_nothing():
    result = subprocess.run(
        [sys.executable, "-c", "import ex03_main_guard"],
        cwd=EXERCISES_DIR,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert result.stdout == ""


def test_calling_main_prints_the_banner(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "=== Setup & Tooling ===\n"


def test_running_the_file_directly_prints_the_banner():
    result = subprocess.run(
        [sys.executable, "ex03_main_guard.py"],
        cwd=EXERCISES_DIR,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert result.stdout == "=== Setup & Tooling ===\n"
