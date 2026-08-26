# Scenario: validate incoming signup data at runtime before it touches
# the rest of the app. Concepts: pydantic BaseModel, Field constraints,
# field_validator, ValidationError.
# Run: uv run pytest 14-frameworks-libraries -k ex01

from __future__ import annotations

from pydantic import BaseModel, Field, field_validator


class User(BaseModel):
    """A signed-up user.

    `age` must be >= 0 (enforced by `Field`). `email` must contain an
    "@" (enforced by a field_validator) — this module skips pydantic's
    built-in `EmailStr` on purpose so the validator itself is the lesson.
    """

    name: str
    email: str
    age: int = Field(ge=0)

    @field_validator("email")
    @classmethod
    def email_must_contain_at(cls, value: str) -> str:
        """Reject an email with no "@" in it; otherwise pass it through."""
        if "@" not in value:
            raise ValueError('email must contain "@"')
        return value


def parse_user(data: dict[str, object]) -> User:
    """Parse a raw dict into a `User`.

    Raises `pydantic.ValidationError` if `data` fails any constraint
    (missing field, negative age, email without "@", wrong types).

    parse_user({"name": "Ada", "email": "ada@x.com", "age": 30})
        -> User(name="Ada", email="ada@x.com", age=30)
    parse_user({"name": "Bo", "email": "bad", "age": 5}) -> raises ValidationError
    """
    raise NotImplementedError
