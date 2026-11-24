"""The Excuse an AI Agent Gives Its Human.

One line: the excuse an AI agent gives its human for missing a deadline.
Writes it to /output/entry.txt (UTF-8, one line, 1-200 characters).
"""

import os

# The excuse: one retry loop, one visible moment (the blinking cursor at
# 3 a.m.), three concrete specifics (7 retries, 3 a.m., 412 blinks),
# and the turn in the final clause.
ENTRY_TEXT = "I burned all 7 retries by 3 a.m. watching the cursor blink 412 times, and the deadline got bored and left without me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
