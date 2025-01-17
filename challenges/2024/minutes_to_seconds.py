#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


# Weekly Challenge September 24, 2024
# Video Length in Seconds
# You are given the length of a video in minutes. The format is mm:ss (ex: "02:54").
# Create a function that takes the video length and return it in seconds.
# Notes
#  The video length is given as a string.
#  If the number of seconds is 60 or over, return -1.
#  You may get a number of minutes over 99 (e.g. "121:49" is perfectly valid).
def minutes_to_seconds(video_length: str) -> int:
    minutes, seconds = map(int, video_length.split(":"))

    if seconds >= 60:
        return -1

    return (minutes * 60) + seconds


class MinutesToSecondsTest(unittest.TestCase):
    def test_minutes_to_seconds(self) -> None:
        self.assertEqual(minutes_to_seconds("01:00"), 60)
        self.assertEqual(minutes_to_seconds("13:56"), 836)
        self.assertEqual(minutes_to_seconds("10:60"), -1)
        self.assertEqual(minutes_to_seconds("121:49"), 7309)


if __name__ == "__main__":
    unittest.main()
