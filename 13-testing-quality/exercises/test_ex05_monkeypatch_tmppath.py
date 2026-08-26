import pytest
from ex05_monkeypatch_tmppath import cache_result, cached, read_api_key


def test_read_api_key_returns_env_value(monkeypatch):
    monkeypatch.setenv("API_KEY", "abc123")
    assert read_api_key() == "abc123"


def test_read_api_key_raises_when_unset(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="API_KEY is not set"):
        read_api_key()


def test_read_api_key_raises_when_empty(monkeypatch):
    monkeypatch.setenv("API_KEY", "")
    with pytest.raises(RuntimeError, match="API_KEY is not set"):
        read_api_key()


def test_cache_result_writes_a_retrievable_value(tmp_path):
    path = tmp_path / "cache.json"
    cache_result(path, "pi", "3.14")
    assert cached(path, "pi") == "3.14"


def test_cache_result_creates_the_file_if_missing(tmp_path):
    path = tmp_path / "brand_new.json"
    assert not path.exists()
    cache_result(path, "greeting", "hi")
    assert path.exists()


def test_cache_result_merges_instead_of_overwriting(tmp_path):
    path = tmp_path / "cache.json"
    cache_result(path, "pi", "3.14")
    cache_result(path, "e", "2.71")
    assert cached(path, "pi") == "3.14"
    assert cached(path, "e") == "2.71"


def test_cache_result_overwrites_same_key(tmp_path):
    path = tmp_path / "cache.json"
    cache_result(path, "pi", "3.14")
    cache_result(path, "pi", "3.14159")
    assert cached(path, "pi") == "3.14159"


def test_cached_returns_none_for_missing_file(tmp_path):
    assert cached(tmp_path / "nope.json", "pi") is None


def test_cached_returns_none_for_missing_key(tmp_path):
    path = tmp_path / "cache.json"
    cache_result(path, "pi", "3.14")
    assert cached(path, "missing") is None
