# Hand Traces

## TM 1 — Addition: 111+11

| Step | State | Tape | Head |
|---|---|---|---|
| 0 | q0 | 111+11 | 0 |
| 1 | q0 | 111+11 | 1 |
| 2 | q0 | 111+11 | 2 |
| 3 | q0 | 111+11 | 3 |
| 4 | q1 | 111111 | 4 |
| 5 | q1 | 111111 | 5 |
| 6 | q2 | 111111_ | 5 |
| 7 | qaccept | 11111 | 6 |

Result: `11111` = 5 in unary = 3 + 2. Correct.

## TM 2 — Palindrome: abcba

Marks the outer pair (a...a), then (b...b), then reaches the middle
`c`, which matches itself. All pairs matched -> ACCEPT.

## TM 2 — Palindrome: abcda

Marks the outer pair (a...a), then compares `b` against `d` on the
next pass -> mismatch -> REJECT.
