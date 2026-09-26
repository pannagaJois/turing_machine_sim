# Member 2 — Python Simulator + Tape Display

## 1. The generic TM engine

The engine is split into two independent pieces: a `Tape` that only knows how to
store and move, and a `TuringMachine` that only knows how to follow a transition
table. Neither piece knows anything about addition or palindromes — all
machine-specific behavior lives entirely in the tables handed over by Member 1.

The tape is a Python `dict` mapping position to symbol, not a fixed array. This
gives an unbounded tape in both directions for free — no "index out of range"
handling needed, and blank cells simply don't exist until something is written.

Any `(state, symbol)` pair with no table entry is treated as an automatic reject,
matching the formal definition (δ is a partial function). A `max_steps` cutoff
guards against infinite loops — the engine cannot know in advance whether a given
machine halts, so a machine that hits the cutoff is reported as `TIMEOUT`.

## 2. Implementing both machines from Member 1's tables

Member 1's tables translate directly into dict literals in `addition_table.py`
and `palindrome_table.py`. Both were checked against Member 1's hand traces
before being trusted.

## 3. Terminal tape display

`Tape.render()` prints the tape with the head position marked underneath each
step, when running with `verbose=True`.

## 4. Sample outputs

```
TM 1 (Addition): 111+11
Result: 11111 (ACCEPT, 8 steps)

TM 2 (Palindrome): abcba
-> ACCEPT

TM 2 (Palindrome): abcda
-> REJECT
```

Matches both the project spec and Member 1's hand traces exactly.

## 5. Tests

`tests/test_addition.py` and `tests/test_palindrome.py` cover the sample cases
and basic edge cases. All pass.
