import time
from tape import Tape, BLANK

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"
CLEAR = "\033c"


class TuringMachine:
    def __init__(self, transitions, start_state, accept_states, reject_states):
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        self.reject_states = reject_states

    def run(self, input_string, max_steps=100000, verbose=False,
            animate=False, delay=0.4, record_history=False):
        tape = Tape(input_string)
        state = self.start_state
        steps = 0
        history = [(dict(tape.cells), tape.head, state)] if record_history else None

        while state not in self.accept_states and state not in self.reject_states:
            if steps >= max_steps:
                return self._finish("TIMEOUT", tape, steps, history, animate)

            symbol = tape.read()
            key = (state, symbol)
            if key not in self.transitions:
                return self._finish("REJECT", tape, steps, history, animate)

            new_state, write_symbol, direction = self.transitions[key]

            if animate:
                print(CLEAR, end="")
                print(tape.render_color())
                print(f"{CYAN}state={state} read='{symbol}' -> state={new_state} "
                      f"write='{write_symbol}' move={direction}{RESET}")
                time.sleep(delay)
            elif verbose:
                print(tape.render())
                print(f"state={state} read='{symbol}' -> state={new_state} "
                      f"write='{write_symbol}' move={direction}\n")

            tape.write(write_symbol)
            tape.move(direction)
            state = new_state
            steps += 1

            if record_history:
                history.append((dict(tape.cells), tape.head, state))

        result = "ACCEPT" if state in self.accept_states else "REJECT"
        return self._finish(result, tape, steps, history, animate)

    def _finish(self, result, tape, steps, history, animate):
        if animate:
            # draw the final tape so the finished result is actually visible
            print(CLEAR, end="")
            print(tape.render_color())
            color = GREEN if result == "ACCEPT" else RED
            print(f"{color}{result}{RESET} after {steps} steps")
        if history is not None:
            return result, tape.to_string(), steps, history
        return result, tape.to_string(), steps
