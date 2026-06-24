from dataclasses import dataclass


class ItemNotFoundError(Exception):
@dataclass
class CartItem:
    name: str
    price: float
    quantity: int

class Cart:
    def __init__(self) -> None:
        self._items: dict[str, CartItem] = {}

    def add_item(self, name: str, price: float, quantity: int) -> None:
        if name in self._items:
            self._items[name].quantity += quantity
        else:
            self._items[name] = CartItem(name, price, quantity)

    def remove_item(self, name: str) -> None:
        self._ensure_known(name)
        del self._items[name]

    def _ensure_known(self, name: str) -> None:
        if name not in self._items:
            raise ItemNotFoundError(f"Artikel '{name}' ist nicht im Warenkorb.")

    def get_total(self) -> float:
        return sum(item.price * item.quantity for item in self._items.values())

    def item_count(self) -> int:
        return len(self._items)
