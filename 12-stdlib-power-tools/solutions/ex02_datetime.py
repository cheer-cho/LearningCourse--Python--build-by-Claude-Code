from datetime import UTC, date, datetime
from zoneinfo import ZoneInfo


def parse_iso_date(text: str) -> date:
    return date.fromisoformat(text)


def days_between(a: date, b: date) -> int:
    return (b - a).days


def format_friendly(dt: date) -> str:
    return dt.strftime("%a %d %b %Y")


def to_utc(dt_string: str, tz: str) -> datetime:
    # strptime always returns a naive datetime; attach the source zone
    # explicitly with .replace(tzinfo=...) before converting to UTC.
    naive = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")  # noqa: DTZ007
    local = naive.replace(tzinfo=ZoneInfo(tz))
    return local.astimezone(UTC)
