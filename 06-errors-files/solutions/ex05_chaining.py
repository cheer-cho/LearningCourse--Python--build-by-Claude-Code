class ConfigError(Exception):
    """Raised when a setting can't be loaded from raw config data."""


def load_setting(raw, key):
    try:
        return int(raw[key])
    except (KeyError, ValueError) as e:
        raise ConfigError(f"bad setting: {key}") from e
