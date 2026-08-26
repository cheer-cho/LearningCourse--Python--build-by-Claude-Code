from collections import Counter, defaultdict, deque


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    counts = Counter(text.split())
    ranked = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return ranked[:n]


def group_by_first_letter(names: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for name in names:
        groups[name[0]].append(name)
    return dict(groups)


class LastN:
    def __init__(self, n: int) -> None:
        self._items: deque[object] = deque(maxlen=n)

    def add(self, item: object) -> None:
        self._items.append(item)

    def items(self) -> list[object]:
        return list(self._items)
