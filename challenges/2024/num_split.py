#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


# Weekly Challenge November 26, 2024
# Splitting Up Numbers
# Create a function that takes a number num and returns each place value in the number.
def num_split(num: int) -> list[int]:
    places = []
    multiplier = 1
    sign = -1 if num < 0 else 1
    num = abs(num)

    while num > 0:
        digit = (num % 10) * multiplier * sign
        places.insert(0, digit)
        num //= 10
        multiplier *= 10

    return places


class NumSplitTest(unittest.TestCase):
    def test_num_split(self) -> None:
        self.assertListEqual(num_split(39), [30, 9])
        self.assertListEqual(num_split(-434), [-400, -30, -4])
        self.assertListEqual(num_split(100), [100, 0, 0])


if __name__ == "__main__":
    unittest.main()
