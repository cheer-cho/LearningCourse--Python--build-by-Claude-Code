import re

import pytest
from ex04_dependency_injection import FakeProvider, WeatherReport


def test_fake_provider_returns_canned_response():
    fake = FakeProvider({"NYC": {"temp_c": 10}})
    assert fake("NYC") == {"temp_c": 10}


def test_fake_provider_returns_none_for_unknown_city():
    fake = FakeProvider({"NYC": {"temp_c": 10}})
    assert fake("LA") is None


def test_fake_provider_records_calls_in_order():
    fake = FakeProvider({"NYC": {"temp_c": 10}, "LA": {"temp_c": 20}})
    fake("NYC")
    fake("LA")
    fake("NYC")
    assert fake.calls == ["NYC", "LA", "NYC"]


def test_weather_report_uses_injected_provider_not_live_one():
    fake = FakeProvider({"NYC": {"temp_c": 10}})
    report = WeatherReport(provider=fake)
    assert report.summary("NYC") == "NYC: 10C"
    assert fake.calls == ["NYC"]


def test_weather_report_success_path_with_different_temp():
    fake = FakeProvider({"SF": {"temp_c": -3}})
    report = WeatherReport(provider=fake)
    assert report.summary("SF") == "SF: -3C"


def test_weather_report_raises_on_missing_city():
    fake = FakeProvider({"NYC": {"temp_c": 10}})
    report = WeatherReport(provider=fake)
    with pytest.raises(ValueError, match="LA"):
        report.summary("LA")


def test_weather_report_with_no_provider_arg_still_works():
    # No fake injected here — this proves the default provider is wired
    # up end-to-end, without asserting on WeatherReport's internals.
    report = WeatherReport()
    assert re.fullmatch(r"[A-Za-z ]+: -?\d+C", report.summary("Testville"))
