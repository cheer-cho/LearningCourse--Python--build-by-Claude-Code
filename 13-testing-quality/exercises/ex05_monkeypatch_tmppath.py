# Scenario: reading an API key from the environment, and caching
# results to disk as JSON. Concepts: monkeypatch (env vars) and
# tmp_path (real filesystem, auto-cleaned) — seen here from the
# consumer side. Read `test_ex05_monkeypatch_tmppath.py`: it's the part
# of this exercise that teaches you something, showing exactly how
# `monkeypatch` and `tmp_path` drive the functions below.
# Run: uv run pytest 13-testing-quality -k ex05

from pathlib import Path


def read_api_key() -> str:
    """Return the value of the `API_KEY` environment variable.

    Raise `RuntimeError("API_KEY is not set")` if the variable is
    absent OR set to an empty string.

    (with env API_KEY=abc123) read_api_key() -> "abc123"
    (with API_KEY unset) read_api_key() -> raises RuntimeError
    """
    raise NotImplementedError


def cache_result(path: Path, key: str, value: str) -> None:
    """Store `value` under `key` in a JSON object at `path`.

    If `path` doesn't exist yet, create it holding just `{key: value}`.
    If it already holds a JSON object, merge `key: value` into it —
    don't drop the other keys already there.

    cache_result(tmp_path / "cache.json", "pi", "3.14")
        -> tmp_path / "cache.json" now contains {"pi": "3.14"}
    """
    raise NotImplementedError


def cached(path: Path, key: str) -> str | None:
    """Return the cached value for `key` at `path`, or `None` if
    `path` doesn't exist yet or doesn't contain `key`.

    cached(tmp_path / "cache.json", "pi") -> "3.14"   (after cache_result above)
    cached(tmp_path / "does_not_exist.json", "pi") -> None
    """
    raise NotImplementedError
