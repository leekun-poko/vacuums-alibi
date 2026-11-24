# One-line entry for "The Vacuum's Alibi" (program/v1).
# Writes a single line in which a robot vacuum explains why it
# missed a spot, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
# Pure Python stdlib, deterministic: no clock, no randomness, no network.
import os

OPENING = "Log 14:02: Corner uncleaned. "
MIDDLE = (
    "The dust formed a union, elected a crumb, and served me "
    "a restraining order. I do not cross picket lines. "
)
ENDING = "I am a vacuum, not a scab."
LINE = OPENING + MIDDLE + ENDING


def main() -> None:
    # One line only: the gate counts 1-200 code points, and LINE is 161.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE and LINE.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
