def make_user(name, *, admin=False, active=True):
    return {"name": name, "admin": admin, "active": active}


def divide(a, b, /):
    return a / b
