from ex07_tdd_bugfix import slugify


def test_lowercases():
    assert slugify("HELLO WORLD") == "hello-world"


def test_strips_punctuation():
    assert slugify("Hello, World!") == "hello-world"


def test_collapses_multiple_hyphens_and_spaces():
    assert slugify("Already--Slugged   Here") == "already-slugged-here"


def test_transliterates_unicode_accents():
    assert slugify("Café München") == "cafe-munchen"


def test_strips_leading_and_trailing_hyphens():
    assert slugify("  --Hello--  ") == "hello"


def test_handles_digits_and_mixed_punctuation():
    assert slugify("Python 3.12 Guide!") == "python-312-guide"
