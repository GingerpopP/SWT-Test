from datetime import date


class ShoppingReminder:
    SHOPPING_WEEKDAY = 6  # Montag=0 ... Sonntag=6

    def is_shopping_day(self) -> bool:
        """Liefert True, wenn heute (laut Systemuhr) Einkaufstag ist."""
        today = date.today()
        return today.weekday() == self.SHOPPING_WEEKDAY

    def days_until_shopping_day(self) -> int:
        """Anzahl Tage bis zum naechsten Einkaufstag (0, falls heute)."""
        today = date.today()
        days_ahead = (self.SHOPPING_WEEKDAY - today.weekday()) % 7
        return days_ahead
