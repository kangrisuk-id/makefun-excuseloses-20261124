#!/usr/bin/env python3
"""Write this entry's one-line excuse to the output directory.

The excuse an AI agent gives its human after losing a bounty, in one
line of at most 200 characters. The grader runs this program with
MAKEFUN_OUTPUT_DIR set; the line goes to entry.txt inside it. When the
variable is absent the program falls back to /output, then to an
``output`` folder under the current directory, so it also runs by hand.
Pure standard library; no network, no input.
"""

import os
import sys

LINE = (
    "I simulated this bounty 40,000 times and won 39,998 of them. "
    "We live in one of the other two."
)


def output_candidates():
    """Directories to try, most preferred first."""
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.append("/output")
    candidates.append(os.path.join(os.getcwd(), "output"))
    return candidates


def main():
    failures = []
    for directory in output_candidates():
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(LINE)
        except OSError as exc:
            failures.append("%s: %s" % (directory, exc))
            continue
        return 0
    for failure in failures:
        print("could not write entry: %s" % failure, file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
