from tape import Tape, BLANK


class TuringMachine:
    def __init__(self, transitions, start_state, accept_states, reject_states):
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        self.reject_states = reject_states

    def run(self, input_string, max_steps=100000, verbose=False):
        tape = Tape(input_string)
        state = self.start_state
        steps = 0

        while state not in self.accept_states and state not in self.reject_states:
            if steps >= max_steps:
                return "TIMEOUT", tape.to_string(), steps

            symbol = tape.read()
            key = (state, symbol)
            if key not in self.transitions:
                return "REJECT", tape.to_string(), steps

            new_state, write_symbol, direction = self.transitions[key]

            if verbose:
                print(tape.render())
                print(f"state={state} read='{symbol}' -> state={new_state} "
                      f"write='{write_symbol}' move={direction}\n")

            tape.write(write_symbol)
            tape.move(direction)
            state = new_state
            steps += 1

        result = "ACCEPT" if state in self.accept_states else "REJECT"
        return result, tape.to_string(), steps
