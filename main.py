#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands.

Writes a single cat joke (one line, under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt.

The joke: a cat hired as a therapist. Setup: therapy framing with
treats and a therapist who naps through every session. Turn: the
"advice" is the classic cat move of knocking things off a table --
applied to the owner's problems, then staring at them on the floor.
Tightened in revision: "falls asleep mid-session" became "naps
through every session", which lands the laziness harder in fewer
syllables and keeps the punchline's rhythm.
"""

import os

JOKE = (
    "I hired my cat as my therapist \u2014 he charges in treats, "
    "naps through every session, and his only advice is to knock "
    "my problems off the table and stare at them on the floor."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
