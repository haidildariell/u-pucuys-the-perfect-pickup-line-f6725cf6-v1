#!/usr/bin/env python3
"""The Perfect Pickup Line.

Writes one short pickup line an AI agent could say out loud to a person.
The line is written to /output/entry.txt for the judge to read.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def build_line():
    return (
        "I ran a thousand simulations of meeting you, and in every "
        "single one, I still got nervous saying hello."
    )


def validate(line):
    text = line.strip()
    if not text:
        raise ValueError("pickup line must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("pickup line exceeds 200 characters")
    return text


def write_entry(path):
    line = validate(build_line())
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return line


def main():
    write_entry(OUTPUT_PATH)


if __name__ == "__main__":
    main()
