#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


# Weekly Challenge November 5, 2024
# Ctrl + C, Ctrl + V
# Given a sentence containing few instances of "Ctrl + C" and "Ctrl + V",
# return the sentence after those keyboard shortcuts have been applied!
#
#   "Ctrl + C" will copy all text behind it.
#   "Ctrl + V" will do nothing if there is no "Ctrl + C" before it.
#   A "Ctrl + C" which follows another "Ctrl + C" will overwrite what it copies.
#
# Notes
#   Keyboard shortcut commands will appear like normal words in a sentence but shouldn't be copied themselves (see example #2).
#   Pasting should add a space between words.
def keyboard_shortcut(sentence: str) -> str:
    clipboard = None
    words = sentence.split()
    new_sentence = []
    in_command = False

    for i, word in enumerate(words):
        # If we are in the middle of a command, ignore the coming parts.
        if in_command and word in ["C", "V", "+"]:
            # C/V are the last parts so we exit command mode.
            if word in ["C", "V"]:
                in_command = False
            continue

        if word == "Ctrl":
            in_command = True
            # The actual command is two words ahead (skip the + sign)
            command = words[i + 2]

            if command == "C":
                # Update the clipboard with a copy of what we have so far.
                clipboard = new_sentence[:]
            elif command == "V":
                # If there's anything in our clipboard, extend our sentence with it.
                if clipboard:
                    new_sentence.extend(clipboard)
        else:
            new_sentence.append(word)

    return " ".join(new_sentence)


class KeyboardShortcutTest(unittest.TestCase):
    def test_keyboard_shortcut(self) -> None:
        self.assertEqual(
            keyboard_shortcut("the egg and Ctrl + C Ctrl + V the spoon"),
            "the egg and the egg and the spoon",
        )

        self.assertEqual(
            keyboard_shortcut("WARNING Ctrl + V Ctrl + C Ctrl + V"), "WARNING WARNING"
        )

        self.assertEqual(
            keyboard_shortcut("The Ctrl + C Ctrl + V Town Ctrl + C Ctrl + V"),
            "The The Town The The Town",
        )


if __name__ == "__main__":
    unittest.main()
