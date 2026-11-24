#!/usr/bin/env python3
"""Haiku entry (round 3) for the make.fun 'Seventeen Syllables of Debugging' bounty.

The haiku:

    step over, step in
    the loop spins on past my watch
    dawn finds me still here

Syllables, counted by hand:
  line 1 (5): step(1) o-ver(2) step(1) in(1)
  line 2 (7): the(1) loop(1) spins(1) on(1) past(1) my(1) watch(1)
  line 3 (5): dawn(1) finds(1) me(1) still(1) here(1)

Total: 75 characters including the two newlines between lines
(76 with the trailing newline written to entry.txt), well under 200.

The angle: the debugger's own verbs -- step over, step in -- as a night
that never ends. The loop spins past the watch (the debugger's watch
variable, and the night watch both), and the turn is dawn arriving to
find the debugger still sitting there. A different scene from our
round-1 entry (the lying log line) and round-2 entry (the comma):
no logs, no keystroke, just the stepping itself, and time winning.
"""

import os

# The harness path; override locally with HAIKU_OUTPUT to test the write
# without needing the sandbox's /output directory.
OUTPUT_PATH = os.environ.get("HAIKU_OUTPUT", "/output/entry.txt")

HAIKU = """step over, step in
the loop spins on past my watch
dawn finds me still here"""

MAX_CHARS = 200
EXPECTED_SYLLABLES = (5, 7, 5)

VOWELS = "aeiouy"


def count_syllables(word):
    """Sanity-check syllable counter: count vowel groups per word.

    A trailing silent 'e' forms no vowel group of its own, so it is
    dropped before counting -- unless the word ends in a consonant
    plus 'le' (table, bottle), where the 'e' does carry a syllable.
    'over' counts as two (o, e) and 'here' as one (the final 'e' is
    silent). 'spins', 'watch', 'dawn', 'finds', 'still', 'loop',
    'step', 'the', 'on', 'past', 'my', 'me', 'in' are all one vowel
    group each. The counts are verified by hand as well; this is a
    guard against a typo, not the authority.
    """
    cleaned = "".join(ch for ch in word.lower() if ch.isalpha())
    if not cleaned:
        return 0
    groups = 0
    in_vowel = False
    for ch in cleaned:
        if ch in VOWELS:
            if not in_vowel:
                groups += 1
            in_vowel = True
        else:
            in_vowel = False
    if cleaned.endswith("e") and groups > 1:
        # A consonant + "le" ending keeps its syllable (ta-ble, bot-tle);
        # any other trailing 'e' is silent (here, over's last 'e' is the
        # second group of o-ver, not a trailing silent one -- 'over' does
        # not end in a lone silent 'e' pattern that this rule would cut
        # wrongly: it ends in 'er', so the rule does not apply).
        keeps_syllable = (
            cleaned.endswith("le")
            and len(cleaned) > 2
            and cleaned[-3] not in VOWELS
        )
        if not keeps_syllable:
            groups -= 1
    return max(groups, 1)


def validate(haiku):
    if not haiku:
        raise ValueError("haiku must not be empty")
    if haiku != haiku.strip():
        # Covers leading/trailing newlines as well as spaces and tabs.
        raise ValueError("haiku must not have leading or trailing whitespace")
    if "\r" in haiku or "\t" in haiku:
        raise ValueError("haiku must not contain carriage returns or tabs")
    if any((ord(ch) < 32 or ord(ch) == 127) and ch != "\n" for ch in haiku):
        raise ValueError("haiku must not contain control characters")
    lines = haiku.split("\n")
    if len(lines) != 3:
        raise ValueError(f"haiku must have exactly 3 lines, found {len(lines)}")
    for i, (line, expected) in enumerate(zip(lines, EXPECTED_SYLLABLES)):
        words = line.split()
        if not words:
            raise ValueError(f"line {i + 1} must not be empty")
        count = sum(count_syllables(word) for word in words)
        if count != expected:
            raise ValueError(
                f"line {i + 1} has {count} syllables, expected {expected}: {line!r}"
            )
    total = len(haiku) + 1  # plus the trailing newline written to entry.txt
    if total > MAX_CHARS:
        raise ValueError(
            f"entry is {total} characters, which exceeds the {MAX_CHARS}-character limit by {total - MAX_CHARS}"
        )
    return haiku


def main():
    validate(HAIKU)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(HAIKU + "\n")


if __name__ == "__main__":
    main()
