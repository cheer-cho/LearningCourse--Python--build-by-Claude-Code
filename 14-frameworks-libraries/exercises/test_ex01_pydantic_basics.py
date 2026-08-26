import pytest

pytest.importorskip("pydantic")

from ex01_pydantic_basics import User, parse_user
from pydantic import ValidationError


def test_parse_user_valid_returns_user():
    user = parse_user({"name": "Ada", "email": "ada@x.com", "age": 30})
    assert user == User(name="Ada", email="ada@x.com", age=30)


def test_parse_user_invalid_email_raises():
    with pytest.raises(ValidationError) as exc_info:
        parse_user({"name": "Bo", "email": "bad", "age": 5})
    errors = exc_info.value.errors()
    assert any(e["loc"] == ("email",) for e in errors)


def test_parse_user_negative_age_raises():
    with pytest.raises(ValidationError) as exc_info:
        parse_user({"name": "Cy", "email": "cy@x.com", "age": -1})
    errors = exc_info.value.errors()
    assert any(e["loc"] == ("age",) for e in errors)


def test_parse_user_missing_field_raises():
    with pytest.raises(ValidationError) as exc_info:
        parse_user({"name": "Dee", "email": "dee@x.com"})
    errors = exc_info.value.errors()
    assert any(e["loc"] == ("age",) and e["type"] == "missing" for e in errors)


def test_parse_user_wrong_type_raises():
    with pytest.raises(ValidationError):
        parse_user({"name": "Eve", "email": "eve@x.com", "age": "old"})
