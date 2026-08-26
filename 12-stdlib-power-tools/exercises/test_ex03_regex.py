import pytest
from ex03_regex import extract_emails, parse_log_line, redact_phones


def test_extract_emails_finds_multiple_in_order():
    text = "contact ada@example.com or bo@x.co for help"
    assert extract_emails(text) == ["ada@example.com", "bo@x.co"]


def test_extract_emails_no_matches_returns_empty_list():
    assert extract_emails("no emails here") == []


def test_extract_emails_handles_plus_and_dots():
    text = "reach us at first.last+tag@sub.example.com"
    assert extract_emails(text) == ["first.last+tag@sub.example.com"]


def test_redact_phones_replaces_dash_separated():
    assert redact_phones("Call 555-123-4567 now") == "Call ***-***-**** now"


def test_redact_phones_replaces_multiple():
    text = "555-123-4567 and 555.987.6543"
    assert redact_phones(text) == "***-***-**** and ***-***-****"


def test_redact_phones_leaves_non_phone_numbers_alone():
    assert redact_phones("order #12345 shipped") == "order #12345 shipped"


def test_parse_log_line_typical():
    line = "2026-08-26T10:00:00 ERROR Payment failed"
    assert parse_log_line(line) == {
        "timestamp": "2026-08-26T10:00:00",
        "level": "ERROR",
        "message": "Payment failed",
    }


def test_parse_log_line_info_level():
    line = "2026-08-26T09:30:00 INFO Server started"
    assert parse_log_line(line) == {
        "timestamp": "2026-08-26T09:30:00",
        "level": "INFO",
        "message": "Server started",
    }


def test_parse_log_line_raises_on_malformed_line():
    with pytest.raises(ValueError):
        parse_log_line("this is not a log line")
