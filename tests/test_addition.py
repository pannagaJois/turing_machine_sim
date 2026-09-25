import sys
sys.path.insert(0, "../src")
sys.path.insert(0, "../tables")
sys.path.insert(0, "src")
sys.path.insert(0, "tables")

from tm_simulator import TuringMachine
from addition_table import build_addition_tm


def run(s):
    t, start, acc, rej = build_addition_tm()
    return TuringMachine(t, start, acc, rej).run(s)


def test_three_plus_two():
    result, tape, _ = run("111+11")
    assert result == "ACCEPT"
    assert tape == "11111"


def test_zero_plus_two():
    result, tape, _ = run("+11")
    assert result == "ACCEPT"
    assert tape == "11"


def test_two_plus_zero():
    result, tape, _ = run("11+")
    assert result == "ACCEPT"
    assert tape == "11"


if __name__ == "__main__":
    test_three_plus_two()
    test_zero_plus_two()
    test_two_plus_zero()
    print("all addition tests passed")
