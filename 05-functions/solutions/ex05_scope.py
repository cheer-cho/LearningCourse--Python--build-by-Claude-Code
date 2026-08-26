LEVEL = "global"
total_clicks = 0


def shadowed_local():
    LEVEL = "local"
    return LEVEL


def read_global_total():
    return total_clicks + 1


def make_id_generator(start=1):
    next_value = start

    def next_id():
        nonlocal next_value
        current = next_value
        next_value += 1
        return current

    return next_id


def register_click():
    global total_clicks
    total_clicks = total_clicks + 1
    return total_clicks
