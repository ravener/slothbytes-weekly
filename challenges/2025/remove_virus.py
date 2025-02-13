#!/usr/bin/env python3
# -*- coding: utf8 -*-
import re
import unittest


# Weekly Challenge February 11, 2025
# Remove the Computer Virus
# Your computer might have been infected by a virus!
# Create a function that finds the viruses in files and removes them from your computer.
#
# Notes
#   Bad files will contain "virus" or "malware", but "antivirus" and "notvirus" will not be viruses.
#   Return "PC Files: Empty" if there are no files left on the computer.
def remove_virus(files: str) -> str:
    file_names = files[10:].split(", ")

    def is_virus(name: str) -> bool:
        if "virus" in name:
            if "antivirus" in name or "notvirus" in name:
                return False
            return True

        return "malware" in name

    good_files = list(filter(lambda f: not is_virus(f), file_names))

    if not good_files:
        good_files = ["Empty"]

    return f"PC Files: {', '.join(good_files)}"


class RemoveVirusTest(unittest.TestCase):
    def test_remove_virus(self) -> None:
        self.assertEqual(
            remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"),
            "PC Files: spotifysetup.exe, dog.jpg",
        )

        self.assertEqual(
            remove_virus(
                "PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe "
            ),
            "PC Files: antivirus.exe, cat.pdf",
        )

        self.assertEqual(
            remove_virus("PC Files: notvirus.exe, funnycat.gif"),
            "PC Files: notvirus.exe, funnycat.gif",
        )


if __name__ == "__main__":
    unittest.main()
