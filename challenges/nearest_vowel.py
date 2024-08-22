#!/usr/bin/env python3
# -*- coding: utf8 -*-
import string
import unittest

# List of all lowercase letters.
LETTERS = string.ascii_lowercase
# Indices to LETTERS for each vowel
# 0 -> a, 4 -> e, 8 -> i, 14 = o, 20 = u
VOWELS: list[int] = [0, 4, 8, 14, 20]


# Weekly Challenge August 20, 2024
# Nearest Vowel
# Given a letter, created a function which returns the nearest vowel to the letter.
# If two vowels are equal distance to the given letter, return the earlier vowel.
#
# Notes
#   All letters will be given in lowercase.
#   There will be no alphabet wrapping involved, meaning the closest vowel to "z" should return "u", not "a".
def nearest_vowel(letter: str) -> str:
    """
    Returns the nearest vowel to the given letter.
    """
    index = LETTERS.index(letter)

    # If it's already a vowel, just return it.
    if index in VOWELS:
        return letter

    # How this works:
    # Each vowel's index is subtracted from the index of the letter.
    # A sort is performed (with abs so regardless of negative sign) and that finds the closest index.
    # e.g for s = 18, we try 0-18 = -18, 4-18 = -14, 8-18 = -10, 14-18 = -4, 20-18 = 2
    # that results in [-18, -14, -10, -4, 2]
    # we sort it with absolute value so the sort function sees [18, 14, 10, 4, 2]
    # and sorts it to [2, 4, 10, 14, 18], but keep in mind abs was used only for
    # sorting, so the actual list ends up being [2, -4, -10, -14, -18]
    # This preserves the sign incase the closest vowel is BEFORE the letter.
    # The first element is the closest vowel. 2 in this case.
    # This final value is then added to the index of the letter i.e s = 18 so 18+2 = 20 (index for u)
    # and index into the LETTERS list and return it.
    closest_vowels = sorted(map(lambda v: v - index, VOWELS), key=lambda x: abs(x))
    return LETTERS[closest_vowels[0] + index]


class NearestVowelTest(unittest.TestCase):
    def test_nearest_vowel(self) -> None:
        self.assertEqual(nearest_vowel("b"), "a")
        self.assertEqual(nearest_vowel("s"), "u")
        self.assertEqual(nearest_vowel("c"), "a")
        self.assertEqual(nearest_vowel("i"), "i")


if __name__ == "__main__":
    unittest.main()
