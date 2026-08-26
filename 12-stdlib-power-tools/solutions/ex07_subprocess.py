import subprocess
import sys


def python_version() -> str:
    result = subprocess.run(
        [sys.executable, "--version"], capture_output=True, text=True, check=False
    )
    output = result.stdout or result.stderr
    return output.strip()


def run_snippet(code: str) -> tuple[int, str, str]:
    result = subprocess.run(
        [sys.executable, "-c", code], capture_output=True, text=True, check=False
    )
    return result.returncode, result.stdout, result.stderr


def safe_run(cmd: list[str]) -> dict[str, object]:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    except OSError as exc:
        return {"ok": False, "returncode": None, "stdout": "", "stderr": str(exc)}
    return {
        "ok": result.returncode == 0,
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
