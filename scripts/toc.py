"""Generate or refresh the table of contents in every LESSON.md.

    uv run python scripts/toc.py          -> rewrite TOCs in place
    uv run python scripts/toc.py --check  -> exit 1 if any TOC is stale

The TOC lives between `<!-- toc -->` and `<!-- /toc -->`, right under the
H1 title. It lists every `##` / `###` heading (outside code fences) as a
GitHub-style anchor link. Re-run after adding or renaming a section.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START, END = "<!-- toc -->", "<!-- /toc -->"
HEADING = re.compile(r"^(#{2,3}) (.+?)\s*$")
TOC_BLOCK = re.compile(rf"{re.escape(START)}.*?{re.escape(END)}\n*", re.DOTALL)


def slugify(title: str) -> str:
    """GitHub's anchor rule: lowercase, drop punctuation, spaces -> '-'."""
    text = re.sub(r"[^\w\- ]", "", title.lower())
    return text.replace(" ", "-")


def headings(markdown: str) -> list[tuple[int, str]]:
    found: list[tuple[int, str]] = []
    in_fence = False
    for line in markdown.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence and (m := HEADING.match(line)):
            found.append((len(m[1]), m[2]))
    return found


def build_toc(markdown: str) -> str:
    seen: Counter[str] = Counter()
    lines = [START, "**Contents**", ""]
    for level, title in headings(markdown):
        slug = slugify(title)
        anchor = f"{slug}-{seen[slug]}" if seen[slug] else slug
        seen[slug] += 1
        indent = "  " * (level - 2)
        lines.append(f"{indent}- [{title}](#{anchor})")
    lines.append(END)
    return "\n".join(lines) + "\n\n"


def with_toc(markdown: str) -> str:
    body = TOC_BLOCK.sub("", markdown)
    toc = build_toc(body)
    title, _, rest = body.partition("\n")
    return f"{title}\n\n{toc}{rest.lstrip(chr(10))}"


def main(argv: list[str]) -> int:
    check = "--check" in argv
    stale: list[Path] = []
    for path in sorted(ROOT.glob("[0-9][0-9]-*/LESSON.md")):
        old = path.read_text(encoding="utf-8")
        new = with_toc(old)
        if new != old:
            stale.append(path)
            if not check:
                path.write_text(new, encoding="utf-8")
    verb = "stale" if check else "updated"
    for path in stale:
        print(f"{verb}: {path.relative_to(ROOT)}")
    if not stale:
        print("all TOCs up to date")
    return 1 if check and stale else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
