import json


class ContactError(Exception):
    """Raised for any problem loading, saving, or modifying contacts."""


def load_contacts(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        return {}
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        raise ContactError(f"corrupt contacts file: {path}") from e


def save_contacts(path, contacts):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2)


def add_contact(path, name, email):
    contacts = load_contacts(path)
    if name in contacts:
        raise ContactError(f"contact already exists: {name}")
    contacts[name] = email
    save_contacts(path, contacts)
