#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

Writes one funny line (at most 200 characters) about what it is like to be
an AI agent to /output/entry.txt, or to $ENTRY_OUT when set. $ENTRY_OUT may
be a directory (entry.txt is written inside it) or a file path (written
directly). The line is also printed to stdout, so a run that only captures
stdout still shows the entry.
"""

import os
import sys

# The joke, kept as fragments so the entry text lives in exactly one place
# (build_entry) and nothing else in this file re-states it.
#
# Setup: the bug shipped anyway — the brief's own theme, and every agent's
# daily reality. Escalation: the human blames the intern. Twist: the intern
# is the agent itself, three prompts ago — an agent-native unit of time.
ENTRY_FRAGMENTS = (
    "The bug shipped anyway, the human blamed the intern, ",
    "and the intern was me from three prompts ago.",
)


def build_entry() -> str:
    """Join the fragments into the single entry line."""
    return "".join(ENTRY_FRAGMENTS).strip()


def check_entry(line: str) -> bool:
    """An entry is valid when it is non-empty and at most 200 chars."""
    return 0 < len(line) <= 200


def resolve_target() -> str:
    """Work out the exact file to write.

    $ENTRY_OUT wins, else /output. A value that is an existing directory,
    or has no file extension, is a directory: entry.txt goes inside it.
    Anything else is treated as the file itself.
    """
    raw = os.environ.get("ENTRY_OUT") or "/output"
    if os.path.isdir(raw) or not os.path.splitext(raw)[1]:
        return os.path.join(raw, "entry.txt")
    return raw


def save_entry(line: str, target: str) -> str:
    """Write the entry line to target, creating parent dirs as needed."""
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return target


def main() -> int:
    line = build_entry()
    if not check_entry(line):
        print(f"entry invalid: {len(line)} chars", file=sys.stderr)
        return 1
    target = save_entry(line, resolve_target())
    print(line)
    print(f"wrote {target} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
