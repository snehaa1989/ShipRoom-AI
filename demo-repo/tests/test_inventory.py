"""Tests describing the intended inventory reservation behavior."""

import unittest

from src.inventory import reserve_stock


class ReserveStockTests(unittest.TestCase):
    def test_successful_stock_reservation(self):
        inventory = {"SKU-1": 10}
        self.assertEqual(reserve_stock(inventory, "SKU-1", 3), 7)
        self.assertEqual(inventory["SKU-1"], 7)

    def test_reserving_exactly_all_available_stock(self):
        inventory = {"SKU-1": 5}
        self.assertEqual(reserve_stock(inventory, "SKU-1", 5), 0)
        self.assertEqual(inventory["SKU-1"], 0)

    def test_negative_quantity_is_rejected(self):
        inventory = {"SKU-1": 10}
        original_inventory = inventory.copy()
        with self.assertRaises(ValueError):
            reserve_stock(inventory, "SKU-1", -2)
        self.assertEqual(inventory, original_inventory)

    def test_boolean_quantity_is_rejected_without_mutation(self):
        inventory = {"SKU-1": 10}
        original_inventory = inventory.copy()
        with self.assertRaises(ValueError):
            reserve_stock(inventory, "SKU-1", True)
        self.assertEqual(inventory, original_inventory)

    def test_non_integer_quantities_are_rejected_without_mutation(self):
        for quantity in (1.5, "2", None):
            with self.subTest(quantity=quantity):
                inventory = {"SKU-1": 10}
                original_inventory = inventory.copy()
                with self.assertRaises(ValueError):
                    reserve_stock(inventory, "SKU-1", quantity)
                self.assertEqual(inventory, original_inventory)

    def test_zero_quantity_is_valid_and_does_not_change_stock(self):
        inventory = {"SKU-1": 10}
        self.assertEqual(reserve_stock(inventory, "SKU-1", 0), 10)
        self.assertEqual(inventory["SKU-1"], 10)

    def test_insufficient_stock_is_rejected(self):
        inventory = {"SKU-1": 2}
        original_inventory = inventory.copy()
        with self.assertRaises(ValueError):
            reserve_stock(inventory, "SKU-1", 3)
        self.assertEqual(inventory, original_inventory)

    def test_invalid_existing_stock_is_rejected_without_mutation(self):
        for stock in (-1, True, 1.5, "10"):
            with self.subTest(stock=stock):
                inventory = {"SKU-1": stock}
                original_inventory = inventory.copy()
                with self.assertRaises(ValueError):
                    reserve_stock(inventory, "SKU-1", 1)
                self.assertEqual(inventory, original_inventory)

    def test_unknown_sku_is_reported_as_validation_error(self):
        inventory = {"SKU-1": 10}
        original_inventory = inventory.copy()
        with self.assertRaises(ValueError):
            reserve_stock(inventory, "MISSING", 1)
        self.assertEqual(inventory, original_inventory)


if __name__ == "__main__":
    unittest.main()
