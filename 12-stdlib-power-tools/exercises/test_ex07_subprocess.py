import sys

from ex07_subprocess import python_version, run_snippet, safe_run


def test_python_version_reports_python_3():
    assert python_version().startswith("Python 3.")


def test_run_snippet_captures_stdout():
    assert run_snippet("print(1 + 1)") == (0, "2\n", "")


def test_run_snippet_captures_nonzero_exit():
    returncode, stdout, stderr = run_snippet("import sys; sys.exit(3)")
    assert returncode == 3
    assert stdout == ""
    assert stderr == ""


def test_run_snippet_captures_stderr():
    returncode, stdout, stderr = run_snippet("import sys; print('oops', file=sys.stderr)")
    assert returncode == 0
    assert stdout == ""
    assert stderr == "oops\n"


def test_safe_run_success():
    result = safe_run([sys.executable, "-c", "print('hi')"])
    assert result == {"ok": True, "returncode": 0, "stdout": "hi\n", "stderr": ""}


def test_safe_run_nonzero_exit_is_not_ok():
    result = safe_run([sys.executable, "-c", "import sys; sys.exit(1)"])
    assert result["ok"] is False
    assert result["returncode"] == 1


def test_safe_run_missing_command_never_raises():
    result = safe_run(["not-a-real-command-xyz"])
    assert result["ok"] is False
    assert result["returncode"] is None
    assert result["stdout"] == ""
    assert isinstance(result["stderr"], str) and result["stderr"] != ""
