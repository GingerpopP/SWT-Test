from dataclasses import dataclass

class EmptyShoppingListError(Exception):
@dataclass
class ShoppingItem:
    name: str
    unit_price: float
    quantity: int

    def line_total(self) -> float:
        return self.unit_price * self.quantity

class ShoppingList:
    """Aggregiert Zutaten aus dem Wochenmenüplan zu einer Einkaufsliste."""

    def __init__(self) -> None:
        self._items: list[ShoppingItem] = []

    def add_item(self, name: str, unit_price: float, quantity: int) -> None:
        if unit_price < 0:
            raise ValueError(f"Preis darf nicht negativ sein: {unit_price}")
        if quantity <= 0:
            raise ValueError(f"Menge muss positiv sein: {quantity}")

        for item in self._items:
            if item.name == name:
                item.quantity += quantity
                return

        self._items.append(ShoppingItem(name, unit_price, quantity))

    def total_cost(self) -> float:
        return sum(item.line_total() for item in self._items)

    def average_item_price(self) -> float:
        if not self._items:
            raise EmptyShoppingListError(
                "Durchschnittspreis nicht berechenbar: Liste ist leer."
            )
        return self.total_cost() / sum(item.quantity for item in self._items)

    def item_count(self) -> int:
        return len(self._items)
