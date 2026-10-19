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


def test_all_sums_up_to_7():
    for m in range(8):
        for n in range(8):
            result, tape, _ = run("1" * m + "+" + "1" * n)
            assert result == "ACCEPT" and tape == "1" * (m + n), (m, n)


def test_sample_takes_8_steps():
    result, tape, steps = run("111+11")
    assert (result, tape, steps) == ("ACCEPT", "11111", 8)


if __name__ == "__main__":
    test_three_plus_two()
    test_zero_plus_two()
    test_two_plus_zero()
    test_all_sums_up_to_7()
    test_sample_takes_8_steps()
    print("all addition tests passed")
