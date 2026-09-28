import sys
sys.path.insert(0, "../src")
sys.path.insert(0, "../tables")
sys.path.insert(0, "src")
sys.path.insert(0, "tables")

from tm_simulator import TuringMachine
from addition_table import build_addition_tm
from palindrome_table import build_palindrome_tm


def run_addition(s):
    t, start, acc, rej = build_addition_tm()
    return TuringMachine(t, start, acc, rej).run(s)


def run_palindrome(s, alphabet=("a", "b", "c", "d")):
    t, start, acc, rej = build_palindrome_tm(list(alphabet))
    return TuringMachine(t, start, acc, rej).run(s)


def test_addition_malformed_no_plus():
    result, _, _ = run_addition("111")
    assert result == "REJECT"


def test_addition_zero_plus_zero():
    result, tape, _ = run_addition("+")
    assert result == "ACCEPT"
    assert tape == ""


def test_palindrome_two_different_chars():
    result, _, _ = run_palindrome("ab")
    assert result == "REJECT"


def test_palindrome_two_same_chars():
    result, _, _ = run_palindrome("aa")
    assert result == "ACCEPT"


def test_palindrome_long_even():
    result, _, _ = run_palindrome("abccba")
    assert result == "ACCEPT"


if __name__ == "__main__":
    test_addition_malformed_no_plus()
    test_addition_zero_plus_zero()
    test_palindrome_two_different_chars()
    test_palindrome_two_same_chars()
    test_palindrome_long_even()
    print("all edge-case tests passed")
