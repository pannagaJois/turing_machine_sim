import sys
sys.path.insert(0, "../src")
sys.path.insert(0, "../tables")
sys.path.insert(0, "src")
sys.path.insert(0, "tables")

from tm_simulator import TuringMachine
from looping_table import build_looping_tm


def test_looping_machine_times_out():
    t, start, acc, rej = build_looping_tm()
    tm = TuringMachine(t, start, acc, rej)
    result, tape, steps = tm.run("101", max_steps=1000)
    assert result == "TIMEOUT"
    assert steps == 1000


def test_looping_machine_on_empty_input():
    t, start, acc, rej = build_looping_tm()
    tm = TuringMachine(t, start, acc, rej)
    result, tape, steps = tm.run("", max_steps=500)
    assert result == "TIMEOUT"


if __name__ == "__main__":
    test_looping_machine_times_out()
    test_looping_machine_on_empty_input()
    print("all halting-demo tests passed")
