#!/usr/bin/env python3
# -*- coding: utf8 -*-
import re
import unittest


# Weekly Challenge January 14, 2025
# Censor Words Longer Than Four Characters
# Create a function that takes a string and censors words over four characters with *.
#
# Notes
#   Don't censor words with exactly four characters.
#   If all words have four characters or less, return the original string.
#   The amount of * is the same as the length of the word.
def censor(text: str) -> str:
    return re.sub(r"\S{5,}", lambda x: "*" * len(x.group()), text)


class CensorTest(unittest.TestCase):
    def test_censor(self) -> None:
        self.assertEqual(censor("The code is fourty"), "The code is ******")
        self.assertEqual(censor("Two plus three is five"), "Two plus ***** is five")
        self.assertEqual(censor("aaaa aaaaa 1234 12345"), "aaaa ***** 1234 *****")


if __name__ == "__main__":
    unittest.main()
