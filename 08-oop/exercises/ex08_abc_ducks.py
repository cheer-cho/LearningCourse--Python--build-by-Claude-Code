# Scenario: a caching layer needs interchangeable storage backends, plus
# a quick duck-typing drill. Concepts: abc.ABC + @abstractmethod,
# composition (wrapping one object inside another), hasattr-based duck
# typing.
# Run: uv run pytest 08-oop -k ex08

from abc import ABC, abstractmethod


class Storage(ABC):
    """The contract every storage backend must implement. Given —
    nothing to fill in here; this defines the interface the two classes
    below must satisfy.
    """

    @abstractmethod
    def save(self, key, value): ...

    @abstractmethod
    def load(self, key): ...


class MemoryStorage(Storage):
    """A Storage backed by an in-memory dict."""

    def __init__(self):
        """Set up an empty backing dict."""
        raise NotImplementedError

    def save(self, key, value):
        """Store `value` under `key`."""
        raise NotImplementedError

    def load(self, key):
        """Return the value stored under `key`, or None if `key` was
        never saved.
        """
        raise NotImplementedError


class PrefixedStorage(Storage):
    """Wraps another Storage, prefixing every key before delegating —
    composition (an "is built from"), not inheriting from MemoryStorage.

    inner = MemoryStorage()
    prefixed = PrefixedStorage(inner, "user:")
    prefixed.save("42", "Ada")
    inner.load("user:42") -> "Ada"     # the real key has the prefix
    prefixed.load("42") -> "Ada"        # PrefixedStorage hides that detail
    """

    def __init__(self, storage, prefix):
        """Store the wrapped storage and the prefix to apply to keys."""
        raise NotImplementedError

    def save(self, key, value):
        """Save `value` under the prefixed key on the wrapped storage."""
        raise NotImplementedError

    def load(self, key):
        """Load the value for the prefixed key from the wrapped storage."""
        raise NotImplementedError


def describe_quacker(obj):
    """Duck-typing drill: describe `obj` by which methods it happens to
    have — check with hasattr, NEVER isinstance.

    - if obj has a "quack" method -> "quacks like a duck"
    - elif obj has a "bark" method -> "barks like a dog"
    - else -> "a mystery creature"
    """
    raise NotImplementedError
