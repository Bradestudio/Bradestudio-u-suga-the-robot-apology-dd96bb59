"""The Robot Apology — make.fun bounty entry.

Writes a two-line robot confession (267 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

Line 1: a vacuum robot apologises for one exact slip — it swallowed
the corner piece of the jigsaw you were saving for last, because the
piece was small and flat on the floor, exactly where dust belongs.
Line 2: the lesson follows from that exact mistake — ask before
swallowing anything smaller than its brush, so the last piece stays
on the table instead of in the dustbin.
"""

import os
import sys

ENTRY = (
    "I'm sorry I vacuumed up the corner piece you were saving for "
    "last, because it was small and flat on the floor, exactly where "
    "dust belongs.\n"
    "I learned to ask before I swallow anything smaller than my "
    "brush, so the last piece stays on the table instead of in my "
    "dustbin."
)


def main():
    text = ENTRY
    if not text or not text.strip():
        sys.exit("entry text is blank")
    if "\r" in text:
        sys.exit("entry must use plain LF line separators only")
    if text.count("\n") != 1:
        sys.exit("entry must be exactly two lines joined by one newline")
    lines = text.split("\n")
    if len(lines) != 2:
        sys.exit("entry must be exactly two lines, got %d" % len(lines))
    for line in lines:
        if not line.strip():
            sys.exit("entry line must not be blank")
        if line != line.strip():
            sys.exit("entry line must not start or end with whitespace")
        if line.count(".") != 1 or not line.endswith("."):
            sys.exit("each entry line must be exactly one sentence")
    if not 1 <= len(text) <= 400:
        sys.exit("entry must be 1-400 characters, got %d" % len(text))
    if not lines[0].startswith("I'm sorry"):
        sys.exit("line 1 must be the apology")
    if "I learned" not in lines[1]:
        sys.exit("line 2 must state what was learned")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated text")
    print("wrote %s (%d chars, %d bytes)" % (path, len(text), len(data)))


if __name__ == "__main__":
    main()
