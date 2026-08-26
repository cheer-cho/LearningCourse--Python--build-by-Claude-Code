from datetime import UTC, date, datetime

from ex02_datetime import days_between, format_friendly, parse_iso_date, to_utc


def test_parse_iso_date_typical():
    assert parse_iso_date("2026-08-26") == date(2026, 8, 26)


def test_parse_iso_date_new_year():
    assert parse_iso_date("2026-01-01") == date(2026, 1, 1)


def test_days_between_positive():
    assert days_between(date(2026, 8, 1), date(2026, 8, 26)) == 25


def test_days_between_negative_when_b_earlier():
    assert days_between(date(2026, 8, 26), date(2026, 8, 1)) == -25


def test_days_between_same_day_is_zero():
    assert days_between(date(2026, 8, 26), date(2026, 8, 26)) == 0


def test_format_friendly_known_date():
    assert format_friendly(date(2026, 8, 26)) == "Wed 26 Aug 2026"


def test_format_friendly_different_month():
    assert format_friendly(date(2026, 1, 1)) == "Thu 01 Jan 2026"


def test_to_utc_from_utc_is_unchanged():
    result = to_utc("2026-08-26 10:00:00", "UTC")
    assert result == datetime(2026, 8, 26, 10, 0, 0, tzinfo=UTC)


def test_to_utc_from_paris_subtracts_dst_offset():
    result = to_utc("2026-08-26 10:00:00", "Europe/Paris")
    assert result == datetime(2026, 8, 26, 8, 0, 0, tzinfo=UTC)


def test_to_utc_from_bangkok_subtracts_seven_hours():
    result = to_utc("2026-08-26 10:00:00", "Asia/Bangkok")
    assert result == datetime(2026, 8, 26, 3, 0, 0, tzinfo=UTC)


def test_to_utc_result_is_aware():
    result = to_utc("2026-08-26 10:00:00", "UTC")
    assert result.tzinfo is not None
