import argparse
import re
from collections import Counter
from datetime import datetime
from enum import Enum


class Level(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


_LOG_LINE_RE = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>[A-Z]+)\s+"
    r"(?P<message>.+)"
)


def parse_line(line: str) -> dict[str, object]:
    match = _LOG_LINE_RE.match(line.strip())
    if match is None:
        raise ValueError(f"malformed log line: {line!r}")
    try:
        level = Level(match["level"])
    except ValueError:
        raise ValueError(f"unknown level: {match['level']!r}") from None
    return {
        "timestamp": datetime.fromisoformat(match["timestamp"]),
        "level": level,
        "message": match["message"],
    }


def filter_entries(
    entries: list[dict[str, object]],
    *,
    level: Level | None = None,
    since: datetime | None = None,
) -> list[dict[str, object]]:
    result = entries
    if level is not None:
        result = [entry for entry in result if entry["level"] == level]
    if since is not None:
        result = [entry for entry in result if entry["timestamp"] >= since]  # type: ignore[operator]
    return result


def report(entries: list[dict[str, object]], top: int = 3) -> str:
    total = len(entries)
    level_counts = Counter(entry["level"] for entry in entries)
    message_counts = Counter(entry["message"] for entry in entries)
    top_messages = sorted(message_counts.items(), key=lambda pair: (-pair[1], pair[0]))[:top]

    level_line = (
        f"INFO: {level_counts.get(Level.INFO, 0)}  "
        f"WARNING: {level_counts.get(Level.WARNING, 0)}  "
        f"ERROR: {level_counts.get(Level.ERROR, 0)}"
    )
    lines = [f"Total: {total}", level_line, "Top messages:"]
    lines.extend(f"  {message} ({count})" for message, count in top_messages)
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="loganalyzer")
    parser.add_argument("path")
    parser.add_argument("--level", choices=[lvl.value for lvl in Level], default=None)
    parser.add_argument("--since", default=None)
    parser.add_argument("--top", type=int, default=3)
    return parser


def run(argv: list[str]) -> str:
    args = build_parser().parse_args(argv)
    with open(args.path, encoding="utf-8") as f:
        lines = [line for line in f.read().splitlines() if line.strip()]
    entries = [parse_line(line) for line in lines]

    level = Level(args.level) if args.level else None
    since = datetime.fromisoformat(args.since) if args.since else None
    filtered = filter_entries(entries, level=level, since=since)
    return report(filtered, top=args.top)
