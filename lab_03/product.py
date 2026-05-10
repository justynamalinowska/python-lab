# -*- coding: utf-8 -*-
"""Klasa Product -- zadanie do samodzielnego wykonania."""


class Product:
    """Reprezentuje produkt w sklepie internetowym."""

    def __init__(self, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Cena nie może być ujemna.")
        if quantity < 0:
            raise ValueError("Ilość nie może być ujemna.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount: int):
        """Dodaje określoną ilość produktów do magazynu."""
        if amount < 0:
            raise ValueError("Ilość do dodania nie może być ujemna.")
        self.quantity += amount

    def remove_stock(self, amount: int):
        """Usuwa określoną ilość produktów z magazynu."""
        if amount < 0:
            raise ValueError("Ilość do usunięcia nie może być ujemna.")
        if amount > self.quantity:
            raise ValueError("Brak wystarczającej ilości w magazynie.")
        self.quantity -= amount

    def is_available(self) -> bool:
        """Zwraca True jeśli produkt jest dostępny (quantity > 0)."""
        return self.quantity > 0

    def total_value(self) -> float:
        """Zwraca całkowitą wartość produktów w magazynie."""
        return self.price * self.quantity