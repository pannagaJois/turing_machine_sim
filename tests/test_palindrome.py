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


def test_exhaustive_up_to_length_7():
    import itertools
    for n in range(8):
        for w in itertools.product(ALPHABET, repeat=n):
            w = "".join(w)
            expected = "ACCEPT" if w == w[::-1] else "REJECT"
            assert run(w)[0] == expected, w


def test_rejects_non_lowercase_alphabet():
    # digits / uppercase / spaces have no distinct "marked" symbol, so the
    # builder must refuse them instead of giving wrong answers (e.g. "123")
    for bad in ["123", "Aa", "a b", "a_a"]:
        try:
            build_palindrome_tm(list(bad))
        except ValueError:
            continue
        raise AssertionError(f"alphabet {bad!r} should have been rejected")


if __name__ == "__main__":
    test_odd_palindrome()
    test_even_palindrome()
    test_not_palindrome()
    test_single_char()
    test_empty()
    test_exhaustive_up_to_length_7()
    test_rejects_non_lowercase_alphabet()
    print("all palindrome tests passed")
