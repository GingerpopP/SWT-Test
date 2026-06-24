import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from shopping_list import ShoppingList, EmptyShoppingListError


def test_add_single_item_increases_total():
    sl = ShoppingList()
    sl.add_item("Tomaten", unit_price=0.50, quantity=4)
    assert sl.total_cost() == pytest.approx(2.0)


def test_add_same_item_twice_merges_quantity():
    sl = ShoppingList()
    sl.add_item("Reis", unit_price=2.0, quantity=1)
    sl.add_item("Reis", unit_price=2.0, quantity=2)
    assert sl.item_count() == 1
    assert sl.total_cost() == pytest.approx(6.0)


def test_total_cost_sums_multiple_items():
    sl = ShoppingList()
    sl.add_item("Nudeln", unit_price=1.20, quantity=2)
    sl.add_item("Sojasauce", unit_price=3.00, quantity=1)
    assert sl.total_cost() == pytest.approx(5.40)


def test_average_item_price_computes_weighted_average():
    sl = ShoppingList()
    sl.add_item("Eier", unit_price=0.30, quantity=10)
    sl.add_item("Butter", unit_price=2.00, quantity=1)
    # total = 3.0 + 2.0 = 5.0, quantity_sum = 11
    assert sl.average_item_price() == pytest.approx(5.0 / 11)


def test_add_item_with_negative_price_raises_value_error():
    sl = ShoppingList()
    with pytest.raises(ValueError):
        sl.add_item("Verdorbene Milch", unit_price=-1.0, quantity=1)


def test_add_item_with_zero_quantity_raises_value_error():
    sl = ShoppingList()
    with pytest.raises(ValueError):
        sl.add_item("Mehl", unit_price=1.0, quantity=0)


def test_average_item_price_on_empty_list_raises_custom_exception():
    sl = ShoppingList()
    with pytest.raises(EmptyShoppingListError):
        sl.average_item_price()
