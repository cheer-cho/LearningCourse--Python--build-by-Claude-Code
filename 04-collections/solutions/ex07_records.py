def emails_of(users: list[dict]) -> list[str]:
    return [user["email"] for user in users]


def find_user(users: list[dict], name: str) -> dict | None:
    for user in users:
        if user["name"] == name:
            return user
    return None


def active_users(users: list[dict]) -> list[dict]:
    return [user for user in users if user["active"]]


def average_age(users: list[dict]) -> float:
    return sum(user["age"] for user in users) / len(users)
