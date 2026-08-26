from ex06_circular_fix import format_money, pick_fix
from mod07_customers import customer_balance_line
from mod07_orders import order_summary


def test_format_money_typical():
    assert format_money(1999) == "$19.99"


def test_format_money_zero():
    assert format_money(0) == "$0.00"


def test_format_money_under_a_dollar():
    assert format_money(5) == "$0.05"


def test_orders_and_customers_import_together_without_a_cycle():
    assert order_summary(42, 1999) == "order 42: $19.99"
    assert customer_balance_line("Ada", 500) == "Ada owes $5.00"


def test_pick_fix_identifies_the_extraction_strategy():
    options = {
        "delay": "move the import inside the function that needs it",
        "extract": "move the shared code both modules need into a new module",
        "merge": "combine both modules into a single file",
    }
    assert pick_fix(options) == "extract"


def test_pick_fix_works_regardless_of_key_names():
    options = {
        "a": "combine both files into a single module",
        "b": "import it lazily, inside the function body",
        "c": "pull the shared logic out into a new module both files can use",
    }
    assert pick_fix(options) == "c"
