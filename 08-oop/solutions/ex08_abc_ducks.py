from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def save(self, key, value): ...

    @abstractmethod
    def load(self, key): ...


class MemoryStorage(Storage):
    def __init__(self):
        self._data = {}

    def save(self, key, value):
        self._data[key] = value

    def load(self, key):
        return self._data.get(key)


class PrefixedStorage(Storage):
    def __init__(self, storage, prefix):
        self._storage = storage
        self._prefix = prefix

    def save(self, key, value):
        self._storage.save(self._prefix + key, value)

    def load(self, key):
        return self._storage.load(self._prefix + key)


def describe_quacker(obj):
    if hasattr(obj, "quack"):
        return "quacks like a duck"
    elif hasattr(obj, "bark"):
        return "barks like a dog"
    else:
        return "a mystery creature"
