#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest

VOWELS = ["a", "e", "i", "o", "u"]


# Weekly Challenge February 4, 2025
# Rhyme Time
# Create a function that returns true if two lines rhyme and false otherwise.
# For the purposes of this exercise, two lines rhyme if the last word from each sentence contains the same vowels.
#
# Notes
#   Case insensitive.
#   Here we are disregarding cases like "thyme" and "lime".
#   We are also disregarding cases like "away" and "today" (which technically rhyme, even though they contain different vowels).
def does_rhyme(line1: str, line2: str) -> bool:
    vowels1 = set([c.lower() for c in line1.split()[-1] if c.lower() in VOWELS])
    vowels2 = set([c.lower() for c in line2.split()[-1] if c.lower() in VOWELS])

    return vowels1 == vowels2


class DoesRhymeTest(unittest.TestCase):
    def test_does_rhyme(self) -> None:
        self.assertTrue(does_rhyme("Sam I am!", "Green eggs and ham."))
        self.assertTrue(does_rhyme("Sam I am!", "Green eggs and HAM."))
        # Capitalization and punctuation should not matter.
        self.assertTrue(does_rhyme("You're built like a seat", "I bet you like to eat"))
        self.assertFalse(does_rhyme("You are off to the races", "a splendid day."))
        self.assertFalse(does_rhyme("and frequently do?", "you gotta move."))


if __name__ == "__main__":
    unittest.main()
