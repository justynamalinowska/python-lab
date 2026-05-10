# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product


# --- Fixture ---
@pytest.fixture
def product():
    """Tworzy instancję Product do testów."""
    return Product("Laptop", 2999.99, 10)


# --- Testy z fixture ---
def test_is_available(product):
    """Sprawdź dostępność produktu."""
    assert product.is_available() == True


def test_total_value(product):
    """Sprawdź wartość całkowitą."""
    assert product.total_value() == 2999.99 * 10


# --- Testy z parametryzacją ---
@pytest.mark.parametrize("amount, expected_quantity", [
    (5, 15),    # dodanie 5 do początkowych 10 = 15
    (0, 10),    # dodanie 0 = bez zmian
    (100, 110), # dodanie 100
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    """Testuje add_stock z różnymi wartościami."""
    product.add_stock(amount)
    assert product.quantity == expected_quantity


# --- Testy błędów ---
def test_remove_stock_too_much_raises(product):
    """Sprawdź, czy próba usunięcia za dużej ilości rzuca ValueError."""
    with pytest.raises(ValueError):
        product.remove_stock(9999)


def test_add_stock_negative_raises(product):
    """Sprawdź, czy ujemna wartość w add_stock rzuca ValueError."""
    with pytest.raises(ValueError):
        product.add_stock(-1)