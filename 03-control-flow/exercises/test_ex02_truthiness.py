from ex02_truthiness import describe, first_truthy


def test_first_truthy_finds_first_when_a_falsy():
    assert first_truthy(0, "", "hi") == "hi"


def test_first_truthy_finds_a_when_truthy():
    assert first_truthy("x", "y", "z") == "x"


def test_first_truthy_finds_middle():
    assert first_truthy(None, 5, "z") == 5


def test_first_truthy_all_falsy_returns_none():
    assert first_truthy(None, 0, False) is None


def test_first_truthy_falsy_zero_is_not_chosen():
    assert first_truthy(0, 0.0, "last") == "last"


def test_describe_none_is_missing():
    assert describe(None) == "missing"


def test_describe_empty_string_is_empty():
    assert describe("") == "empty"


def test_describe_zero_is_present():
    assert describe(0) == "present"


def test_describe_false_is_present():
    assert describe(False) == "present"


def test_describe_word_is_present():
    assert describe("hi") == "present"
