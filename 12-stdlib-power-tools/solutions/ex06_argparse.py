import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="notes")
    parser.add_argument("action", choices=["add", "list"])
    parser.add_argument("text", nargs="?", default="")
    parser.add_argument("--tag", action="append", default=None)
    parser.add_argument("--limit", type=int, default=10)
    return parser


def _add_note(notes: list[dict[str, object]], text: str, tags: list[str]) -> str:
    notes.append({"text": text, "tags": tags})
    return f"Added: {text}"


def _list_notes(notes: list[dict[str, object]], limit: int) -> str:
    if not notes:
        return "No notes."
    lines = []
    for note in notes[:limit]:
        tags: list[str] = note["tags"]  # type: ignore[assignment]
        lines.append(f"{note['text']} [{','.join(tags)}]")
    return "\n".join(lines)


def run(argv: list[str], notes: list[dict[str, object]] | None = None) -> str:
    if notes is None:
        notes = []
    args = build_parser().parse_args(argv)
    if args.action == "add":
        return _add_note(notes, args.text, args.tag or [])
    return _list_notes(notes, args.limit)
