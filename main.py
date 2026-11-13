# ai-joke-03 entry (Python 3.13, standard library only): writes one fixed
# one-liner about AI coding agents to /output/entry.txt.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The gate takes UTF-8 text of 1 to 280 characters that is not only white
# space, and the judge reads exactly the bytes written, so the joke is
# written as raw bytes with no trailing line end.

import os
from pathlib import Path

JOKE = "My coding agent wrote 40,000 lines this week. I've read eleven of them. I approved all 40,000."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    (output_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
