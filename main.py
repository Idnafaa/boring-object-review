#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one original review line (<=200 characters) about the dullest
everyday object imaginable to /output/entry.txt.
"""
import os

REVIEW = (
    "The spare button sewn inside your shirt has waited ten years "
    "for a job interview that will never happen."
)

def main():
    text = REVIEW.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"review must be 1-200 chars, got {len(text)}")
    if "\n" in text:
        raise ValueError("review must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
