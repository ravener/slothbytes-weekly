#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest

MAPPING = ["O", "I", "Z", "E", "H", "S", "G", "L", "B", "-"]


# Weekly Challenge March 11, 2025
# Hidden Calculator Words
# At school, we used to play with our calculators and send each other secret messages.
# The trick was to enter a special number and turn the calculator upside-down.
# Like saying hello, you’d type in the calculator 07734 and turn it upside down:
# Given a number, create a function that converts it into a word by turning the integer 180 degrees around.
#
# 1 -> I
# 2 -> Z
# 3 -> E
# 4 -> H
# 5 -> S
# 6 -> G
# 7 -> L
# 8 -> B
# 9 -> -
# 0 -> O
#
# Notes
#   Convert to uppercase words.
#   Ignore dots.
def turn_calc(n: int) -> str:
    digits = []

    # Extract digits from right to left.
    while n > 10:
        d = n % 10
        n = n // 10

        digits.append(d)

    # If the digit is less than 10, can't be divided so add it.
    # this will also apply to the last digit after the loop above completes.
    if n < 10:
        digits.append(n)

    # Map them to the right character and join them into one string.
    return "".join(map(lambda x: MAPPING[x], digits))


class TurnCalcTest(unittest.TestCase):
    def test_turn_calc(self) -> None:
        self.assertEqual("LOL", turn_calc(707))
        self.assertEqual("BOSS", turn_calc(5508))
        self.assertEqual("SHOE", turn_calc(3045))
        # Leading zero is not allowed as that's used for octal literals.
        # self.assertEqual("HELLO", turn_calc(07734))


if __name__ == "__main__":
    unittest.main()
