#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


# Weekly Challenge December 3, 2024
# Invert Colors
# Create a function that inverts the rgb values of a given list
#
# Notes
#   Must return a list.
#   255 is the max value of a single color channel.
def color_invert(color: list[int]) -> list[int]:
    """
    Inverts the given list of R, G, B values and
    returns a new list with the inverted channels.
    """
    assert len(color) == 3
    return [255 - color[0], 255 - color[1], 255 - color[2]]


class ColorInvertTest(unittest.TestCase):
    def test_color_invert(self) -> None:
        self.assertListEqual(color_invert([255, 255, 255]), [0, 0, 0])
        self.assertListEqual(color_invert([0, 0, 0]), [255, 255, 255])
        self.assertListEqual(color_invert([165, 170, 221]), [90, 85, 34])


if __name__ == "__main__":
    unittest.main()
