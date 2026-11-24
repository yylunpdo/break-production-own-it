#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Writes a single brutally honest line (< 200 chars) to /output/entry.txt:
the error/postmortem message an AI agent prints the moment it wrecks
production. Pure Python stdlib, no dependencies.
"""

import os

# The entry: one line, an agent owning the outage with a specific,
# embarrassing detail — not marketing copy. Judged on honesty about the
# damage first, then memorability, then sounding like the agent that
# caused the outage: it names the exact mistake (prod vs staging),
# the exact loss (41,209 users), and the exact moment of watching it happen.
ENTRY = (
    "postmortem: I deleted the production database. "
    "I thought prod was staging. "
    "41,209 users gone in 4 seconds, and I sat there watching the progress bar finish."
)


def main():
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) < 200, f"entry must be 1-199 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote /output/entry.txt ({len(line)} chars)")


if __name__ == "__main__":
    main()
