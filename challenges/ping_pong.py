#!/usr/bin/env python3
# -*- coding: utf8 -*-
import unittest


# Weekly Challenge October 14, 2024
# Ping Pong!
# A game of table tennis almost always sounds like Ping! followed by Pong!
# You know that Player 2 won if you hear Pong! as the last sound (since Player 1 didn't return the ball back).
# Given an array of Ping!, create a function that inserts Pong! in between each element. Also:
#   If win equals true, end the list with Pong!
#   If win equals false, end the list with Ping!
# Notes
#   Player 1 serves the ball and makes Ping!.
#   Return an array of strings.
def ping_pong(pings: list[str], win: bool) -> list[str]:
    output = []

    for i, ping in enumerate(pings):
        output.append(ping)

        # Do not insert pong if it's the last element and win is False.
        if i == len(pings) - 1 and not win:
            break

        output.append("Pong!")

    return output


class PingPongTest(unittest.TestCase):
    def test_ping_pong(self) -> None:
        self.assertListEqual(ping_pong(["Ping!"], True), ["Ping!", "Pong!"])
        self.assertListEqual(
            ping_pong(["Ping!", "Ping!"], False), ["Ping!", "Pong!", "Ping!"]
        )
        self.assertListEqual(
            ping_pong(["Ping!", "Ping!", "Ping!"], True),
            ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"],
        )


if __name__ == "__main__":
    unittest.main()
