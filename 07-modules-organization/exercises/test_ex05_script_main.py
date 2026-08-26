import subprocess
from pathlib import Path

from ex05_script_main import run

SCRIPT = Path(__file__).resolve().parent / "ex05_script_main.py"


def _repo_root(start):
    """Walk up from `start` to find the real repo root (the directory
    holding uv.lock) — works whether tests run in place or from inside
    scripts/verify_solutions.py's `.verify/` working copy.
    """
    for parent in [start, *start.parents]:
        if (parent / "uv.lock").exists():
            return parent
    return start


ROOT = _repo_root(SCRIPT.parent)


def test_run_prints_report_and_returns_zero(capsys):
    code = run(["10", "20", "30"])
    out = capsys.readouterr().out
    assert code == 0
    assert "count: 3" in out
    assert "total: 60.0" in out
    assert "average: 20.0" in out


def test_run_single_number(capsys):
    code = run(["5"])
    out = capsys.readouterr().out
    assert code == 0
    assert "count: 1" in out
    assert "average: 5.0" in out


def test_run_empty_argv_errors(capsys):
    code = run([])
    out = capsys.readouterr().out
    assert code == 1
    assert out.startswith("error:")


def test_run_invalid_number_errors(capsys):
    code = run(["a"])
    out = capsys.readouterr().out
    assert code == 1
    assert "invalid number: a" in out


def test_script_runs_as_subprocess_with_valid_args():
    result = subprocess.run(
        ["uv", "run", "python", str(SCRIPT), "10", "20", "30"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=60,
    )
    assert result.returncode == 0
    assert "count: 3" in result.stdout


def test_script_runs_as_subprocess_with_bad_arg():
    result = subprocess.run(
        ["uv", "run", "python", str(SCRIPT), "not-a-number"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
        timeout=60,
    )
    assert result.returncode == 1
    assert "error:" in result.stdout
