#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest
from typing import Iterable


# Weekly Challenge October 1, 2024
# How Much is True?
# Create a function which returns the number of true values there are in an array.
#
# Notes
#   Return 0 if given an empty array.
#   All array items are of the type bool (true or false).
def count_true(iter: Iterable[bool]) -> int:
    return sum(1 for item in iter if item is True)


class CountTrueTest(unittest.TestCase):
    def test_count_true(self) -> None:
        self.assertEqual(2, count_true([True, False, False, True, False]))
        self.assertEqual(0, count_true([False, False, False, False]))
        self.assertEqual(0, count_true([]))


if __name__ == "__main__":
    unittest.main()
