"""Inventory stock reservation for the ShipRoom AI demo."""


def reserve_stock(inventory, sku, quantity):
    """Reserve quantity units for sku and return the remaining stock.

    Quantity and the existing stock must be non-negative integers (booleans
    are not accepted). Invalid requests raise ``ValueError`` without changing
    the inventory.
    """
    if isinstance(quantity, bool) or not isinstance(quantity, int) or quantity < 0:
        raise ValueError("quantity must be a non-negative integer")

    try:
        sku_exists = sku in inventory
    except TypeError as error:
        raise ValueError("sku must be a valid inventory key") from error
    if not sku_exists:
        raise ValueError(f"unknown SKU: {sku!r}")

    stock = inventory[sku]
    if isinstance(stock, bool) or not isinstance(stock, int) or stock < 0:
        raise ValueError("existing stock must be a non-negative integer")
    if quantity > stock:
        raise ValueError("insufficient stock")

    remaining = stock - quantity
    inventory[sku] = remaining
    return remaining
