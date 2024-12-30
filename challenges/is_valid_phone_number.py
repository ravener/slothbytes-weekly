#!/usr/bin/env python3
# -*- coding: utf8 -*-
import re
import unittest


# Weekly Challenge December 10, 2024
# Is the Phone Number Formatted Correctly?
# Create a function that accepts a string and returns true if it's in the format of a proper phone number and false if it's not. Assume any number between 0-9 (in the appropriate spots) will produce a valid phone number.
# This is what a valid phone number looks like:
#   (123) 456-7890
#
# Notes
#   Don't forget the space after the closing parenthesis.
def is_valid_phone_number(phone_number: str) -> bool:
    return re.match(r"^\(\d{3}\) \d{3}-\d{4}$", phone_number) is not None


class IsValidPhoneNumberTest(unittest.TestCase):
    def test_is_valid_phone_number(self) -> None:
        self.assertTrue(is_valid_phone_number("(123) 456-7890"))
        self.assertFalse(is_valid_phone_number("1111)555 2345"))
        self.assertFalse(is_valid_phone_number("098) 123 4567"))


if __name__ == "__main__":
    unittest.main()
