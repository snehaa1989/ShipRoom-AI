"""Tests for the fictional Checkout API total calculation."""

import unittest

from src.checkout import calculate_total


class CalculateTotalTests(unittest.TestCase):
    def test_normal_order_with_multiple_items(self):
        items = [
            {"unit_price": 10.00, "quantity": 2},
            {"unit_price": 3.50, "quantity": 3},
        ]
        self.assertEqual(calculate_total(items), 30.5)

    def test_valid_percentage_discount(self):
        items = [{"unit_price": 25.00, "quantity": 2}]
        self.assertEqual(calculate_total(items, discount_percent=20), 40.0)

    def test_empty_order(self):
        self.assertEqual(calculate_total([]), 0.0)

    def test_negative_item_quantity_raises_value_error(self):
        items = [{"unit_price": 10.00, "quantity": -1}]
        with self.assertRaises(ValueError):
            calculate_total(items)

    def test_negative_unit_price_raises_value_error(self):
        items = [{"unit_price": -10.00, "quantity": 1}]
        with self.assertRaises(ValueError):
            calculate_total(items)

    def test_discount_below_zero_raises_value_error(self):
        items = [{"unit_price": 10.00, "quantity": 1}]
        with self.assertRaises(ValueError):
            calculate_total(items, discount_percent=-1)

    def test_discount_above_100_raises_value_error(self):
        items = [{"unit_price": 10.00, "quantity": 1}]
        with self.assertRaises(ValueError):
            calculate_total(items, discount_percent=101)


if __name__ == "__main__":
    unittest.main()
