#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


# Weekly Challenge June 4, 2024
# Fizz Buzz
# This is a classic problem that some companies even use as a warm up before an interview.
#
# Given an integer n, return a string array answer (1-indexed) where:
#   answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#   answer[i] == "Fizz" if i is divisible by 3.
#   answer[i] == "Buzz" if i is divisible by 5.
#   answer[i] == i (as a string) if none of the above conditions are true.
def fizzbuzz(n: int) -> list[str]:
    """
    Creates a list that contains the fizzbuzz sequence up to n.

    :param n: The sequence continues until n.
    :returns: A list containing the fizzbuzz sequence.
    """
    return [
        "FizzBuzz"
        if i % 3 == 0 and i % 5 == 0
        else "Fizz"
        if i % 3 == 0
        else "Buzz"
        if i % 5 == 0
        else str(i)
        for i in range(1, n + 1)
    ]


class FizzBuzzTest(unittest.TestCase):
    def test_fizzbuzz(self) -> None:
        self.assertEqual(fizzbuzz(3), ["1", "2", "Fizz"])
        self.assertEqual(fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"])
        self.assertEqual(
            fizzbuzz(15),
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        )


if __name__ == "__main__":
    unittest.main()
