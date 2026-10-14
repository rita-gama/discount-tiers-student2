"""Existing project tests. They pass before and after the fix."""

from decimal import Decimal

import pytest

from shop.cart import cart_total
from shop.pricing import apply_discount, line_total


def test_small_order_has_no_discount():
    assert line_total(Decimal("2.50"), 3) == Decimal("7.50")


def test_large_order_gets_top_tier():
    assert line_total(Decimal("1.00"), 120) == Decimal("102.00")


def test_cart_adds_lines():
    assert cart_total([(Decimal("2.50"), 3), (Decimal("1.00"), 120)]) == Decimal("109.50")


def test_empty_cart_is_zero():
    assert cart_total([]) == Decimal("0")


def test_discount_rounds_to_cents():
    assert apply_discount(Decimal("10.00"), Decimal("33")) == Decimal("6.70")


def test_negative_quantity_is_rejected():
    with pytest.raises(ValueError):
        line_total(Decimal("1.00"), -1)
