# Scenario: a weather report is hard-wired to a slow, nondeterministic
# network call, which makes it untestable. Concepts: dependency
# injection, refactoring for testability, the fake test double.
# Run: uv run pytest 13-testing-quality -k ex04

import random
import time
from collections.abc import Callable


def live_provider(city: str) -> dict[str, object] | None:
    """A stand-in for a real network call: slow, and returns a random
    temperature every time. Given — never call this from a test.

    live_provider("NYC") -> {"city": "NYC", "temp_c": <random int>}
    """
    time.sleep(0.01)
    return {"city": city, "temp_c": random.randint(-10, 40)}


class WeatherReport:
    """Formats a one-line weather summary for a city.

    As given, this class would call `live_provider` directly, which
    makes it slow and nondeterministic to test. Implement it with
    dependency injection instead: `__init__` accepts a `provider`
    callable (defaulting to `live_provider` for real use), stores it,
    and `summary` calls `self._provider` — never `live_provider` by
    name. That's what lets a test swap in `FakeProvider` below.
    """

    def __init__(self, provider: Callable[[str], dict[str, object] | None] = live_provider) -> None:
        raise NotImplementedError

    def summary(self, city: str) -> str:
        """Return `"<city>: <temp_c>C"` using whatever provider was
        injected. If the provider returns `None` for `city` (a lookup
        miss), raise `ValueError(f"no data for {city}")`.

        report = WeatherReport(provider=some_fake)
        report.summary("NYC") -> "NYC: 10C"   (if the provider returns {"temp_c": 10} for "NYC")
        """
        raise NotImplementedError


class FakeProvider:
    """Test double for `WeatherReport`: returns canned responses instead
    of calling the network, and records every city it was asked about
    so a test can prove the injected provider was actually used.

    responses: maps city name -> canned provider output, or `None` to
    simulate "not found".
    calls: starts empty; append each requested city, in call order.

    fake = FakeProvider({"NYC": {"temp_c": 10}})
    fake("NYC") -> {"temp_c": 10}
    fake.calls -> ["NYC"]
    fake("LA") -> None          # "LA" not in responses
    """

    def __init__(self, responses: dict[str, dict[str, object] | None]) -> None:
        raise NotImplementedError

    def __call__(self, city: str) -> dict[str, object] | None:
        raise NotImplementedError
