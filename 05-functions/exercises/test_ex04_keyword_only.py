import pytest
from ex04_keyword_only import divide, make_user


def test_make_user_defaults():
    assert make_user("Ada") == {"name": "Ada", "admin": False, "active": True}


def test_make_user_with_admin_keyword():
    assert make_user("Bo", admin=True) == {"name": "Bo", "admin": True, "active": True}


def test_make_user_with_both_keywords():
    result = make_user("Cy", admin=True, active=False)
    assert result == {"name": "Cy", "admin": True, "active": False}


def test_make_user_rejects_positional_admin():
    with pytest.raises(TypeError):
        make_user("Cy", True)


def test_divide_typical():
    assert divide(6, 3) == 2.0


def test_divide_returns_float():
    assert divide(9, 2) == 4.5


def test_divide_rejects_keyword_arguments():
    with pytest.raises(TypeError):
        divide(a=6, b=3)
