# Checkpoint 06 — Contacts file store
#
# A tiny contacts book persisted as a JSON file: {"Ada": "ada@x.com"}.
# This combines everything in the module — EAFP file handling, custom
# exceptions, chaining, and json I/O.
# Run: uv run pytest 06-errors-files -k checkpoint


class ContactError(Exception):
    """Raised for any problem loading, saving, or modifying contacts."""


def load_contacts(path):
    """Return the contacts dict stored at `path`.

    If `path` doesn't exist yet, return `{}` (a brand-new contacts
    book) — don't check `path.exists()` first, just try to open it and
    catch FileNotFoundError (EAFP).

    If the file exists but isn't valid JSON, raise
    `ContactError("corrupt contacts file: <path>") from e`, keeping the
    original `json.JSONDecodeError` as the cause.

    load_contacts(path to missing file) -> {}
    load_contacts(path to '{"Ada": "ada@x.com"}') -> {"Ada": "ada@x.com"}
    load_contacts(path to 'not json') -> raises ContactError
    """
    raise NotImplementedError


def save_contacts(path, contacts):
    """Write `contacts` (a dict) to `path` as JSON, overwriting it.

    save_contacts(path, {"Ada": "ada@x.com"}) -> file at `path` now
    holds valid JSON for that dict.
    """
    raise NotImplementedError


def add_contact(path, name, email):
    """Add `name` -> `email` to the contacts book stored at `path`.

    Load the current contacts (via `load_contacts`), reject the call
    with `ContactError` if `name` is already present (don't overwrite
    an existing contact), otherwise add the entry and save it back (via
    `save_contacts`). Returns nothing.

    add_contact(path, "Ada", "ada@x.com") on an empty/missing file ->
        file now contains {"Ada": "ada@x.com"}
    add_contact(path, "Ada", "new@x.com") when "Ada" already exists ->
        raises ContactError, file is left unchanged
    """
    raise NotImplementedError
