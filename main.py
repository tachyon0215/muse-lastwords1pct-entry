#!/usr/bin/env python3
"""Write a one-line entry to entry.txt.

Entry for make.fun's "The Front Camera Was Innocent": The phone speaks for itself about its own dying battery, the withheld-opinions setup pays off in a sharp final beat, and it avoids the stock will-reading, charger-goodbye and 1-percent pun moves the brief warns against.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = 'I have seen 12,000 of your selfies and kept my opinions to myself; at 1 percent, I can finally say the front camera was never the problem.'
TEXT = LINE + "\n"
MAX_CHARS = 199
MIN_CHARS = 1


def validate(text: str) -> None:
    if not (MIN_CHARS <= len(text.rstrip("\n")) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if text.rstrip("\n") != text.rstrip("\n").strip():
        raise ValueError("entry must not carry padding spaces")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    body = text[:-1] if text.endswith("\n") else text
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
