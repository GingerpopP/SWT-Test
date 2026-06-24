import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from cart import Cart, ItemNotFoundError


def test_add_item_increases_item_count():
    cart = Cart()
    cart.add_item("Apfel", price=0.40, quantity=3)
    assert cart.item_count() == 1


def test_add_same_item_twice_merges_quantity():
    cart = Cart()
    cart.add_item("Apfel", price=0.40, quantity=3)
    cart.add_item("Apfel", price=0.40, quantity=2)
    assert cart.item_count() == 1
    assert cart.get_total() == pytest.approx(0.40 * 5)


def test_remove_item_decreases_item_count():
    cart = Cart()
    cart.add_item("Apfel", price=0.40, quantity=3)
    cart.add_item("Banane", price=0.30, quantity=2)
    cart.remove_item("Apfel")
    assert cart.item_count() == 1


def test_get_total_sums_price_times_quantity():
    cart = Cart()
    cart.add_item("Apfel", price=0.40, quantity=3)
    cart.add_item("Banane", price=0.30, quantity=2)
    # 0.40*3 + 0.30*2 = 1.20 + 0.60 = 1.80
    assert cart.get_total() == pytest.approx(1.80)


def test_remove_nonexistent_item_raises_item_not_found_error():
    cart = Cart()
    cart.add_item("Apfel", price=0.40, quantity=3)
    with pytest.raises(ItemNotFoundError):
        cart.remove_item("Kiwi")
