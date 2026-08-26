from enum import Enum, auto


class Status(Enum):
    PENDING = auto()
    ACTIVE = auto()
    CLOSED = auto()


def from_label(text: str) -> Status:
    try:
        return Status[text.upper()]
    except KeyError:
        raise ValueError(f"unknown status: {text!r}") from None


def next_status(s: Status) -> Status:
    match s:
        case Status.PENDING:
            return Status.ACTIVE
        case Status.ACTIVE:
            return Status.CLOSED
        case Status.CLOSED:
            return Status.CLOSED


def is_terminal(s: Status) -> bool:
    return s is Status.CLOSED
