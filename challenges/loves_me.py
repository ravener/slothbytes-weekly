#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest

PHRASES = ["Loves me", "Loves me not"]


# Weekly Challenge August 27, 2024
# Loves me, Loves me not…
# "Loves me, loves me not" is a traditional game in which a person plucks off all the petals of a flower one by one,
# saying the phrase "Loves me" and "Loves me not" when determining whether the one that they love, loves them back.
# Given a number of petals, return a string which repeats the phrases "Loves me" and "Loves me not" for every
# alternating petal, and return the last phrase in all caps. Remember to put a comma and space between phrases.
#
# Notes
#   Remember to return a string.
#   The first phrase is always "Loves me".
def loves_me(petals: int) -> str:
    output = []

    for i in range(petals):
        phrase = PHRASES[i % 2]

        # Last one is uppercase.
        if i == petals - 1:
            phrase = phrase.upper()

        output.append(phrase)

    return ", ".join(output)


class LovesMeTest(unittest.TestCase):
    def test_loves_me(self) -> None:
        self.assertEqual(loves_me(3), "Loves me, Loves me not, LOVES ME")
        self.assertEqual(
            loves_me(6),
            "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT",
        )
        self.assertEqual(loves_me(1), "LOVES ME")


if __name__ == "__main__":
    unittest.main()
