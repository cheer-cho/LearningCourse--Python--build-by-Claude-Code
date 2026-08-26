import json

import pytest
from checkpoint_06 import ContactError, add_contact, load_contacts, save_contacts


def test_load_contacts_missing_file_returns_empty_dict(tmp_path):
    path = tmp_path / "contacts.json"
    assert load_contacts(path) == {}


def test_load_contacts_reads_existing_file(tmp_path):
    path = tmp_path / "contacts.json"
    path.write_text('{"Ada": "ada@x.com"}', encoding="utf-8")
    assert load_contacts(path) == {"Ada": "ada@x.com"}


def test_load_contacts_corrupt_json_raises_contact_error(tmp_path):
    path = tmp_path / "contacts.json"
    path.write_text("not json", encoding="utf-8")
    with pytest.raises(ContactError):
        load_contacts(path)


def test_load_contacts_corrupt_json_chains_json_decode_error(tmp_path):
    path = tmp_path / "contacts.json"
    path.write_text("not json", encoding="utf-8")
    with pytest.raises(ContactError) as excinfo:
        load_contacts(path)
    assert isinstance(excinfo.value.__cause__, json.JSONDecodeError)


def test_save_contacts_writes_json(tmp_path):
    path = tmp_path / "contacts.json"
    save_contacts(path, {"Ada": "ada@x.com"})
    assert json.loads(path.read_text(encoding="utf-8")) == {"Ada": "ada@x.com"}


def test_save_then_load_roundtrip(tmp_path):
    path = tmp_path / "contacts.json"
    save_contacts(path, {"Ada": "ada@x.com", "Bo": "bo@x.com"})
    assert load_contacts(path) == {"Ada": "ada@x.com", "Bo": "bo@x.com"}


def test_add_contact_creates_file_when_missing(tmp_path):
    path = tmp_path / "contacts.json"
    add_contact(path, "Ada", "ada@x.com")
    assert load_contacts(path) == {"Ada": "ada@x.com"}


def test_add_contact_appends_to_existing_contacts(tmp_path):
    path = tmp_path / "contacts.json"
    save_contacts(path, {"Ada": "ada@x.com"})
    add_contact(path, "Bo", "bo@x.com")
    assert load_contacts(path) == {"Ada": "ada@x.com", "Bo": "bo@x.com"}


def test_add_contact_rejects_duplicate_name(tmp_path):
    path = tmp_path / "contacts.json"
    save_contacts(path, {"Ada": "ada@x.com"})
    with pytest.raises(ContactError):
        add_contact(path, "Ada", "new@x.com")


def test_add_contact_duplicate_does_not_change_file(tmp_path):
    path = tmp_path / "contacts.json"
    save_contacts(path, {"Ada": "ada@x.com"})
    with pytest.raises(ContactError):
        add_contact(path, "Ada", "new@x.com")
    assert load_contacts(path) == {"Ada": "ada@x.com"}
