from datetime import datetime

import pytest
from checkpoint_12 import Level, filter_entries, parse_line, report, run

SAMPLE_LINES = [
    "2026-08-26T09:00:00 INFO Server started",
    "2026-08-26T09:15:00 WARNING Disk usage high",
    "2026-08-26T10:00:00 ERROR Payment failed",
    "2026-08-26T10:05:00 ERROR Payment failed",
    "2026-08-26T10:10:00 ERROR Database timeout",
]


def _entries():
    return [parse_line(line) for line in SAMPLE_LINES]


def test_parse_line_typical():
    entry = parse_line("2026-08-26T10:00:00 ERROR Payment failed")
    assert entry == {
        "timestamp": datetime(2026, 8, 26, 10, 0, 0),  # noqa: DTZ001 — log lines carry no tz
        "level": Level.ERROR,
        "message": "Payment failed",
    }


def test_parse_line_raises_on_malformed_line():
    with pytest.raises(ValueError):
        parse_line("not a log line at all")


def test_parse_line_raises_on_unknown_level():
    with pytest.raises(ValueError):
        parse_line("2026-08-26T10:00:00 CRITICAL Meltdown")


def test_filter_entries_by_level():
    filtered = filter_entries(_entries(), level=Level.ERROR)
    assert len(filtered) == 3
    assert all(entry["level"] == Level.ERROR for entry in filtered)


def test_filter_entries_by_since():
    # Log timestamps are naive (no tz in the log format) — matches
    # parse_line's output, so comparing naive to naive here is correct.
    since = datetime(2026, 8, 26, 10, 0, 0)  # noqa: DTZ001
    filtered = filter_entries(_entries(), since=since)
    assert len(filtered) == 3
    assert all(entry["timestamp"] >= since for entry in filtered)


def test_filter_entries_by_level_and_since_combined():
    since = datetime(2026, 8, 26, 10, 5, 0)  # noqa: DTZ001
    filtered = filter_entries(_entries(), level=Level.ERROR, since=since)
    assert len(filtered) == 2


def test_filter_entries_no_filters_returns_everything():
    entries = _entries()
    assert filter_entries(entries) == entries


def test_report_counts_and_top_messages():
    text = report(_entries(), top=2)
    assert text == (
        "Total: 5\n"
        "INFO: 1  WARNING: 1  ERROR: 3\n"
        "Top messages:\n"
        "  Payment failed (2)\n"
        "  Database timeout (1)"
    )


def test_report_empty_entries():
    assert report([], top=3) == "Total: 0\nINFO: 0  WARNING: 0  ERROR: 0\nTop messages:"


def test_run_reads_file_and_filters_by_level(tmp_path):
    log_file = tmp_path / "app.log"
    log_file.write_text("\n".join(SAMPLE_LINES) + "\n")

    output = run([str(log_file), "--level", "ERROR", "--top", "1"])

    assert output == (
        "Total: 3\n"
        "INFO: 0  WARNING: 0  ERROR: 3\n"
        "Top messages:\n"
        "  Payment failed (2)"
    )


def test_run_reads_file_and_filters_by_since(tmp_path):
    log_file = tmp_path / "app.log"
    log_file.write_text("\n".join(SAMPLE_LINES) + "\n")

    output = run([str(log_file), "--since", "2026-08-26T10:00:00"])

    assert output.startswith("Total: 3\n")


def test_run_defaults_report_everything(tmp_path):
    log_file = tmp_path / "app.log"
    log_file.write_text("\n".join(SAMPLE_LINES) + "\n")

    output = run([str(log_file)])

    assert output.startswith("Total: 5\n")
    assert "INFO: 1  WARNING: 1  ERROR: 3" in output
