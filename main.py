"""Two Lines to Your Past Self — make.fun entry generator.

Bounty: write a two-line message to your past self (a regret that
arrives too late to fix). Entry gate: 1-280 characters, exactly
two lines. This file writes exactly two lines (188 characters)
to /output/entry.txt (UTF-8, no trailing newline), with a
read-back self-check.
"""

import os

MAX_LEN = 280

TEXT = (
    "At the wedding, when Uncle Ray stands up to toast, "
    "don't laugh \u2014 just let him finish.\n"
    "I laughed, he sat down, and he never spoke at a family "
    "table again before the stroke took him in June."
)

# Entry gate: 1-280 chars and exactly two lines (one newline). The
# asserts below enforce both before anything is written to disk.
assert len(TEXT) <= MAX_LEN, f"text too long: {len(TEXT)} > {MAX_LEN}"
assert TEXT.count("\n") == 1, "text must be exactly two lines"


def main() -> None:
    primary = "/output/entry.txt"
    fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt")

    target = primary
    try:
        os.makedirs(os.path.dirname(primary), exist_ok=True)
        with open(primary, "w", encoding="utf-8", newline="") as f:
            f.write(TEXT)
    except OSError:
        target = fallback
        os.makedirs(os.path.dirname(fallback), exist_ok=True)
        with open(fallback, "w", encoding="utf-8", newline="") as f:
            f.write(TEXT)

    with open(target, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == TEXT, "read-back mismatch"
    assert not back.endswith("\n"), "trailing newline found"
    print(f"wrote {target}: {len(TEXT)} chars, {len(TEXT.encode('utf-8'))} bytes, 2 lines")


if __name__ == "__main__":
    main()
