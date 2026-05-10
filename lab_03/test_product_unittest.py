# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

import unittest
from product import Product

class TestProduct(unittest.TestCase):

    def setUp(self):
        """Przygotuj instancję Product do testów."""
        self.product = Product("Laptop", 2999.99, 10)

    # --- Testy add_stock ---
    def test_add_stock_positive(self):
        """Sprawdź, czy dodanie towaru zwiększa quantity."""
        self.product.add_stock(5)
        self.assertEqual(self.product.quantity, 15)

    def test_add_stock_negative_raises(self):
        """Sprawdź, czy ujemna wartość rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.product.add_stock(-1)

    # --- Testy remove_stock ---
    def test_remove_stock_positive(self):
        """Sprawdź, czy usunięcie towaru zmniejsza quantity."""
        self.product.remove_stock(4)
        self.assertEqual(self.product.quantity, 6)

    def test_remove_stock_too_much_raises(self):
        """Sprawdź, czy próba usunięcia więcej niż jest dostępne rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.product.remove_stock(9999)

    def test_remove_stock_negative_raises(self):
        """Sprawdź, czy ujemna wartość rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.product.remove_stock(-1)

    # --- Testy is_available ---
    def test_is_available_when_in_stock(self):
        """Sprawdź, czy produkt z quantity > 0 jest dostępny."""
        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        """Sprawdź, czy produkt z quantity == 0 nie jest dostępny."""
        empty_product = Product("Pendrive", 49.99, 0)
        self.assertFalse(empty_product.is_available())

    # --- Testy total_value ---
    def test_total_value(self):
        """Sprawdź, czy total_value zwraca price * quantity."""
        self.assertEqual(self.product.total_value(), 2999.99 * 10)


if __name__ == "__main__":
    unittest.main()