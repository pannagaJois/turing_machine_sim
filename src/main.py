import sys
sys.path.insert(0, "../tables")
sys.path.insert(0, "tables")

from tm_simulator import TuringMachine
from addition_table import build_addition_tm
from palindrome_table import build_palindrome_tm
from halting_demo import show_contradiction


def run_addition(input_string, verbose=False):
    transitions, start, accept, reject = build_addition_tm()
    tm = TuringMachine(transitions, start, accept, reject)
    return tm.run(input_string, verbose=verbose)


def run_palindrome(input_string, alphabet=None, verbose=False):
    if alphabet is None:
        alphabet = sorted(set(input_string))
    transitions, start, accept, reject = build_palindrome_tm(alphabet)
    tm = TuringMachine(transitions, start, accept, reject)
    return tm.run(input_string, verbose=verbose)


def demo():
    print("TM 1 (Addition): 111+11")
    result, tape, steps = run_addition("111+11", verbose=True)
    print(f"Result: {tape} ({result}, {steps} steps)\n")

    for word in ["abcba", "abcda"]:
        print(f"TM 2 (Palindrome): {word}")
        result, tape, steps = run_palindrome(word)
        print(f"-> {result}\n")

    print("--- Halting Problem ---")
    show_contradiction()


if __name__ == "__main__":
    demo()
