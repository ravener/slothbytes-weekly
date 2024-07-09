#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest
from typing import TypeVar

T = TypeVar("T", int, str)


# Weekly Challenge July 10, 2024
# Advanced List Sort
# Create a function that takes a list of numbers or strings and
# returns a list with the items from the original list stored into sub lists.
# Items of the same value should be in the same sub list.
#
# Notes
# The sub lists should be returned in the order of each element's first appearance in the given list.
def advanced_sort(arr: list[T]) -> list[list[T]]:
    results: list[list[T]] = []
    cache: dict[T, int] = {}

    for item in arr:
        if item in cache:
            results[cache[item]].append(item)
        else:
            cache[item] = len(results)
            results.append([item])

    return results


class TestAdvancedSort(unittest.TestCase):
    def test_advanced_sort(self) -> None:
        self.assertEqual(advanced_sort([2, 1, 2, 1]), [[2, 2], [1, 1]])
        self.assertEqual(advanced_sort([5, 4, 5, 5, 4, 3]), [[5, 5, 5], [4, 4], [3]])
        self.assertEqual(
            advanced_sort(["b", "a", "b", "a", "c"]), [["b", "b"], ["a", "a"], ["c"]]
        )


if __name__ == "__main__":
    unittest.main()
