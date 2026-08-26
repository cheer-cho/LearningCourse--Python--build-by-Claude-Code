from ex07_records import active_users, average_age, emails_of, find_user


def test_emails_of_typical():
    users = [{"email": "a@x.com"}, {"email": "b@x.com"}]
    assert emails_of(users) == ["a@x.com", "b@x.com"]


def test_emails_of_empty_list():
    assert emails_of([]) == []


def test_find_user_found():
    users = [{"name": "Ada"}, {"name": "Grace"}]
    assert find_user(users, "Grace") == {"name": "Grace"}


def test_find_user_returns_first_match():
    users = [{"name": "Ada", "age": 1}, {"name": "Ada", "age": 2}]
    assert find_user(users, "Ada") == {"name": "Ada", "age": 1}


def test_find_user_not_found_returns_none():
    users = [{"name": "Ada"}]
    assert find_user(users, "Nobody") is None


def test_active_users_filters_and_preserves_order():
    users = [
        {"name": "Ada", "active": True},
        {"name": "Bo", "active": False},
        {"name": "Cy", "active": True},
    ]
    assert active_users(users) == [
        {"name": "Ada", "active": True},
        {"name": "Cy", "active": True},
    ]


def test_active_users_none_active():
    users = [{"name": "Bo", "active": False}]
    assert active_users(users) == []


def test_average_age_typical():
    assert average_age([{"age": 30}, {"age": 40}]) == 35.0


def test_average_age_single_user():
    assert average_age([{"age": 21}]) == 21.0
