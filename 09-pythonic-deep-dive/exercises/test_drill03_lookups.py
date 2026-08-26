import inspect
import re

import pytest
from drill03_lookups import group_words_by_letter, price_or_default, required_setting, tally_word

REWRITTEN = [price_or_default, tally_word, group_words_by_letter, required_setting]


def test_price_or_default_found():
    assert price_or_default({"apple": 2}, "apple") == 2


def test_price_or_default_missing():
    assert price_or_default({"apple": 2}, "banana") == 0


def test_tally_word_first_time():
    assert tally_word({}, "hi") == {"hi": 1}


def test_tally_word_repeat():
    assert tally_word({"hi": 1}, "hi") == {"hi": 2}


def test_group_words_by_letter_creates_bucket():
    assert group_words_by_letter({}, "cat") == {"c": ["cat"]}


def test_group_words_by_letter_appends_to_bucket():
    assert group_words_by_letter({"c": ["cat"]}, "car") == {"c": ["cat", "car"]}


def test_required_setting_present():
    assert required_setting({"host": "x"}, "host") == "x"


def test_required_setting_missing_raises_key_error():
    with pytest.raises(KeyError):
        required_setting({}, "host")


def test_rewrites_avoid_an_if_statement():
    for func in REWRITTEN:
        source = inspect.getsource(func)
        assert re.search(r"\bif\b", source) is None, (
            f"{func.__name__} still uses `if` instead of .get/.setdefault/try-except"
        )
