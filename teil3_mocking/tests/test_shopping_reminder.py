import sys
import os
from datetime import date
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import shopping_reminder
from shopping_reminder import ShoppingReminder

def test_is_shopping_day_true_on_sunday():
    reminder = ShoppingReminder()
    with patch.object(shopping_reminder, "date") as mock_date:
        mock_date.today.return_value = date(2026, 6, 21)  # ein Sonntag
        assert reminder.is_shopping_day() is Trueq

def test_is_shopping_day_false_on_wednesday():
    reminder = ShoppingReminder()
    with patch.object(shopping_reminder, "date") as mock_date:
        mock_date.today.return_value = date(2026, 6, 24)  # ein Mittwoch
        assert reminder.is_shopping_day() is False

def test_days_until_shopping_day_from_wednesday():
    reminder = ShoppingReminder()
    with patch.object(shopping_reminder, "date") as mock_date:
        mock_date.today.return_value = date(2026, 6, 24)  # Mittwoch
        assert reminder.days_until_shopping_day() == 4

def test_days_until_shopping_day_is_zero_on_sunday():
    reminder = ShoppingReminder()
    with patch.object(shopping_reminder, "date") as mock_date:
        mock_date.today.return_value = date(2026, 6, 21)  # Sonntag
        assert reminder.days_until_shopping_day() == 0