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
step, when running with `verbose=True`. The CLI also has `--trace`, which prints
a compact one-line-per-step trace (state + tape with the head in `[ ]`), and the
default demo shows this trace for the addition machine.

## 4. Sample outputs

```
TM 1 (Addition): 111+11
addition on '111+11' -> ACCEPT (tape: '11111', 8 steps)
  Result: 11111 (= 5 in unary)
  Step-by-step:
      0  q0           [1]11+11
      ...
      8  qaccept      11111_[_]

TM 2 (Palindrome): abcba
palindrome on 'abcba' -> ACCEPT (tape: 'ABCBA', 27 steps)

TM 2 (Palindrome): abcda
palindrome on 'abcda' -> REJECT (tape: 'ABcdA', 18 steps)
  Mismatch detected at positions 2 and 4: b vs d
```

The accept/reject results and the 8-step addition trace match Member 1's hand
traces. (The project brief's sample prints "positions 1 and 5: a vs d", but in
`abcda` positions 1 and 5 are both `a`; the real mismatch is `b` vs `d` at
positions 2 and 4, which is what the program reports.) The mismatch line is
computed by the CLI from the input string; the TM itself only answers
ACCEPT/REJECT.

## 5. CLI, color, and matplotlib (polish pass)

After the initial version, the display was upgraded as a team pass, since the
plain-text output was too minimal on its own:

- **Color** (added to the engine): `tape.render_color()` highlights the head cell
  in yellow using ANSI escape codes, and the final tape and result print
  green/red as the last animation frame. Only active in `--animate` mode; the
  original plain `render()` path is unchanged.
- **CLI** (added on top of the engine): `main.py` uses `argparse` with subcommands
  — `addition <input>`, `palindrome <input>`, `halting`, or no argument for the
  original fixed demo — each machine command with `--animate`, `--trace` and
  `--plot FILE.png` flags.
- **Matplotlib** (`visualize.py`): draws a grid (rows = steps, columns = tape
  positions, head cell highlighted) from a recorded run history, satisfying the
  "Matplotlib or terminal animation" tooling option with an actual static figure.
  History is a list of `(cells_dict, head, state)` snapshots; the plot's column
  range covers every written cell *and* every head position, so the head is
  drawn even when it sits on a blank past the tape's end. History is only
  recorded when `--plot` or `--trace` is used.

## 6. Tests

`tests/test_addition.py` and `tests/test_palindrome.py` cover the sample cases and
basic edge cases, plus exhaustive checks (every sum 0+0 to 7+7; every string over
{a,b,c,d} up to length 7 against a direct palindrome test). All pass.

Palindrome alphabets are restricted to lowercase letters a-z, because "already
matched" is marked with the uppercase form. Digits, spaces, uppercase letters or
`_` have no distinct marker and would give wrong answers (for example `123` used
to be wrongly accepted), so `build_palindrome_tm` raises `ValueError` and the
CLI reports a clean usage error.
