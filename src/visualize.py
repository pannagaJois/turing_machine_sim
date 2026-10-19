import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BLANK = "_"


def plot_history(history, title, out_path):
    """
    history: list of (cells, head_position, state) snapshots, where cells is a
    dict {position: symbol} (as recorded by TuringMachine.run).
    Draws a grid: rows = steps, columns = tape positions, head cell highlighted.
    The column range covers every cell written AND every head position, so the
    head is always visible (even when it sits on a blank beyond the tape).
    """
    positions = []
    for cells, head, _ in history:
        positions.extend(cells.keys())
        positions.append(head)
    lo, hi = min(positions), max(positions)
    width = hi - lo + 1
    height = len(history)

    fig, ax = plt.subplots(figsize=(max(4, width * 0.6), max(2, height * 0.4)))

    for row, (cells, head, state) in enumerate(history):
        y = height - row - 1
        for col in range(width):
            pos = lo + col
            symbol = cells.get(pos, BLANK)
            color = "#ffd54f" if pos == head else "#eeeeee"
            ax.add_patch(plt.Rectangle((col, y), 1, 1, facecolor=color,
                                        edgecolor="#999999"))
            ax.text(col + 0.5, y + 0.5, symbol, ha="center", va="center",
                    fontsize=10)
        ax.text(width + 0.3, y + 0.5, state, ha="left", va="center",
                fontsize=8, color="#555555")

    ax.set_xlim(0, width + 2.5)
    ax.set_ylim(0, height)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)
    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    return out_path
