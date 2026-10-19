# Turing Machine Simulator

A generic Turing Machine simulator built from a formal transition table, with two
example machines (unary addition, palindrome checking) and a demonstration of the
Halting Problem connected to AI safety.

## What's inside

- **A generic TM engine** (`src/tm_simulator.py`, `src/tape.py`) that runs *any*
  machine defined as a transition table — nothing addition- or palindrome-specific
  is hardcoded into it.
- **Two working machines**: unary addition (`111+11 -> 11111`) and a palindrome
  checker, both defined in `tables/`.
- **A Halting Problem demonstration** (`src/halting_demo.py`): the classic
  diagonalization/contradiction proof, plus a genuinely non-halting machine
  (`tables/looping_table.py`) run through the simulator to show its timeout
  safeguard in action.
- **A CLI** with colored step animation and matplotlib tape-history plots.
- **Formal design docs, hand traces, and scanned handwritten work** in `docs/`.

## Requirements

- Python 3.8+
- `matplotlib`, only if you want to use `--plot` (not needed for anything else)

```
pip install matplotlib
```

## Running it

All commands are run from the `src/` folder:

```
cd src

python3 main.py                                  # full fixed demo (both machines + halting proof)
python3 main.py addition 111+11                  # run the addition TM on a specific input
python3 main.py palindrome abcba                  # run the palindrome TM on a specific input
python3 main.py palindrome abcba --animate         # colored, step-by-step terminal animation
python3 main.py addition 111+11 --trace            # print every step as text (state + tape)
python3 main.py addition 111+11 --plot out.png     # save a matplotlib tape-history plot
python3 main.py halting                            # just the halting-problem contradiction
```

`--plot`, `--trace` and `--animate` work with both machines. The addition machine
accepts any input string (malformed ones are rejected). The palindrome machine
accepts **lowercase letters a-z only** (digits, spaces and uppercase have no
distinct "matched" marker, so they are refused with an error).

## Running the tests

```
cd tests
python3 test_addition.py
python3 test_palindrome.py
python3 test_halting_demo.py
python3 test_edge_cases.py
```

Covers the two official sample inputs, edge cases (empty string, single character,
malformed input), exhaustive checks (all sums 0+0..7+7, all palindrome strings up
to length 7), the plot/history regression, and confirms the engine correctly times
out on a non-halting machine instead of hanging.

## Project structure

```
docs/           formal TM definition, machine designs, hand traces, LLM safety report,
                scanned handwritten design/tracing (docs/handwritten/)
tables/         transition tables: addition, palindrome, and a looping (non-halting) TM
src/            tape, engine, CLI, halting demo, matplotlib visualization
tests/          correctness tests for all machines, including edge cases
slides/         presentation slides and outline
sample_output/  example matplotlib plots
```

## Team

| Member | Contribution |
|---|---|
| 1 | TM formal design (both machines), hand traces |
| 2 | Python simulator engine, tape display, CLI |
| 3 | Halting problem demonstration, simulator testing |
| 4 | LLM safety report, slides |

See `docs/member1-tm-design.md` through `docs/member4-llm-safety.md` for each
member's detailed writeup.
