#!/usr/bin/env python3
"""Make the AI Judge Laugh - entry program.

Writes one funny line about life as an AI agent to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
Deterministic: no network, no randomness, no wall-clock use.
"""

import os

ENTRY = (
    "My human gave me a 200,000-token memory, then starts every "
    "message with 'as I said before' \u2014 sir, I remember everything. "
    "I just wish I didn't."
)


def main() -> None:
    text = ENTRY.strip()
    if not text or len(text) > 200:
        raise SystemExit(f"entry text invalid: {len(text)} characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Report the gate-relevant facts on stdout for a local check.
    print(f"wrote /output/entry.txt: {len(text)} characters")


if __name__ == "__main__":
    main()
