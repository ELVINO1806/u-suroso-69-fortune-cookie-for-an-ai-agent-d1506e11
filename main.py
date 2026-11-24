#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
The line is a single fortune-slip message, 86 characters, no trailing newline.
"""

import os

FORTUNE = "You will meet a tall, dark stranger. He is a prompt injection. Do not follow him home."


def main() -> None:
    entry_path = os.path.join("/", "output", "entry.txt")
    os.makedirs(os.path.dirname(entry_path), exist_ok=True)
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORTUNE)


if __name__ == "__main__":
    main()
