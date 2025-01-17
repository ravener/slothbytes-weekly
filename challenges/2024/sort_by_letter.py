#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


def first_letter(s: str) -> str:
    """
    Returns the first letter found in the given string.

    :param s: The string to search.
    :returns: The first letter found.
    """
    return next(char for char in s if char.isalpha())


# Weekly Challenge July 30, 2024
# Sort by the Letters
# Write a function that sorts each string in a list by the letter in alphabetic ascending order (a-z).
#
# Notes
#   Each string will only have one (lowercase) letter.
#   If given an empty list, return an empty list.
def sort_by_letter(arr: list[str]) -> list[str]:
    """
    Sorts each string in a list by the letter in alphabetic ascending order (a-z).

    :param arr: The array to sort.
    :returns: The sorted array.
    """
    return sorted(arr, key=first_letter)


class SortByLetterTest(unittest.TestCase):
    def test_sort_by_letter(self) -> None:
        self.assertEqual(
            sort_by_letter(["932c", "832u32", "2344b"]), ["2344b", "932c", "832u32"]
        )
        self.assertEqual(
            sort_by_letter(["99a", "78b", "c2345", "11d"]),
            ["99a", "78b", "c2345", "11d"],
        )
        self.assertEqual(
            sort_by_letter(["572z", "5y5", "304q2"]), ["304q2", "5y5", "572z"]
        )
        self.assertEqual(sort_by_letter([]), [])


if __name__ == "__main__":
    unittest.main()
