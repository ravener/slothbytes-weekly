#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest

vowels: list[str] = ["a", "e", "i", "o", "u"]


# Weekly Challenge October 8, 2024
# pigLatin
# Write a function that converts a sentence into pig latin.
#
# Rules for converting to pig latin:
#  For words that begin with a vowel (a, e, i, o, u), add "way".
#  Otherwise, move all letters before the first vowel to the end and add "ay".
#  For simplicity, no punctuation will be present in the inputs.
#
# Notes
#   All letters will be in lowercase.
def pig_latin_sentence(sentence: str) -> str:
    def map_word(word: str) -> str:
        # If it stars with a vowel
        if word[0].lower() in vowels:
            return word + "way"
        else:
            # Look for the first vowel
            first_vowel = next(i for i, char in enumerate(word) if char in vowels)
            # After the vowel + Before the first vowel + ay
            return word[first_vowel:] + word[:first_vowel] + "ay"

    # Split the sentence into words, map them, join them back into a sentence.
    return " ".join(map(map_word, sentence.split(" ")))


class PigLatinSentenceTest(unittest.TestCase):
    def test_pig_latin_sentence(self) -> None:
        self.assertEqual(
            pig_latin_sentence("this is pig latin"), "isthay isway igpay atinlay"
        )
        self.assertEqual(
            pig_latin_sentence("wall street journal"), "allway eetstray ournaljay"
        )


if __name__ == "__main__":
    unittest.main()
