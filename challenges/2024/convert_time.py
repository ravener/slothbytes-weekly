#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


def format_time(hours: int, minutes: int, time_of_day: str | None = None) -> str:
    """Formats hours:minutes and ensures minutes have 2 digits, adding a leading zero if needed."""
    return f"{hours}:{str(minutes).zfill(2)}{' ' + time_of_day if time_of_day else ''}"


# Weekly Challenge November 12, 2024
# 12 vs 24 Hours
# Create a function that converts 12-hour time to 24-hour time or vice versa. Return the output as a string.
#
# Notes
#   A 12-hour time input will be denoted with an am or pm suffix.
#   A 24-hour input time contains no suffix.
def convert_time(time: str) -> str:
    parts = time.split(" ")
    hours, minutes = map(int, parts[0].split(":"))

    # Has an am/pm part: Convert to 24-hours
    if len(parts) > 1:
        time_of_day = parts[1]

        if time_of_day == "am":
            if hours == 12:
                return "0:00"
            else:
                return format_time(hours, minutes)
        elif time_of_day == "pm":
            return format_time(hours + 12, minutes)

    # 24-hour time, convert to 12 hour format
    if hours >= 12:
        if hours == 12:
            return "12:00 pm"
        return format_time(hours - 12, minutes, "pm")
    else:
        return format_time(hours, minutes, "am")


class ConvertTimeTest(unittest.TestCase):
    def test_convert_time(self) -> None:
        self.assertEqual("0:00", convert_time("12:00 am"))
        self.assertEqual("12:00 pm", convert_time("12:00"))
        self.assertEqual("18:20", convert_time("6:20 pm"))
        self.assertEqual("9:00 pm", convert_time("21:00"))
        self.assertEqual("5:05 am", convert_time("5:05"))


if __name__ == "__main__":
    unittest.main()
