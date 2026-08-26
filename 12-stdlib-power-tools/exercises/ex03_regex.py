# Scenario: cleaning up messy free-text support tickets — pulling out
# email addresses, redacting phone numbers before storage, and parsing a
# structured log line. Concepts: raw strings, re.findall/sub/match,
# named groups.
# Run: uv run pytest 12-stdlib-power-tools -k ex03

import re  # noqa: F401 — needed once functions are implemented


def extract_emails(text: str) -> list[str]:
    """Return every email address found in `text`, in the order they
    appear. An email looks like local-part@domain (letters, digits,
    dots, plus, hyphen, underscore in the local part; letters, digits,
    dots, hyphens in the domain).

    extract_emails("contact ada@example.com or bo@x.co") ->
        ["ada@example.com", "bo@x.co"]
    """
    raise NotImplementedError


def redact_phones(text: str) -> str:
    """Replace every phone number of the shape "555-123-4567" (digits
    grouped 3-3-4, separated by "-", "." or a space) with
    "***-***-****". Everything else in `text` is unchanged.

    redact_phones("Call 555-123-4567 now") -> "Call ***-***-**** now"
    """
    raise NotImplementedError


def parse_log_line(line: str) -> dict[str, str]:
    """Parse a log line shaped like
    "2026-08-26T10:00:00 ERROR Payment failed" into
    {"timestamp": "2026-08-26T10:00:00", "level": "ERROR",
     "message": "Payment failed"} using NAMED regex groups.

    Raises ValueError if `line` doesn't match the expected shape.

    parse_log_line("2026-08-26T10:00:00 ERROR Payment failed") ->
        {"timestamp": "2026-08-26T10:00:00", "level": "ERROR", "message": "Payment failed"}
    """
    raise NotImplementedError
