#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


# Weekly Challenge July 2, 2024
# Binary Search Practice
# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index.
# Return -1 if the target is not in the array.
def find_first_occurrence(arr: list[int], target: int) -> int:
    """
    Finds the first occurrence of target from the given list.

    :param arr: The array of integers, must be sorted.
    :param target: The target integer to find.
    :returns: The index of the first occurrence of target in arr or -1 if not found.
    """
    left = 0
    right = len(arr) - 1
    results = -1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            results = mid
            right = mid - 1

    return results


class TestFindFirstOccurrence(unittest.TestCase):
    def test_find_first_occurrence(self) -> None:
        arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
        target = 3
        self.assertEqual(find_first_occurrence(arr, target), 1)

    def test_not_found(self) -> None:
        arr = [2, 3, 5, 7, 11, 13, 17, 19]
        target = 6
        self.assertEqual(find_first_occurrence(arr, target), -1)


if __name__ == "__main__":
    unittest.main()
