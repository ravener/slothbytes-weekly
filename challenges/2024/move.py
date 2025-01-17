#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


# Weekly Challenge June 18, 2024
# Change Every Letter to the Next Letter
# Write a function that changes every letter to the next letter:
#   "a" becomes "b"
#   "b" becomes "c"
#   "d" becomes "e"
#   and so on ...
#
# Notes
#   There will be no z's in the tests.
def move(word: str) -> str:
    """
    Changes every letter of the word to the next letter.

    :param word: The word to change.
    :returns: The word with its letters moved.
    """
    return "".join(chr(ord(letter) + 1) for letter in word)


class MoveTest(unittest.TestCase):
    def test_move(self) -> None:
        self.assertEqual(move("hello"), "ifmmp")
        self.assertEqual(move("bye"), "czf")
        self.assertEqual(move("welcome"), "xfmdpnf")


if __name__ == "__main__":
    unittest.main()
