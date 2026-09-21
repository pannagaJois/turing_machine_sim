# Member 1 — TM Formal Design

## 1. Formal Definition

See `docs/tm-formal-definition.md` for the full 7-tuple definition.

## 2. TM 1 — Unary Addition

**Goal:** compute `m + n` where m, n are written in unary (m ones, then `+`, then n ones).

**Idea:** `+` sits between the two unary blocks. Turning `+` into a `1` merges both
blocks into one block of `m + n + 1` ones (one too many). Erasing exactly one `1` from
the end of that merged block fixes the count to `m + n`.

**Formal machine:**
- Σ = {1, +}
- Γ = {1, +, _}
- Q = {q0, q1, q2, q_accept, q_reject}
- q0 = start

**State diagram (plain description):**
- **q0** — scanning the first number. On `1`, stay in q0, move right. On `+`, write `1`
  (merging the numbers), move right, go to q1.
- **q1** — scanning the second number. On `1`, stay in q1, move right. On blank, the end
  of the tape has been reached — move left, go to q2.
- **q2** — positioned on the last `1` of the merged block. Erase it (write blank), move
  right, go to q_accept.

**Transition table:**

| State | Read | Write | Move | Next State |
|---|---|---|---|---|
| q0 | 1 | 1 | R | q0 |
| q0 | + | 1 | R | q1 |
| q1 | 1 | 1 | R | q1 |
| q1 | _ | _ | L | q2 |
| q2 | 1 | _ | R | q_accept |

Any (state, symbol) pair not listed above is an automatic reject.

## 3. TM 2 — Palindrome Checker

**Goal:** accept the input if and only if it reads the same forwards and backwards.

**Idea:** repeatedly take the leftmost not-yet-checked symbol, remember it, sweep to
the rightmost not-yet-checked symbol, and compare. If they match, mark both as checked
(by writing an uppercase version) and repeat from the left. If they don't match, reject.
If the sweep finds nothing left to check, accept.

**Formal machine (generalizes to any alphabet of single-character symbols):**
- Σ = {a, b, c, d} for this project
- Γ = {a, b, c, d, A, B, C, D, _} — uppercase = "already matched" marker
- Q = {find_left, seekend_a..d, checkend_a..d, goback, accept, reject}
- q0 = find_left

**State diagram (plain description), for a generic symbol `c` with marker `C`:**
- **find_left** — scanning from the left for the next not-yet-marked symbol.
  Skip marked symbols. On blank, nothing left to check, accept. On unmarked `c`,
  mark it, move right, go to **seekend_c**.
- **seekend_c** — sweep right to the current right boundary (first marked symbol
  or blank), then step back onto the last unmarked symbol, go to **checkend_c**.
- **checkend_c** — compare that symbol to `c`. Match: mark it, go to **goback**.
  Same marker already (middle reached): accept. Different symbol: reject.
- **goback** — sweep left back to the start, then restart at **find_left**.

**Transition table (worked out for alphabet {a, b, c, d}):**

| State | Read | Write | Move | Next State |
|---|---|---|---|---|
| find_left | a/b/c/d | A/B/C/D | R | seekend_a/b/c/d |
| find_left | A/B/C/D | A/B/C/D | R | find_left |
| find_left | _ | _ | R | accept |
| seekend_c | lowercase | unchanged | R | seekend_c |
| seekend_c | uppercase | unchanged | L | checkend_c |
| seekend_c | _ | _ | L | checkend_c |
| checkend_c | c | C | L | goback |
| checkend_c | C | C | R | accept |
| checkend_c | other lowercase | unchanged | R | reject |
| checkend_c | other uppercase | unchanged | R | accept |
| goback | any symbol | unchanged | L | goback |
| goback | _ | _ | R | find_left |

This generic table is what `tables/palindrome_table.py` generates in code.
