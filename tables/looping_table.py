BLANK = "_"

START = "loop"
ACCEPT = "accept"
REJECT = "reject"


def build_looping_tm():
    """
    A TM that never halts on any input: it just keeps moving right
    forever, never reaching accept or reject. Used to demonstrate
    that the simulator cannot know in advance whether a machine
    halts, and must rely on a step cutoff.
    """
    transitions = {
        ("loop", "0"): ("loop", "0", "R"),
        ("loop", "1"): ("loop", "1", "R"),
        ("loop", BLANK): ("loop", BLANK, "R"),
    }
    return transitions, START, {ACCEPT}, {REJECT}
