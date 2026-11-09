# Scenario: a tiny user database represented as a list of dicts
# ("records") — the shape you'll see everywhere once you start reading
# JSON. Concepts: iterating lists of dicts, comprehensions over records,
# loop + early return.
# Run: uv run pytest 04-collections -k ex07

# Each user record looks like:
# {"name": "Ada", "email": "ada@example.com", "age": 36, "active": True}


def emails_of(users: list[dict]) -> list[str]:
    """Return the "email" of every user in `users`, in order.

    emails_of([{"email": "a@x.com"}, {"email": "b@x.com"}])
        -> ["a@x.com", "b@x.com"]
    """
    return [user["email"] for user in users]


def find_user(users: list[dict], name: str) -> dict | None:
    """Return the first user record whose "name" equals `name`, or None
    if no user matches. Loop over `users` and return as soon as you find
    a match — don't scan the rest.

    find_user([{"name": "Ada"}, {"name": "Grace"}], "Grace") -> {"name": "Grace"}
    find_user([{"name": "Ada"}], "Nobody") -> None
    """
    for user in users:
        if user.get("name") == name:
            return user

    return None


def active_users(users: list[dict]) -> list[dict]:
    """Return the records where "active" is True, in original order.

    active_users([{"name": "Ada", "active": True}, {"name": "Bo", "active": False}])
        -> [{"name": "Ada", "active": True}]
    """
    return [user for user in users if user["active"]]


def average_age(users: list[dict]) -> float:
    """Return the mean "age" across all `users`. `users` has at least
    one record.

    average_age([{"age": 30}, {"age": 40}]) -> 35.0
    """
    
    return sum(user["age"] for user in users) / len(users)
