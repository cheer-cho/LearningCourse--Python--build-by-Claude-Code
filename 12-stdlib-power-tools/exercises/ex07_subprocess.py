# Scenario: shelling out to another process the safe way — capturing
# output instead of letting it print straight to the terminal, and
# never letting a bad command crash the caller. Concepts: subprocess.run,
# capture_output, returncode, check=False.
# Run: uv run pytest 12-stdlib-power-tools -k ex07

import subprocess  # noqa: F401 — needed once functions are implemented
import sys  # noqa: F401 — needed once functions are implemented


def python_version() -> str:
    """Run `[sys.executable, "--version"]`, capture its output, and
    return it stripped of trailing whitespace.

    python_version() -> "Python 3.12.4"  (exact patch version varies)
    """
    raise NotImplementedError


def run_snippet(code: str) -> tuple[int, str, str]:
    """Run `code` as a Python one-liner via `-c` and return
    (returncode, stdout, stderr).

    run_snippet("print(1 + 1)") -> (0, "2\\n", "")
    run_snippet("import sys; sys.exit(3)") -> (3, "", "")
    """
    raise NotImplementedError


def safe_run(cmd: list[str]) -> dict[str, object]:
    """Run `cmd` and never raise, even if the command doesn't exist.
    Returns {"ok": bool, "returncode": int | None, "stdout": str,
    "stderr": str}. "ok" is True only when the process ran and exited
    with code 0. If the command can't be started at all (e.g. it isn't
    on PATH), catch the OSError, set "ok" False, "returncode" None, and
    put the exception message in "stderr".

    safe_run([sys.executable, "-c", "print('hi')"])
        -> {"ok": True, "returncode": 0, "stdout": "hi\\n", "stderr": ""}
    safe_run(["not-a-real-command-xyz"])
        -> {"ok": False, "returncode": None, "stdout": "", "stderr": "..."}
    """
    raise NotImplementedError
