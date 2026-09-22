BLANK = "_"

START = "find_left"
ACCEPT = "accept"
REJECT = "reject"


def build_palindrome_tm(alphabet):
    marker = {c: c.upper() for c in alphabet}
    transitions = {}

    for c in alphabet:
        C = marker[c]

        transitions[(START, c)] = (f"seekend_{c}", C, "R")
        transitions[(START, C)] = (START, C, "R")

        for d in alphabet:
            transitions[(f"seekend_{c}", d)] = (f"seekend_{c}", d, "R")
        for d in alphabet:
            D = marker[d]
            transitions[(f"seekend_{c}", D)] = (f"checkend_{c}", D, "L")
        transitions[(f"seekend_{c}", BLANK)] = (f"checkend_{c}", BLANK, "L")

        transitions[(f"checkend_{c}", c)] = ("goback", C, "L")
        transitions[(f"checkend_{c}", C)] = (ACCEPT, C, "R")
        transitions[(f"checkend_{c}", BLANK)] = (ACCEPT, BLANK, "R")
        for d in alphabet:
            if d != c:
                transitions[(f"checkend_{c}", d)] = (REJECT, d, "R")
                transitions[(f"checkend_{c}", marker[d])] = (ACCEPT, marker[d], "R")

        transitions[("goback", c)] = ("goback", c, "L")
        transitions[("goback", C)] = ("goback", C, "L")

    transitions[(START, BLANK)] = (ACCEPT, BLANK, "R")
    transitions[("goback", BLANK)] = (START, BLANK, "R")

    return transitions, START, {ACCEPT}, {REJECT}
