import pytest
from ex08_abc_ducks import MemoryStorage, PrefixedStorage, Storage, describe_quacker


def test_storage_cannot_be_instantiated_directly():
    with pytest.raises(TypeError):
        Storage()


def test_memory_storage_saves_and_loads():
    storage = MemoryStorage()
    storage.save("name", "Ada")
    assert storage.load("name") == "Ada"


def test_memory_storage_missing_key_returns_none():
    storage = MemoryStorage()
    assert storage.load("missing") is None


def test_memory_storage_instances_do_not_share_data():
    a = MemoryStorage()
    b = MemoryStorage()
    a.save("name", "Ada")
    assert b.load("name") is None


def test_prefixed_storage_delegates_with_prefix():
    inner = MemoryStorage()
    prefixed = PrefixedStorage(inner, "user:")
    prefixed.save("42", "Ada")
    assert inner.load("user:42") == "Ada"
    assert prefixed.load("42") == "Ada"


def test_prefixed_storage_missing_key_returns_none():
    prefixed = PrefixedStorage(MemoryStorage(), "user:")
    assert prefixed.load("99") is None


def test_prefixed_storage_can_wrap_any_storage_including_another_prefixed():
    innermost = MemoryStorage()
    once = PrefixedStorage(innermost, "a:")
    twice = PrefixedStorage(once, "b:")
    twice.save("1", "x")
    assert innermost.load("a:b:1") == "x"


class _Duck:
    def quack(self):
        return "quack!"


class _Dog:
    def bark(self):
        return "woof!"


class _Rock:
    pass


def test_describe_quacker_detects_quack():
    assert describe_quacker(_Duck()) == "quacks like a duck"


def test_describe_quacker_detects_bark():
    assert describe_quacker(_Dog()) == "barks like a dog"


def test_describe_quacker_falls_back_for_unknown_object():
    assert describe_quacker(_Rock()) == "a mystery creature"
