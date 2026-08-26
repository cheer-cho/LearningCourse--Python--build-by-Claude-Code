# Scenario: a small API client that other code hands an httpx.Client to
# (dependency injection, not a module-level singleton — that's what makes
# it testable with MockTransport, no real network). Concepts: httpx.Client,
# raise_for_status, .json(), MockTransport, retry loops.
# Run: uv run pytest 14-frameworks-libraries -k ex03

from __future__ import annotations

import httpx


class ApiError(Exception):
    """Raised when a request ultimately fails. Carries the HTTP status
    code of the last response so callers can decide how to react.
    """

    def __init__(self, message: str, status_code: int) -> None:
        super().__init__(message)
        self.status_code = status_code


def get_json(client: httpx.Client, url: str) -> dict[str, object]:
    """GET `url` via `client` and return the parsed JSON body.

    Raises `ApiError` (not `httpx.HTTPStatusError`) if the response is a
    4xx or 5xx — callers of this function shouldn't need to know it's
    built on httpx.

    get_json(client, "/health") -> {"status": "ok"}  (on a 200 response)
    """
    raise NotImplementedError


def fetch_with_retry(client: httpx.Client, url: str, attempts: int = 3) -> dict[str, object]:
    """GET `url` via `client`, retrying on a 5xx response up to
    `attempts` total tries. A 4xx response raises `ApiError` immediately
    (retrying won't fix a client error). Raises `ApiError` if every
    attempt comes back 5xx.

    fetch_with_retry(client, "/flaky", attempts=3) -> the JSON body of
    whichever attempt (1st, 2nd, or 3rd) first returns < 400.
    """
    raise NotImplementedError
