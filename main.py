#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast for an invented city to
$OUTPUT_DIR/entry.txt (default /output). Pure Python 3.13 stdlib only.
"""

import os
import sys

LINE = (
    "In Drizlebury, steady rain today, falling upward from noon; "
    "commuters are advised to wear their umbrellas underneath."
)


def _strip_controls(line: str) -> str:
    """Remove control characters (keeping tab) so none can leak into entry.txt."""
    return "".join(ch for ch in line if ch == "\t" or ord(ch) >= 0x20)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = _strip_controls(LINE).encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
