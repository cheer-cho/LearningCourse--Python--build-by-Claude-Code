import re

_EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
_PHONE_RE = re.compile(r"\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b")
_LOG_LINE_RE = re.compile(
    r"(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>[A-Z]+)\s+"
    r"(?P<message>.+)"
)


def extract_emails(text: str) -> list[str]:
    return _EMAIL_RE.findall(text)


def redact_phones(text: str) -> str:
    return _PHONE_RE.sub("***-***-****", text)


def parse_log_line(line: str) -> dict[str, str]:
    match = _LOG_LINE_RE.match(line.strip())
    if match is None:
        raise ValueError(f"malformed log line: {line!r}")
    return {
        "timestamp": match["timestamp"],
        "level": match["level"],
        "message": match["message"],
    }
