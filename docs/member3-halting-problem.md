# Member 3 — Halting Problem Demonstration

## 1. The proof structure (diagonalization/contradiction)

The Halting Problem asks: does there exist an algorithm `halts(program, input)` that
always correctly decides whether `program` halts on `input`? The answer is no, proved
by a diagonalization argument — the same style of proof used by Cantor and Godel.

**Proof sketch:**
1. Assume `halts(P, x)` exists and is always correct.
2. Construct `paradox(x)` that deliberately does the opposite of what `halts`
   predicts about it.
3. Either prediction `halts` could make turns out wrong by construction.
4. Since the assumption leads to a contradiction either way, no such `halts` can exist.

## 2. The paradox, in code

See `src/halting_demo.py`. This code does not execute an undecidable computation —
that's not something you can actually do. It makes the logical structure of the
proof concrete: it shows exactly what `paradox` is defined to do in each branch.

## 3. Showing the contradiction

- **Case 1:** `halts` predicts `paradox` will halt -> by its own definition it loops
  forever instead -> prediction wrong.
- **Case 2:** `halts` predicts `paradox` will not halt -> by its own definition it
  halts immediately instead -> prediction wrong.

Since `halts` is wrong in both possible cases, it cannot be the always-correct
decider assumed at the start.

## 4. Testing the simulator

### 4a. A machine that never halts

`tables/looping_table.py` defines a one-state TM with no path to accept or reject —
it runs forever on every input. Running it through the engine confirms the engine
cannot know this in advance; it only notices via the `max_steps` cutoff:

```
tm.run("101", max_steps=1000) -> ("TIMEOUT", ..., 1000)
```

### 4b. Extra edge-case tests

A few tricky cases were added for the other two machines: malformed addition input
with no `+`, `0 + 0`, two different single characters, two identical single
characters, and a longer even-length palindrome. All pass — see
`tests/test_halting_demo.py` and `tests/test_edge_cases.py`.

## 5. Why this connects to Member 4's report

If no algorithm can always decide something as basic as "does this program halt,"
no algorithm can be guaranteed to perfectly verify every possible output of a much
more complex system like a language model either. That bridge is developed in
`docs/llm-safety-report.md`.
