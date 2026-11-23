#!/usr/bin/env python3
"""Write one real-life patch note to /output/entry.txt.

The entry is a single-line software-style changelog entry for a bug in
human biology: hair migrating from the scalp to the ears and nose after
age 40. Deterministic: the same bytes are written on every run.
Standard library only.
"""

import os
import stat

ENTRY = (
    "v1.2.8: fixed a bug where hair migrated from the scalp "
    "to the ears and nose after age 40."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (ENTRY + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
