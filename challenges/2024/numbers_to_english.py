#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


# Weekly Challenge October 29, 2024
# Numbers to English
# Write a function that accepts a positive integer between 0 and 999 inclusive and
# returns a string representation of that integer written in English.
# Notes
#   There are no hyphens used (e.g. "thirty five" not "thirty-five").
#   The word "and" is not used (e.g. "one hundred one" not "one hundred and one").
def num_to_eng(num: int) -> str:
    nums = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]

    tens_list = [
        "twenty",
        "thirty",
        "fourty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    if num < len(nums):
        return nums[num]

    output = []
    hundreds, remainder = divmod(num, 100)

    if hundreds:
        output.append(nums[hundreds])
        output.append("hundred")

    if remainder < len(nums):
        if remainder:
            output.append(nums[remainder])
        return " ".join(output)

    tens, ones = divmod(remainder, 10)
    output.append(tens_list[tens - 2])

    if ones:
        output.append(nums[ones])

    return " ".join(output)


class NumToEngTest(unittest.TestCase):
    def test_num_to_eng(self) -> None:
        self.assertEqual(num_to_eng(0), "zero")
        self.assertEqual(num_to_eng(18), "eighteen")
        self.assertEqual(num_to_eng(126), "one hundred twenty six")
        self.assertEqual(num_to_eng(909), "nine hundred nine")
        self.assertEqual(num_to_eng(100), "one hundred")


if __name__ == "__main__":
    unittest.main()
