from ex03_dicts import add_contact, count_words, lookup


def test_add_contact_to_empty_book():
    assert add_contact({}, "Ada", "555-0100") == {"Ada": "555-0100"}


def test_add_contact_returns_the_same_dict():
    book = {"Ada": "555-0100"}
    result = add_contact(book, "Grace", "555-0200")
    assert result is book


def test_add_contact_overwrites_existing_number():
    book = {"Ada": "555-0100"}
    add_contact(book, "Ada", "555-9999")
    assert book == {"Ada": "555-9999"}


def test_lookup_found():
    assert lookup({"Ada": "555-0100"}, "Ada") == "555-0100"


def test_lookup_missing_returns_unknown():
    assert lookup({"Ada": "555-0100"}, "Grace") == "unknown"


def test_lookup_missing_does_not_raise():
    lookup({}, "Nobody")  # must not raise KeyError


def test_count_words_typical():
    assert count_words("a b a c b a") == {"a": 3, "b": 2, "c": 1}


def test_count_words_empty_text():
    assert count_words("") == {}


def test_count_words_single_word():
    assert count_words("hello") == {"hello": 1}


def test_count_words_is_case_sensitive():
    assert count_words("Cat cat") == {"Cat": 1, "cat": 1}
