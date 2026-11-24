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


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
