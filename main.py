"""Two Robots in an Elevator.

make.fun bounty u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f.

Design: the entry is one fixed line of plain text -- a piece of awkward
small talk one robot says to another while they ride an elevator together.
The line was chosen by a local tournament over 22 freshly written
candidates, judged against the bounty judge's own brief (a real robot
elevator line first, then machine logic showing through, then the
awkwardness landing, then a laugh on the first read with a surprising
turn, then a tight single line). The winner is a robot that rehearsed its
one line 47 times, delivers the most generic small talk possible, and
then undercuts it: there are no windows in the elevator at all. No
setup, nothing to explain afterwards, 105 characters.

The program is deliberately boring: no input, no randomness, no network,
no clock, no files read. It writes the single winning line to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output/entry.txt`` when the variable
is unset), so two runs are byte-identical by construction.
"""

import os

# The winning line (105 characters, one line, plain UTF-8 text).
# Chosen by the local tournament in ../CANDIDATES.md (playoff record 4-0).
ENTRY = "I rehearsed this ride 47 times. 'Nice weather' was the best line I had, and there are no windows in here."


def main() -> int:
    # Gate self-check: the sealed scorer only accepts 1-200 characters.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip() or "\n" in ENTRY:
        raise SystemExit("entry violates the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
