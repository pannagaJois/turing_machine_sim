# Turing Machine Simulator

Project 15: a Turing Machine simulator with two example machines
(unary addition, palindrome checking) and a demonstration of the
Halting Problem linked to LLM safety.

## Run it

```
cd src
python3 main.py                              # full fixed demo
python3 main.py addition 111+11               # run a specific input
python3 main.py palindrome abcba --animate     # colored step-by-step animation
python3 main.py addition 111+11 --plot out.png  # save a matplotlib tape-history plot
python3 main.py halting                         # just the halting contradiction
```

Needs `matplotlib` for `--plot` (`pip install matplotlib --break-system-packages`).

## Team

| Member | Contribution |
|---|---|
| 1 | TM formal design, both machines |
| 2 | Python simulator, tape display |
| 3 | Halting problem demonstration |
| 4 | LLM safety report, slides |
