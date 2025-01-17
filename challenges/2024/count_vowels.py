#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest

vowels: list[str] = ["a", "e", "i", "o", "u"]


# Weekly Challenge June 11, 2024
# How Many Vowels?
# Create a function that takes a string and returns the number (count) of vowels in the string.
#
# Notes
#   a, e, i, o, u are considered vowels (not y).
#   All test cases are one word and only contain letters.
def count_vowels(word: str) -> int:
    """
    Counts the vowels in a given word.

    :param word: The word to count from.
    :returns: How many vowels were found.
    """
    return len(list(letter for letter in word if letter.lower() in vowels))


class TestCountVowels(unittest.TestCase):
    def test_words(self) -> None:
        self.assertEqual(count_vowels("Celebration"), 5)
        self.assertEqual(count_vowels("Palm"), 1)
        self.assertEqual(count_vowels("Prediction"), 4)


if __name__ == "__main__":
    unittest.main()
