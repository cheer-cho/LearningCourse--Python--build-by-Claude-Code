# Scenario: a reversible text transform, tested by stating properties
# it must always hold instead of listing individual examples.
# Concepts: property-based testing, reversibility, predicates that
# hypothesis feeds generated inputs through.
# Run: uv run pytest 13-testing-quality -k ex06


def encode(text: str) -> str:
    """Caesar-shift every ASCII letter in `text` forward by 3 places in
    the alphabet, preserving case and wrapping past 'z'/'Z'. Every
    other character (digits, punctuation, spaces, non-ASCII characters)
    passes through completely unchanged.

    encode("abc") -> "def"
    encode("XYZ") -> "ABC"        (wraps around)
    encode("a1!☃") -> "d1!☃"      (non-letters untouched)
    """
    raise NotImplementedError


def decode(data: str) -> str:
    """Undo `encode`: shift every ASCII letter in `data` back by 3
    places, wrapping past 'a'/'A'. Everything `encode` leaves alone,
    `decode` also leaves alone.

    decode("def") -> "abc"
    decode(encode(text)) -> text   for any string `text`
    """
    raise NotImplementedError


def prop_roundtrip(text: str) -> bool:
    """Property: encoding then decoding any string returns the
    original string exactly. Return whether this holds for `text`.

    prop_roundtrip("hello") -> True
    """
    raise NotImplementedError


def prop_length_nonneg(text: str) -> bool:
    """Property: `encode` never changes the length of the string (it's
    a character-by-character substitution). Return whether the encoded
    text has a non-negative length equal to `len(text)`.

    prop_length_nonneg("hello") -> True
    prop_length_nonneg("") -> True
    """
    raise NotImplementedError
