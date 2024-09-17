#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest
from typing import NamedTuple


class Pocket(NamedTuple):
    quarters: int
    dimes: int
    nickels: int
    pennies: int

    def sum(self) -> float:
        """Return the sum total of the pocket in dollars."""
        # quarter = 25 cents / $0.25
        # dime= 10 cents / $0.10
        # nickel = 5 cents / $0.05
        # penny = 1 cent / $0.01
        return (
            (self.quarters / 4)
            + (self.dimes / 10)
            + (self.nickels / 20)
            + (self.pennies / 100)
        )


# Weekly Challenge September 17, 2024
# Convenience Store
# Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item.
# Change will always be represented in the following order: quarters, dimes, nickels, pennies.
#  Example: changeEnough([25, 20, 5, 0], 4.25) return true because:
#  25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50.
#  This means you can afford the item, so return true.
def change_enough(pocket: Pocket, item_price: float) -> bool:
    return pocket.sum() >= item_price


class ChangeEnoughTest(unittest.TestCase):
    def test_change_enough(self) -> None:
        self.assertEqual(Pocket(25, 20, 5, 0).sum(), 8.50)
        self.assertFalse(change_enough(Pocket(2, 100, 0, 0), 14.11))
        self.assertTrue(change_enough(Pocket(0, 0, 20, 5), 0.75))
        self.assertTrue(change_enough(Pocket(30, 40, 20, 5), 12.55))
        self.assertFalse(change_enough(Pocket(10, 0, 0, 50), 3.85))
        self.assertFalse(change_enough(Pocket(1, 0, 5, 219), 19.99))


if __name__ == "__main__":
    unittest.main()
