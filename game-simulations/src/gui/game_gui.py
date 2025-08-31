import tkinter as tk
from tkinter import ttk
from random import choice
from src.calculations.lines import LinesGame
from src.calculations.ways import WaysGame
from src.calculations.cluster import ClusterGame
from src.calculations.scatter import ScatterGame
from src.config.config import GameConfig

# Map game name to class
GAME_CLASSES = {
    "lines": LinesGame,
    "ways": WaysGame,
    "cluster": ClusterGame,
    "scatter": ScatterGame,
}

# Color palette for highlighting
HIGHLIGHT_COLORS = ["yellow", "lightgreen", "lightblue", "orange", "pink"]

class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Slot Game Visualizer")

        self.game_var = tk.StringVar(value="lines")
        self.dropdown = ttk.Combobox(master, textvariable=self.game_var, values=list(GAME_CLASSES.keys()))
        self.dropdown.grid(row=0, column=0, padx=10, pady=10)

        self.spin_button = tk.Button(master, text="Spin", command=self.next_spin)
        self.spin_button.grid(row=0, column=1, padx=10, pady=10)

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.game_instance = None
        self.cell_size = 60
        self.board_rows = 5
        self.board_cols = 5

        self.next_spin()

    def init_game_instance(self):
        game_name = self.game_var.get()
        GameClass = GAME_CLASSES[game_name]
        config = GameConfig(game_name)
        self.game_instance = GameClass(config)

    def draw_board(self, board, highlight_positions=None):
        self.canvas.delete("all")
        highlight_positions = highlight_positions or {}

        for c, col in enumerate(board):
            for r, symbol in enumerate(col):
                x0 = c * self.cell_size
                y0 = r * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size

                # Choose color based on highlight_positions dict
                fill_color = highlight_positions.get((c, r), "white")
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill_color, outline="black")
                self.canvas.create_text(x0 + self.cell_size/2, y0 + self.cell_size/2,
                                        text=symbol, font=("Arial", 16, "bold"))

    def next_spin(self):
        self.init_game_instance()
        result = self.game_instance.play_once(sim_index=0)
        board = result.get("board", [])
        highlight_positions = {}

        game_name = self.game_var.get()
        if game_name == "cluster" and "clusters" in result:
            for idx, cluster in enumerate(result["clusters"]):
                color = HIGHLIGHT_COLORS[idx % len(HIGHLIGHT_COLORS)]
                for pos in cluster["positions"]:
                    highlight_positions[pos] = color
        elif game_name == "scatter" and "scatters" in result:
            color = choice(HIGHLIGHT_COLORS)
            for pos in result["scatters"]:
                highlight_positions[pos] = color
        elif game_name == "lines" and "wins" in result:
            for idx, win in enumerate(result["wins"]):
                color = HIGHLIGHT_COLORS[idx % len(HIGHLIGHT_COLORS)]
                for c in range(len(board)):
                    highlight_positions[(c, win["line"])] = color
        elif game_name == "ways" and "wins" in result:
            for idx, win in enumerate(result["wins"]):
                color = HIGHLIGHT_COLORS[idx % len(HIGHLIGHT_COLORS)]
                for pos in win.get("positions", []):
                    highlight_positions[pos] = color

        self.draw_board(board, highlight_positions)

if __name__ == "__main__":
    root = tk.Tk()
    gui = GameGUI(root)
    root.mainloop()
