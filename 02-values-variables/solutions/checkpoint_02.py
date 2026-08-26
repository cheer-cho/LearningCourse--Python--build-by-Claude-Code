"""Reference solution for checkpoint_02. See ../checkpoint_02.py."""

from __future__ import annotations


def parse_money(text: str) -> float:
    return float(text.strip().removeprefix("$"))


def format_receipt(store: str, items: list[tuple[str, str, int]]) -> str:
    # Exactly 3 items — unpack directly, no loop needed.
    (name1, price1_text, qty1), (name2, price2_text, qty2), (name3, price3_text, qty3) = items

    price1, price2, price3 = parse_money(price1_text), parse_money(price2_text), parse_money(price3_text)
    total1, total2, total3 = price1 * qty1, price2 * qty2, price3 * qty3

    subtotal = total1 + total2 + total3
    tax = subtotal * 0.07
    total = subtotal + tax

    line1 = f"{name1:<10} x{qty1:<3} @ ${price1:>6.2f} = ${total1:>7.2f}"
    line2 = f"{name2:<10} x{qty2:<3} @ ${price2:>6.2f} = ${total2:>7.2f}"
    line3 = f"{name3:<10} x{qty3:<3} @ ${price3:>6.2f} = ${total3:>7.2f}"

    return "\n".join(
        [
            f"=== {store} ===",
            line1,
            line2,
            line3,
            "-" * 34,
            f"{'Subtotal':<24}${subtotal:>8.2f}",
            f"{'Tax (7%)':<24}${tax:>8.2f}",
            f"{'Total':<24}${total:>8.2f}",
        ]
    )
