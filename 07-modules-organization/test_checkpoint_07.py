import pytest
from checkpoint_07_pkg import add_item, low_stock_report, remove_item, stock_count


def test_add_item_creates_new_entry():
    inventory = {}
    add_item(inventory, "bolts", 40)
    assert inventory == {"bolts": 40}


def test_add_item_increments_existing_entry():
    inventory = {"bolts": 40}
    add_item(inventory, "bolts", 10)
    assert inventory == {"bolts": 50}


def test_remove_item_decrements():
    inventory = {"bolts": 40}
    remove_item(inventory, "bolts", 15)
    assert inventory == {"bolts": 25}


def test_remove_item_deletes_key_when_reaching_zero():
    inventory = {"bolts": 40}
    remove_item(inventory, "bolts", 40)
    assert inventory == {}


def test_remove_item_raises_when_name_missing():
    with pytest.raises(ValueError):
        remove_item({}, "bolts", 1)


def test_remove_item_raises_when_qty_exceeds_stock():
    with pytest.raises(ValueError):
        remove_item({"bolts": 5}, "bolts", 10)


def test_stock_count_known_item():
    assert stock_count({"bolts": 40}, "bolts") == 40


def test_stock_count_unknown_item_is_zero():
    assert stock_count({"bolts": 40}, "screws") == 0


def test_low_stock_report_filters_and_sorts_alphabetically():
    inventory = {"bolts": 40, "nuts": 5, "screws": 2}
    assert low_stock_report(inventory, 10) == ["nuts", "screws"]


def test_low_stock_report_empty_when_all_well_stocked():
    inventory = {"bolts": 40}
    assert low_stock_report(inventory, 10) == []
