# Formal Definition of a Turing Machine

A Turing Machine is a 7-tuple:

**M = (Q, Σ, Γ, δ, q0, qaccept, qreject)**

- **Q** — finite set of states
- **Σ** — input alphabet (does not include the blank symbol)
- **Γ** — tape alphabet, Σ ⊆ Γ, and blank `_` ∈ Γ
- **δ** — transition function: δ: Q × Γ → Q × Γ × {L, R}
- **q0** — start state, q0 ∈ Q
- **qaccept** — accept state
- **qreject** — reject state, qreject ≠ qaccept

## How it runs

1. The tape starts with the input string, blanks everywhere else.
2. The head starts at position 0 in state q0.
3. At each step, read the symbol under the head, look up δ(state, symbol),
   write the new symbol, move the head left or right, and switch state.
4. The machine halts when it enters qaccept or qreject, or if δ is
   undefined for the current (state, symbol) pair.

## This project's two machines

| Machine | Σ | Purpose |
|---|---|---|
| TM 1 | {1, +} | unary addition, e.g. `111+11 -> 11111` |
| TM 2 | {a, b, c, d} | palindrome checking |

See `addition_table.py` and `palindrome_table.py` for the concrete
transition functions, and `docs/traces.md` for hand traces.
