def halts(program, program_input):
    """
    Hypothetical perfect halting decider.
    Assume this always correctly returns True/False.
    """
    if program == "paradox":
        return not halts("paradox", program_input)
    return True


def paradox(x):
    """
    A program that does the opposite of whatever halts()
    predicts about it.
    """
    if halts("paradox", x):
        while True:
            pass
    else:
        return


def show_contradiction():
    print("Assume halts(program, input) always gives a correct answer.")
    print()
    print("Define paradox(x):")
    print("    if halts('paradox', x): loop forever")
    print("    else: return immediately")
    print()
    print("Case 1: halts('paradox', x) == True")
    print("  -> paradox(x) loops forever -> it does NOT halt -> contradiction")
    print()
    print("Case 2: halts('paradox', x) == False")
    print("  -> paradox(x) returns immediately -> it DOES halt -> contradiction")
    print()
    print("Both cases contradict the assumption, so no such halts() can exist.")
    print("=> The Halting Problem is undecidable.")


if __name__ == "__main__":
    show_contradiction()
