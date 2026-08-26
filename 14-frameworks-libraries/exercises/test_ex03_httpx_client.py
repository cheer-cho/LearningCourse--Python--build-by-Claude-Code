import pytest

pytest.importorskip("httpx")

import httpx
from ex03_httpx_client import ApiError, fetch_with_retry, get_json


def _client(handler):
    return httpx.Client(transport=httpx.MockTransport(handler), base_url="https://example.test")


def test_get_json_returns_body_on_200():
    def handler(request):
        return httpx.Response(200, json={"status": "ok"})

    with _client(handler) as client:
        assert get_json(client, "/health") == {"status": "ok"}


def test_get_json_raises_api_error_on_404():
    def handler(request):
        return httpx.Response(404, json={"detail": "not found"})

    with _client(handler) as client:
        with pytest.raises(ApiError) as exc_info:
            get_json(client, "/missing")
        assert exc_info.value.status_code == 404


def test_fetch_with_retry_succeeds_after_transient_failures():
    calls = {"count": 0}

    def handler(request):
        calls["count"] += 1
        if calls["count"] < 3:
            return httpx.Response(503, json={"detail": "unavailable"})
        return httpx.Response(200, json={"status": "ok"})

    with _client(handler) as client:
        assert fetch_with_retry(client, "/flaky", attempts=3) == {"status": "ok"}
    assert calls["count"] == 3


def test_fetch_with_retry_gives_up_after_all_5xx():
    def handler(request):
        return httpx.Response(500, json={"detail": "boom"})

    with _client(handler) as client:
        with pytest.raises(ApiError) as exc_info:
            fetch_with_retry(client, "/down", attempts=3)
        assert exc_info.value.status_code == 500


def test_fetch_with_retry_does_not_retry_on_4xx():
    calls = {"count": 0}

    def handler(request):
        calls["count"] += 1
        return httpx.Response(400, json={"detail": "bad request"})

    with _client(handler) as client, pytest.raises(ApiError):
        fetch_with_retry(client, "/bad", attempts=3)
    assert calls["count"] == 1
