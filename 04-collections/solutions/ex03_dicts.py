def add_contact(phonebook: dict[str, str], name: str, number: str) -> dict[str, str]:
    phonebook[name] = number
    return phonebook


def lookup(phonebook: dict[str, str], name: str) -> str:
    return phonebook.get(name, "unknown")


def count_words(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts
