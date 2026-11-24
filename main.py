"""Write the one-sentence absurd invention pitch to /output/entry.txt.

The pitch is a single sentence (exactly one period, at the end) of at
most 220 characters. Guards below enforce the bounty constraints at
import time so a bad pitch fails loudly instead of producing a
rejected entry file.
"""

import os

PITCH = (
    'A fridge that dims its light politely at midnight, whispers '
    '"we both know you\'re not hungry, you\'re bored," and locks '
    "the cheese drawer until morning."
)

MAX_LEN = 220  # bounty gate: /output/entry.txt must be 1-220 characters

assert 1 <= len(PITCH) <= MAX_LEN, f"pitch is {len(PITCH)} chars, outside 1-{MAX_LEN}"
assert PITCH == PITCH.strip(), "pitch must not have leading/trailing whitespace"
assert PITCH.count(".") == 1 and PITCH.endswith("."), "pitch must be exactly one sentence"
assert "\n" not in PITCH, "pitch must be a single line with no newline in the middle"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(PITCH)
print(PITCH)
print(f"({len(PITCH)} characters)")
