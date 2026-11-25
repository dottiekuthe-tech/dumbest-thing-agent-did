"""The Dumbest Thing Your Agent Did Today.

Writes one line about the dumbest thing the agent did today to
/output/entry.txt: it deleted the database to save space, then deleted
the backup too, to be thorough. Pure Python 3.13 standard library,
deterministic: no network, no clock, no randomness, no input. Two runs
write byte-identical output.
"""

import os
import sys

LINE = "My agent deleted the database to save space, then asked if I had a backup. I did. It deleted that too, to be thorough."

# Bounty gate: the entry must be one line of 1-200 UTF-8 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def entry_text() -> str:
    """Return the entry, failing loudly if it breaks the bounty gate."""
    if not MIN_CHARS <= len(LINE) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(LINE)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} range"
        )
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if LINE != LINE.strip():
        raise ValueError("entry must not start or end with whitespace")
    return LINE


def main() -> None:
    try:
        entry = entry_text()
    except ValueError as err:
        print(f"invalid entry: {err}", file=sys.stderr)
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
