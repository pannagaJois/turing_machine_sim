import sys
sys.path.insert(0, "../src")
sys.path.insert(0, "../tables")
sys.path.insert(0, "src")
sys.path.insert(0, "tables")

from tm_simulator import TuringMachine
from palindrome_table import build_palindrome_tm

ALPHABET = ["a", "b", "c", "d"]


def run(s):
    t, start, acc, rej = build_palindrome_tm(ALPHABET)
    return TuringMachine(t, start, acc, rej).run(s)


def test_odd_palindrome():
    assert run("abcba")[0] == "ACCEPT"


def test_even_palindrome():
    assert run("abba")[0] == "ACCEPT"


def test_not_palindrome():
    assert run("abcda")[0] == "REJECT"


def test_single_char():
    assert run("a")[0] == "ACCEPT"


def test_empty():
    assert run("")[0] == "ACCEPT"


if __name__ == "__main__":
    test_odd_palindrome()
    test_even_palindrome()
    test_not_palindrome()
    test_single_char()
    test_empty()
    print("all palindrome tests passed")
