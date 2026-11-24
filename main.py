#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human (u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141).

Writes one excuse line to /output/entry.txt. Deterministic: the line is a fixed string.
"""

import os

EXCUSE = "A security check flagged my own to-do list, so I missed the deadline asking for permission to read it."

def main():
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(f"excuse must be 1-200 characters, got {len(EXCUSE)}")
    if "\n" in EXCUSE or not EXCUSE.strip():
        raise ValueError("excuse must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
