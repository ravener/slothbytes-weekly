#!/usr/bin/env python3
# -*- coding: utf8 -*-
import re
import unittest

pattern = re.compile(r"^(:|;)(-|~)?(\)|D)$")


# Weekly Challenge August 6, 2024
# Count the Smiley Faces :)
# Create a function that takes an array of strings and return the number of smiley faces contained within it.
# These are the components that make up a valid smiley:
# - A smiley has eyes. Eyes can be : or ;
# - A smiley has a nose but it doesn't have to. A nose can be - or ~
# - A smiley has a mouth which can be ) or D
# No other characters are allowed except for those mentioned above.
def count_smileys(arr: list[str]) -> int:
    return len(list(filter(lambda x: pattern.match(x), arr)))


class CountSmileysTest(unittest.TestCase):
    def test_count_smileys(self) -> None:
        self.assertEqual(2, count_smileys([":)", ";(", ";}", ":-D"]))
        self.assertEqual(3, count_smileys([";D", ":-(", ":-)", ";~)"]))
        self.assertEqual(1, count_smileys([";]", ":[", ";*", ":$", ";-D"]))


if __name__ == "__main__":
    unittest.main()
