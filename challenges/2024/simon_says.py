#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


# Weekly Challenge October 22, 2024
# Simon Says
# Simon asks you to perform operations on a list of numbers that only he tells you.
# You should ignore all other instructions given.
# Create a function which evaluates a list of commands (written in plain English) if the command begins with Simon says.
# Return the result as an integer.
# Notes
#   If no instructions are given by Simon, return 0.
#   For the sake of simplicity, there will be no command for dividing.
def simon_says(instructions: list[str]) -> int:
    output = 0

    for instruction in instructions:
        if instruction.startswith("Simon says"):
            words = instruction.split(" ")
            command = words[2]

            if command == "add":
                output += int(words[3])
            elif command == "subtract":
                output -= int(words[3])
            elif command == "multiply":
                output *= int(words[4])

    return output


class SimonSaysTest(unittest.TestCase):
    def test_simon_says(self) -> None:
        self.assertEqual(
            10, simon_says(["Simon says add 4", "Simon says add 6", "Then add 5"])
        )

        self.assertEqual(
            24,
            simon_says(
                ["Susan says add 10", "Simon says add 3", "Simon says multiply by 8"]
            ),
        )

        self.assertEqual(
            0,
            simon_says(
                [
                    "Firstly, add 4",
                    "Simeon says subtract 100",  # Look at the name closely :)
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
