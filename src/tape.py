BLANK = "_"


class Tape:
    def __init__(self, input_string):
        self.cells = {i: c for i, c in enumerate(input_string)}
        self.head = 0

    def read(self):
        return self.cells.get(self.head, BLANK)

    def write(self, symbol):
        if symbol == BLANK:
            self.cells.pop(self.head, None)
        else:
            self.cells[self.head] = symbol

    def move(self, direction):
        if direction == "R":
            self.head += 1
        elif direction == "L":
            self.head -= 1

    def to_string(self):
        if not self.cells:
            return ""
        lo, hi = min(self.cells), max(self.cells)
        return "".join(self.cells.get(i, BLANK) for i in range(lo, hi + 1))

    def render(self):
        if not self.cells:
            lo, hi = 0, 0
        else:
            lo, hi = min(self.cells), max(self.cells)
        lo = min(lo, self.head)
        hi = max(hi, self.head)
        top = " ".join(self.cells.get(i, BLANK) for i in range(lo, hi + 1))
        marker = "   ".join("^" if i == self.head else " " for i in range(lo, hi + 1))
        return f"{top}\n{marker}"

    def render_color(self):
        YELLOW = "\033[93m"
        RESET = "\033[0m"
        if not self.cells:
            lo, hi = 0, 0
        else:
            lo, hi = min(self.cells), max(self.cells)
        lo = min(lo, self.head)
        hi = max(hi, self.head)
        cells = []
        for i in range(lo, hi + 1):
            symbol = self.cells.get(i, BLANK)
            if i == self.head:
                cells.append(f"{YELLOW}[{symbol}]{RESET}")
            else:
                cells.append(f" {symbol} ")
        return "".join(cells)
