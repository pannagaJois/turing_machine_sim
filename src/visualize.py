import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def plot_history(history, title, out_path):
    """
    history: list of (tape_string, head_position, state) snapshots.
    Draws a grid: rows = steps, columns = tape cells, head cell highlighted.
    """
    tapes = [h[0] for h in history]
    width = max(len(t) for t in tapes) if tapes else 1
    height = len(history)

    fig, ax = plt.subplots(figsize=(max(4, width * 0.6), max(2, height * 0.4)))

    for row, (tape_str, head, state) in enumerate(history):
        y = height - row - 1
        for col in range(width):
            symbol = tape_str[col] if col < len(tape_str) else "_"
            is_head = (col == head)
            color = "#ffd54f" if is_head else "#eeeeee"
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
