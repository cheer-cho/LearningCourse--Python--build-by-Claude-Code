import pytest
from ex05_chaining import ConfigError, load_setting


def test_load_setting_returns_int_value():
    assert load_setting({"retries": "3"}, "retries") == 3


def test_load_setting_accepts_already_numeric_value():
    assert load_setting({"retries": 5}, "retries") == 5


def test_load_setting_raises_config_error_on_missing_key():
    with pytest.raises(ConfigError):
        load_setting({}, "retries")


def test_load_setting_chains_key_error_as_cause():
    with pytest.raises(ConfigError) as excinfo:
        load_setting({}, "retries")
    assert isinstance(excinfo.value.__cause__, KeyError)


def test_load_setting_chains_value_error_as_cause():
    with pytest.raises(ConfigError) as excinfo:
        load_setting({"retries": "many"}, "retries")
    assert isinstance(excinfo.value.__cause__, ValueError)


def test_load_setting_error_message_names_the_key():
    with pytest.raises(ConfigError, match="retries"):
        load_setting({}, "retries")
