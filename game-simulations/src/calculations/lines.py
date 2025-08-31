# src/calculations/lines.py
from typing import List, Dict, Any
import random

def evaluate_lines_helper(board: List[List[str]], config) -> Dict[str, Any]:
    """
    Simple evaluation: count matching symbols on each payline.
    Returns dict with list of wins and total payout.
    """
    wins = []
    total = 0

    # Iterate over list of paylines
    for line_idx, line in enumerate(config.paylines):
        symbols = [board[col][row] for col, row in enumerate(line)]
        first_symbol = symbols[0]
        count = 1
        for sym in symbols[1:]:
            if sym == first_symbol:
                count += 1
            else:
                break
        if count >= config.min_line_length:
            payout = config.symbol_values.get(first_symbol, 0) * count
            total += payout
            wins.append({"line": line_idx, "symbol": first_symbol, "count": count, "payout": payout})

    return {"wins": wins, "total": total}

class LinesGame:
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
        lines_result = evaluate_lines_helper(board, self.config)
        return {"board": board, "lines": lines_result["wins"], "total": lines_result["total"]}
