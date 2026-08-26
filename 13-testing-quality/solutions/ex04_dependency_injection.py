import random
import time
from collections.abc import Callable


def live_provider(city: str) -> dict[str, object] | None:
    time.sleep(0.01)
    return {"city": city, "temp_c": random.randint(-10, 40)}


class WeatherReport:
    def __init__(
        self, provider: Callable[[str], dict[str, object] | None] = live_provider
    ) -> None:
        self._provider = provider

    def summary(self, city: str) -> str:
        data = self._provider(city)
        if data is None:
            raise ValueError(f"no data for {city}")
        return f"{city}: {data['temp_c']}C"


class FakeProvider:
    def __init__(self, responses: dict[str, dict[str, object] | None]) -> None:
        self._responses = responses
        self.calls: list[str] = []

    def __call__(self, city: str) -> dict[str, object] | None:
        self.calls.append(city)
        return self._responses.get(city)
