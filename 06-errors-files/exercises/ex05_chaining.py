# Scenario: reading a setting out of a raw config dict, translating
# low-level failures into one domain-specific error. Concepts: `raise ...
# from e` exception chaining, catching multiple exception types.
# Run: uv run pytest 06-errors-files -k ex05


class ConfigError(Exception):
    """Raised when a setting can't be loaded from raw config data."""


def load_setting(raw, key):
    """Look up `raw[key]` and return it converted to int.

    `raw` is a dict of settings (values may be strings or numbers).
    Two things can go wrong:
    - `key` isn't in `raw` -> KeyError
    - the value can't convert to int -> ValueError

    Catch either and re-raise `ConfigError(f"bad setting: {key}") from e`
    so the original exception is preserved as the chain's cause.

    load_setting({"retries": "3"}, "retries") -> 3
    load_setting({}, "retries") -> raises ConfigError, __cause__ is a KeyError
    load_setting({"retries": "many"}, "retries") -> raises ConfigError,
        __cause__ is a ValueError
    """
    raise NotImplementedError
