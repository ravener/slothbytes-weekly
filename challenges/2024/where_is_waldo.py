#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest
from collections import Counter


# Weekly Challenge August 13, 2024
# Where’s Waldo
# Return the coordinates ([row, col]) of the element that differs from the rest.
#
# Notes
#   The given array will always be a square or rectangle.
#   Rows and columns are 1-indexed (not zero-indexed).
def where_is_waldo(arr: list[list[str]]) -> tuple[int, int] | None:
    # Flatten the array and identify the most common character.
    flattened = Counter([char for row in arr for char in row])
    common_char = flattened.most_common(1)[0][0]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # And if the character differs from the most common character, that's the one.
            if arr[i][j] != common_char:
                return (i + 1, j + 1)


class WhereIsWaldoTest(unittest.TestCase):
    def test_where_is_waldo(self) -> None:
        self.assertEqual(
            (3, 2), where_is_waldo([["A", "A", "A"], ["A", "A", "A"], ["A", "B", "A"]])
        )
        self.assertEqual(
            (2, 4), where_is_waldo([["c", "c", "c", "c"], ["c", "c", "c", "d"]])
        )
        self.assertEqual(
            (5, 1),
            where_is_waldo(
                [
                    ["O", "O", "O", "O"],
                    ["O", "O", "O", "O"],
                    ["O", "O", "O", "O"],
                    ["O", "O", "O", "O"],
                    ["P", "O", "O", "O"],
                    ["O", "O", "O", "O"],
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
