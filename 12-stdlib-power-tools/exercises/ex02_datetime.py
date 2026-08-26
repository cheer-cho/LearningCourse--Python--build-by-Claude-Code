# Scenario: parsing and formatting dates the way a small booking app
# would — ISO strings in, friendly strings out, and converting a local
# wall-clock time to UTC for storage. Concepts: date/datetime parsing,
# timedelta math, zoneinfo (aware datetimes).
# Run: uv run pytest 12-stdlib-power-tools -k ex02

from datetime import date, datetime


def parse_iso_date(text: str) -> date:
    """Parse an ISO 8601 date string ("YYYY-MM-DD") into a date object.

    parse_iso_date("2026-08-26") -> date(2026, 8, 26)
    """
    raise NotImplementedError


def days_between(a: date, b: date) -> int:
    """Return the number of days from date `a` to date `b` (b - a).
    Negative when `b` is earlier than `a`.

    days_between(date(2026, 8, 1), date(2026, 8, 26)) -> 25
    days_between(date(2026, 8, 26), date(2026, 8, 1)) -> -25
    """
    raise NotImplementedError


def format_friendly(dt: date) -> str:
    """Format a date (or datetime) as "Wed 26 Aug 2026": three-letter
    weekday, zero-padded day, three-letter month, four-digit year.

    format_friendly(date(2026, 8, 26)) -> "Wed 26 Aug 2026"
    """
    raise NotImplementedError


def to_utc(dt_string: str, tz: str) -> datetime:
    """Interpret `dt_string` ("YYYY-MM-DD HH:MM:SS") as naive wall-clock
    time in the IANA zone `tz` (e.g. "UTC", "Europe/Paris",
    "Asia/Bangkok"), then convert it to an aware UTC datetime. Use
    zoneinfo.ZoneInfo — never hardcode an offset, since it must account
    for daylight saving.

    to_utc("2026-08-26 10:00:00", "Europe/Paris")
        -> datetime(2026, 8, 26, 8, 0, tzinfo=<UTC>)  (Paris is UTC+2 in August)
    """
    raise NotImplementedError
