import pytest
from ex03_parametrize_cases import STRENGTH_CASES, password_strength


@pytest.mark.parametrize(
    "pw, expected",
    STRENGTH_CASES,
    ids=[f"case{i}" for i in range(len(STRENGTH_CASES))],
)
def test_strength_case_matches_password_strength(pw, expected):
    assert password_strength(pw) == expected


def test_case_table_covers_empty():
    assert any(pw == "" for pw, _ in STRENGTH_CASES)


def test_case_table_covers_too_short():
    assert any(0 < len(pw) < 8 for pw, _ in STRENGTH_CASES)


def test_case_table_covers_no_digit():
    assert any(
        len(pw) >= 8 and not any(ch.isdigit() for ch in pw) for pw, _ in STRENGTH_CASES
    )


def test_case_table_covers_strong():
    assert any(
        len(pw) >= 8 and any(ch.isdigit() for ch in pw) for pw, _ in STRENGTH_CASES
    )


def test_case_table_covers_unicode():
    assert any(any(ord(ch) > 127 for ch in pw) for pw, _ in STRENGTH_CASES)


def test_case_table_has_enough_cases():
    # Five categories above, at least one dedicated case each (some may
    # double up, but five one-purpose cases is the honest minimum).
    assert len(STRENGTH_CASES) >= 5
