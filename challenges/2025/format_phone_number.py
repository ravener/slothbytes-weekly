#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest
from collections.abc import Sequence


# Weekly Challenge February 18, 2025
# Phone Number Formatting
# Create a function that takes a list of 10 numbers (between 0 and 9) and
# returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).
#
# Notes
#   Don't forget the space after the closing parenthesis.
def format_phone_number(digits: Sequence[int]) -> str:
    assert len(digits) == 10
    to_str = lambda s: "".join(map(str, s))

    return f"({to_str(digits[:3])}) {to_str(digits[3:6])}-{to_str(digits[6:])}"


class FormatPhoneNumberTest(unittest.TestCase):
    def test_format_phone_number(self) -> None:
        self.assertEqual(
            format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890"
        )
        self.assertEqual(
            format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]), "(519) 555-4468"
        )
        self.assertEqual(
            format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]), "(345) 501-2527"
        )


if __name__ == "__main__":
    unittest.main()
