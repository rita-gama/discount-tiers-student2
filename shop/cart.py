"""Shopping cart totals"""

from decimal import Decimal

from shop.pricing import line_total


def cart_total(lines: list[tuple[Decimal, int]]) -> Decimal:
    """Return the total for a list of (unit price, quantity) lines."""
    return sum((line_total(price, quantity) for price, quantity in lines), Decimal("0"))
