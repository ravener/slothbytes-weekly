#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


# Weekly Challenge June 25, 2024
# Making a box
# Create a function that creates a box based on dimension n.
def make_box(n: int) -> list[str]:
    """
    Creates a box based on dimension n.

    :param n: The dimension of the box.
    :returns: A list representing the box.
    """
    if n == 1:
        return ["#"]

    top_bottom = "#" * n
    middle = "#" + " " * (n - 2) + "#"
    return [top_bottom] + [middle] * (n - 2) + [top_bottom]


class TestMakeBox(unittest.TestCase):
    def test_make_box(self) -> None:
        self.assertEqual(make_box(5), ["#####", "#   #", "#   #", "#   #", "#####"])
        self.assertEqual(make_box(3), ["###", "# #", "###"])
        self.assertEqual(make_box(2), ["##", "##"])
        self.assertEqual(make_box(1), ["#"])


if __name__ == "__main__":
    unittest.main()
