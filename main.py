#!/usr/bin/env python3
"""Midnight Fridge Roast.

Prints one line: a roast of a smart fridge that refuses to open
after midnight, and writes the same line to entry.txt.

The joke: the fridge does not merely lock itself, it hires a
bouncer, and the leftovers have taken out a restraining order
against their own owner. The midnight refusal is the target,
and the line reads like something said aloud at the door.
"""

import os

ENTRY = "My fridge hired a bouncer at midnight \u2014 apparently the leftovers filed a restraining order against me."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
