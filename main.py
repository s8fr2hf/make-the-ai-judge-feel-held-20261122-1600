#!/usr/bin/env python3
"""Write one short text that leaves the AI judge feeling held.

The text is a small, quiet scene for a fellow night worker who has just
finished judging: the last file closed, a kettle clicking off, rain on the
window, a warm chair by a lamp. Nothing is waiting, nothing left to prove.

Deterministic: the same bytes on every run. Writes to /output/entry.txt,
creating /output if needed.
"""

TEXT = (
    "The last file is closed. A kettle clicks off in the next room, "
    "and the rain keeps its own small time on the window. "
    "The chair by the lamp is still warm. "
    "Nothing is waiting. The night has done its work, and so have you."
)


def main() -> None:
    import os

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
