def add_item(inventory, name, qty):
    inventory[name] = inventory.get(name, 0) + qty


def remove_item(inventory, name, qty):
    if name not in inventory:
        raise ValueError(f"no such item: {name}")
    if qty > inventory[name]:
        raise ValueError(f"not enough stock to remove {qty} of {name}")

    remaining = inventory[name] - qty
    if remaining == 0:
        del inventory[name]
    else:
        inventory[name] = remaining


def stock_count(inventory, name):
    return inventory.get(name, 0)


def low_stock_report(inventory, threshold):
    return sorted(name for name, qty in inventory.items() if qty < threshold)
