from ex06_properties import decode, encode, prop_length_nonneg, prop_roundtrip
from hypothesis import given, settings
from hypothesis import strategies as st

# Bounded on purpose: max_examples caps runtime, deadline=None avoids
# flaky timing failures on a loaded CI box, and st.text() is a fully
# deterministic strategy (no wall-clock/real randomness involved).
_settings = settings(max_examples=50, deadline=None)


def test_encode_shifts_lowercase_letters():
    assert encode("abc") == "def"


def test_encode_wraps_uppercase_past_z():
    assert encode("XYZ") == "ABC"


def test_encode_leaves_non_letters_untouched():
    assert encode("a1!") == "d1!"


def test_decode_undoes_a_known_encoding():
    assert decode("def") == "abc"


@_settings
@given(st.text(min_size=0, max_size=40))
def test_prop_roundtrip_holds_for_generated_text(text):
    assert prop_roundtrip(text) is True


@_settings
@given(st.text(min_size=0, max_size=40))
def test_prop_length_nonneg_holds_for_generated_text(text):
    assert prop_length_nonneg(text) is True


@_settings
@given(st.text(min_size=0, max_size=40))
def test_decode_of_encode_matches_original(text):
    assert decode(encode(text)) == text
