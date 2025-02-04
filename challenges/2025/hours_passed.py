#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest
from datetime import datetime


# Weekly Challenge January 28, 2025
# Amateur Hour
# Write a function that takes time t1 and time t2 and returns the number of hours passed between the two times.
#
# Notes
#   Time t1 will always be the starting time and t2, the ending time.
#   Return the string "no time passed" if t1 is equal to t2.
def hours_passed(t1: str, t2: str) -> str:
    format_str = "%I:%M %p"
    time1 = datetime.strptime(t1, format_str)
    time2 = datetime.strptime(t2, format_str)

    hours = (time2 - time1).seconds // 3600

    return f"{hours} hours" if hours > 0 else "no time passed"


class HoursPassedTest(unittest.TestCase):
    def test_hours_passed(self) -> None:
        self.assertEqual(hours_passed("3:00 AM", "9:00 AM"), "6 hours")
        self.assertEqual(hours_passed("2:00 PM", "4:00 PM"), "2 hours")
        self.assertEqual(hours_passed("1:00 AM", "3:00 PM"), "14 hours")
        self.assertEqual(hours_passed("4:00 PM", "4:00 PM"), "no time passed")


if __name__ == "__main__":
    unittest.main()
