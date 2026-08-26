"""Tests for ex04_ruff_cleanup.

Run: uv run pytest 01-setup-tooling -k ex04
"""

import subprocess
from pathlib import Path

from ex04_ruff_cleanup import total_unique_length

ROOT = Path(__file__).resolve().parents[2]
EXERCISE_FILE = Path(__file__).resolve().parent / "ex04_ruff_cleanup.py"


def test_total_unique_length_counts_each_word_once():
    assert total_unique_length(["a", "bb", "a"]) == 3


def test_total_unique_length_empty_list_is_zero():
    assert total_unique_length([]) == 0


def test_total_unique_length_all_duplicates():
    assert total_unique_length(["cat", "cat", "cat"]) == 3


def test_file_is_ruff_clean():
    result = subprocess.run(
        ["uv", "run", "ruff", "check", str(EXERCISE_FILE)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
