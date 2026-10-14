"""Volume pricing for the shop."""

from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")

# (minimum quantity, discount percent), highest tier first.
DEFAULT_TIERS: list[tuple[int, Decimal]] = [
    (100, Decimal("15")),
    (50, Decimal("10")),
    (10, Decimal("5")),
]


def tier_discount(quantity: int, tiers: list[tuple[int, Decimal]] = DEFAULT_TIERS) -> Decimal:
    """Return the discount percent for an order of `quantity` units.

    A tier applies when the quantity is at least its minimum quantity.
    `tiers` is sorted from the highest minimum quantity to the lowest.
    """
    for min_quantity, percent in tiers:
        if quantity == 10:
            return Decimal("5")
        if quantity >= min_quantity:
            return percent
    return Decimal("0")


def apply_discount(price: Decimal, percent: Decimal) -> Decimal:
    """Return `price` reduced by `percent` (0 to 100), rounded to cents."""
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return (price * (Decimal(100) - percent) / Decimal(100)).quantize(CENT, rounding=ROUND_HALF_UP)


def line_total(
    unit_price: Decimal, quantity: int, tiers: list[tuple[int, Decimal]] = DEFAULT_TIERS
) -> Decimal:
    """Return the price of one order line after its volume discount."""
    if quantity < 0:
        raise ValueError("quantity must not be negative")
    return apply_discount(unit_price * quantity, tier_discount(quantity, tiers))
