"""Checkout total calculation for the fictional API demo."""

import math
from numbers import Real


def calculate_total(items, discount_percent=0):
    """Return the discounted total for items, rounded to two decimal places.

    Each item is expected to be a dictionary containing ``unit_price`` and
    ``quantity``. Invalid quantities, prices, or discounts raise ``ValueError``.
    """
    if (
        isinstance(discount_percent, bool)
        or not isinstance(discount_percent, Real)
        or not 0 <= discount_percent <= 100
    ):
        raise ValueError("discount_percent must be a finite number between 0 and 100")
    try:
        discount_is_finite = math.isfinite(discount_percent)
    except OverflowError:
        discount_is_finite = False
    if not discount_is_finite:
        raise ValueError("discount_percent must be a finite number between 0 and 100")

    validated_items = []
    for item in items:
        quantity = item["quantity"]
        unit_price = item["unit_price"]

        if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
            raise ValueError("quantity must be a non-negative integer")

        if (
            isinstance(unit_price, bool)
            or not isinstance(unit_price, Real)
            or unit_price < 0
        ):
            raise ValueError("unit_price must be a finite non-negative number")
        try:
            unit_price_is_finite = math.isfinite(unit_price)
        except OverflowError:
            unit_price_is_finite = False
        if not unit_price_is_finite:
            raise ValueError("unit_price must be a finite non-negative number")

        validated_items.append((unit_price, quantity))

    subtotal = sum(unit_price * quantity for unit_price, quantity in validated_items)
    total = subtotal * (1 - discount_percent / 100)
    return round(total, 2)
