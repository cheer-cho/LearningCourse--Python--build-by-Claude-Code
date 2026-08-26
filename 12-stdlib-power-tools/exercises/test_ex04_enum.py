import pytest
from ex04_enum import Status, from_label, is_terminal, next_status


def test_from_label_matches_lowercase():
    assert from_label("active") == Status.ACTIVE


def test_from_label_matches_uppercase():
    assert from_label("PENDING") == Status.PENDING


def test_from_label_matches_mixed_case():
    assert from_label("Closed") == Status.CLOSED


def test_from_label_raises_value_error_for_unknown_label():
    with pytest.raises(ValueError):
        from_label("bogus")


def test_next_status_pending_to_active():
    assert next_status(Status.PENDING) == Status.ACTIVE


def test_next_status_active_to_closed():
    assert next_status(Status.ACTIVE) == Status.CLOSED


def test_next_status_closed_stays_closed():
    assert next_status(Status.CLOSED) == Status.CLOSED


def test_is_terminal_true_for_closed():
    assert is_terminal(Status.CLOSED) is True


def test_is_terminal_false_for_pending_and_active():
    assert is_terminal(Status.PENDING) is False
    assert is_terminal(Status.ACTIVE) is False
