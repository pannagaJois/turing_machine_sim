# Slides — Turing Machine Simulator

## Slide 1 — Title
**Turing Machine Simulator**
Project 15 | Formal Model of Computation

## Slide 2 — What is a Turing Machine
A 7-tuple M = (Q, Σ, Γ, δ, q0, q_accept, q_reject). Infinite tape + a head that
reads, writes, and moves, guided by a transition table.

## Slide 3 — TM 1: Unary Addition
Design: turn `+` into `1`, then erase the trailing `1` to correct the count.

```
Input:  111+11
Output: 11111   (3 + 2 = 5)
Result: ACCEPT, 8 steps
```

## Slide 4 — TM 2: Palindrome Checker
Design: mark the outer pair, compare, repeat inward.

```
abcba -> ACCEPT
abcda -> REJECT
```

## Slide 5 — The Halting Problem
No algorithm `halts(program, input)` can always correctly decide whether an
arbitrary program halts.

```
halts predicts "halts"  -> paradox loops forever -> wrong
halts predicts "loops"  -> paradox halts at once  -> wrong
```

## Slide 6 — From Undecidability to LLM Safety
Rice's Theorem generalizes the Halting Problem: no algorithm can decide any
non-trivial property of an arbitrary program. No single checker can guarantee an
LLM's output in every case; safety relies on layered, bounded defenses.

## Slide 7 — Conclusion
Built a generic TM simulator, two working machines, and a concrete demonstration
of undecidability, connecting 1930s computability theory to a current AI safety
argument.
