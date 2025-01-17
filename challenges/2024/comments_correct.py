#!/usr/bin/env python3
# -*- coding: utf8 -*-
import textwrap
import unittest


# Weekly Challenge November 19, 2024
# Valid JavaScript Comments
# In JavaScript, there are two types of comments:
#   Single-line comments start with //
#   Multi-line or inline comments start with /* and end with */
#
# The input will be a sequence of //, /* and */. Every /* must have a */ that immediately follows it.
# To add, there can be no single-line comments in between multi-line comments in between the /* and */.
# Create a function that returns True if comments are properly formatted, and False otherwise.
def comments_correct(input: str) -> bool:
    # Split into chunks of 2 characters at a time
    chunks = textwrap.fill(input, 2).split()
    is_in_comment = False

    for chunk in chunks:
        if chunk == "/*":
            if is_in_comment:
                return False  # Comments cannot nest

            is_in_comment = True
        elif chunk == "*/":
            is_in_comment = False
        elif chunk == "//":
            # No single line comments in between multi-line comments
            if is_in_comment:
                return False
        else:
            # Anything else is invalid
            return False

    if is_in_comment:
        # Failed to close the multi-line comment
        return False

    return True


class CommentsCorrectTest(unittest.TestCase):
    def test_comments_correct(self) -> None:
        self.assertTrue(comments_correct("//////"))
        self.assertTrue(comments_correct("/**//**////**/"))
        self.assertFalse(comments_correct("///*/**/"))
        self.assertFalse(comments_correct("/////"))


if __name__ == "__main__":
    unittest.main()
