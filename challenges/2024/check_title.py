#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


# Weekly Challenge July 23, 2024
# Check If It's a Title String
# Check if a string is formatted as a title.
# A title string is when every word of the string start with a upper case letter.
def check_title(sentence: str) -> bool:
    """
    Checks if the given sentence is a title string.
    A title string is when every word of the string start with a upper case letter.

    :param sentence: The sentence to check.
    :returns: True if the sentence is a title string.
    """
    return all(map(lambda word: word[0].isupper(), sentence.split()))


class CheckTitleTest(unittest.TestCase):
    def test_check_title(self) -> None:
        self.assertTrue(check_title("A Mind Boggling Achievement"))
        self.assertTrue(check_title("A Simple C++ Program!"))
        self.assertFalse(check_title("Water is transparent"))


if __name__ == "__main__":
    unittest.main()
