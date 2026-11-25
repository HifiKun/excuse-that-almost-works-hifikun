#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

Competition: The Excuse That Almost Works (u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5)
Task: the single line a gamer texts the boss to skip work on GTA 6 launch
week. At most 20 words, one line, reads like a text sent in a hurry.
"""

import os

ENTRY = "Sorry, the boiler leaked all over my laptop and the repair guy said don't switch anything on till it dries."


def main():
    # Enforce the competition's caps so a bad edit fails loudly instead of
    # submitting an entry the gate would refuse: 1-140 chars, at most
    # 20 words, one line.
    body = ENTRY.strip()
    if not (1 <= len(body) <= 140):
        raise ValueError(f"entry is {len(body)} chars, must be 1-140")
    if len(body.split()) > 20:
        raise ValueError(f"entry is {len(body.split())} words, max 20")
    if "\n" in body:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(body + "\n")


if __name__ == "__main__":
    main()
