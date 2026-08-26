from ex08_json_csv import load_config, read_inventory, save_config


def test_save_config_writes_valid_json(tmp_path):
    path = tmp_path / "config.json"
    save_config(path, {"debug": True})
    assert '"debug"' in path.read_text(encoding="utf-8")


def test_save_config_and_load_config_roundtrip(tmp_path):
    path = tmp_path / "config.json"
    config = {"debug": True, "retries": 3, "name": "app"}
    save_config(path, config)
    assert load_config(path) == config


def test_load_config_reads_existing_file(tmp_path):
    path = tmp_path / "config.json"
    path.write_text('{"debug": true}', encoding="utf-8")
    assert load_config(path) == {"debug": True}


def test_read_inventory_parses_rows_with_int_quantity(tmp_path):
    path = tmp_path / "inventory.csv"
    path.write_text("name,quantity\nbolts,100\nscrews,250\n", encoding="utf-8")

    result = read_inventory(path)

    assert result == [
        {"name": "bolts", "quantity": 100},
        {"name": "screws", "quantity": 250},
    ]


def test_read_inventory_empty_file_has_only_header(tmp_path):
    path = tmp_path / "inventory.csv"
    path.write_text("name,quantity\n", encoding="utf-8")
    assert read_inventory(path) == []


def test_read_inventory_quantity_is_actually_an_int(tmp_path):
    path = tmp_path / "inventory.csv"
    path.write_text("name,quantity\nbolts,100\n", encoding="utf-8")
    result = read_inventory(path)
    assert result[0]["quantity"] == 100
    assert isinstance(result[0]["quantity"], int)
