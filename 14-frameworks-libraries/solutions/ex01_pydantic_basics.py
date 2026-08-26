from pydantic import BaseModel, Field, field_validator


class User(BaseModel):
    name: str
    email: str
    age: int = Field(ge=0)

    @field_validator("email")
    @classmethod
    def email_must_contain_at(cls, value: str) -> str:
        if "@" not in value:
            raise ValueError('email must contain "@"')
        return value


def parse_user(data: dict[str, object]) -> User:
    return User.model_validate(data)
