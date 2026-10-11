import sys
import argparse

sys.path.insert(0, "../tables")
sys.path.insert(0, "tables")

from tm_simulator import TuringMachine
from addition_table import build_addition_tm
from palindrome_table import build_palindrome_tm
from halting_demo import show_contradiction


def build_machine(kind, alphabet):
    if kind == "addition":
        return build_addition_tm()
    if kind == "palindrome":
        return build_palindrome_tm(alphabet)
    raise ValueError(f"unknown machine: {kind}")


def run_machine(kind, input_string, alphabet, animate, delay):
    transitions, start, accept, reject = build_machine(kind, alphabet)
    tm = TuringMachine(transitions, start, accept, reject)
    result, tape, steps = tm.run(input_string, animate=animate, delay=delay)
    if not animate:
        print(f"{kind} on '{input_string}' -> {result} (tape: '{tape}', {steps} steps)")


def demo():
    print("TM 1 (Addition): 111+11")
    run_machine("addition", "111+11", None, animate=False, delay=0.4)

    for word in ["abcba", "abcda"]:
        print(f"TM 2 (Palindrome): {word}")
        run_machine("palindrome", word, list(word), animate=False, delay=0.4)

    print("--- Halting Problem ---")
    show_contradiction()


def main():
    parser = argparse.ArgumentParser(description="Turing Machine Simulator CLI")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("demo", help="run the full fixed demo (default)")

    add_p = sub.add_parser("addition", help="run the unary addition TM")
    add_p.add_argument("input", help="e.g. 111+11")
    add_p.add_argument("--animate", action="store_true", help="colored step animation")
    add_p.add_argument("--delay", type=float, default=0.4)

    pal_p = sub.add_parser("palindrome", help="run the palindrome checker TM")
    pal_p.add_argument("input", help="e.g. abcba")
    pal_p.add_argument("--animate", action="store_true")
    pal_p.add_argument("--delay", type=float, default=0.4)

    args = parser.parse_args()

    if args.command is None or args.command == "demo":
        demo()
    elif args.command == "addition":
        run_machine("addition", args.input, None, args.animate, args.delay)
    elif args.command == "palindrome":
        run_machine("palindrome", args.input, list(args.input), args.animate, args.delay)


if __name__ == "__main__":
    main()
