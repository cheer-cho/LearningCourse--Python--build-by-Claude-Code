"""Tests for checkpoint_01 — the About-me card.

Run: uv run pytest 01-setup-tooling -k checkpoint
"""

import subprocess
import sys
from pathlib import Path

from checkpoint_01 import build_card, main

MODULE_DIR = Path(__file__).resolve().parent
CHECKPOINT_FILE = MODULE_DIR / "checkpoint_01.py"


def test_build_card_has_a_name_line_and_an_age_line():
    card = build_card("Ada", 28)
    assert card.splitlines() == ["Name: Ada", "Age: 28"]


def test_build_card_uses_both_arguments():
    card = build_card("Grace", 41)
    assert "Grace" in card
    assert "41" in card


def test_main_prints_a_card(capsys):
    main()
    captured = capsys.readouterr()
    assert "Name:" in captured.out
    assert "Age:" in captured.out


def test_importing_the_module_prints_nothing():
    result = subprocess.run(
        [sys.executable, "-c", "import checkpoint_01"],
        cwd=MODULE_DIR,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert result.stdout == ""


def test_file_is_ruff_clean():
    result = subprocess.run(
        ["uv", "run", "ruff", "check", str(CHECKPOINT_FILE)],
        cwd=MODULE_DIR.parent,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
