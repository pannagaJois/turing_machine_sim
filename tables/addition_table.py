BLANK = "_"

START = "q0"
ACCEPT = "qaccept"
REJECT = "qreject"


def build_addition_tm():
    transitions = {
        ("q0", "1"): ("q0", "1", "R"),
        ("q0", "+"): ("q1", "1", "R"),
        ("q1", "1"): ("q1", "1", "R"),
        ("q1", BLANK): ("q2", BLANK, "L"),
        ("q2", "1"): (ACCEPT, BLANK, "R"),
    }
    return transitions, START, {ACCEPT}, {REJECT}
