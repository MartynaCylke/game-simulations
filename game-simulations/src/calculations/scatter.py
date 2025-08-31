# src/calculations/scatter.py
import random
from typing import List, Tuple, Dict, Any

def count_scatters(board: List[List[str]], scatter_symbol: str):
    positions = []
    for reel_idx, reel in enumerate(board):
        for row_idx, s in enumerate(reel):
            if s == scatter_symbol:
                positions.append((reel_idx, row_idx))
    return len(positions), positions

class ScatterGame:
    def __init__(self, config):
        self.config = config

    def draw_board(self):
        pool = self.config.symbol_pool
        board = []
        for _ in range(self.config.num_reels):
            col = [random.choice(pool) for _ in range(self.config.num_rows)]
            board.append(col)
        return board

    def play_once(self, sim_index:int):
        board = self.draw_board()
        scatters, positions = count_scatters(board, self.config.scatter)
        fs_awarded = self.config.freespin_triggers.get(scatters, 0) if scatters >= 3 else 0
        # also evaluate lines for wins
        from src.calculations.lines import evaluate_lines_helper
        lines = evaluate_lines_helper(board, self.config)
        return {"board": board, "lines": lines, "scatters": scatters, "fs_awarded": fs_awarded, "scatter_positions": positions}
