_SHIFT = 3


def _shift_char(char: str, amount: int) -> str:
    if "a" <= char <= "z":
        return chr((ord(char) - ord("a") + amount) % 26 + ord("a"))
    if "A" <= char <= "Z":
        return chr((ord(char) - ord("A") + amount) % 26 + ord("A"))
    return char


def encode(text: str) -> str:
    return "".join(_shift_char(char, _SHIFT) for char in text)


def decode(data: str) -> str:
    return "".join(_shift_char(char, -_SHIFT) for char in data)


def prop_roundtrip(text: str) -> bool:
    return decode(encode(text)) == text


def prop_length_nonneg(text: str) -> bool:
    return len(encode(text)) == len(text) >= 0
