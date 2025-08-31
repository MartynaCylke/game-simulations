# src/calculations/lines.py
import random
from typing import List, Dict, Any

class LinesGame:
    def __init__(self, config):
        self.config = config

    def draw_board(self):
        # board: list of reels (columns), each [top..bottom]
        board = []
        pool = self.config.symbol_pool
        for _ in range(self.config.num_reels):
            col = [random.choice(pool) for _ in range(self.config.num_rows)]
            board.append(col)
        return board

    def evaluate_lines(self, board: List[List[str]]):
        from src.calculations.lines import evaluate_lines_helper
        return evaluate_lines_helper(board, self.config)

    def play_once(self, sim_index: int):
        board = self.draw_board()
        # events: reveal
        lines_result = evaluate_lines_helper(board, self.config)
        # check scatters handled outside by caller or here
        return {"board": board, "lines": lines_result}

def evaluate_lines_helper(board: List[List[str]], config) -> Dict[str, Any]:
    wins = []
    total = 0
    for line_idx, line in config.paylines.items():
        # get symbol at first reel on that line
        first = board[0][line[0]]
        if first is None:
            continue
        # treat wild as matching any symbol, but prefer real symbols in first non-wild
        # we'll compute consecutive match count
        count = 1
        positions = [{"reel":0,"row":line[0]}]
        for r in range(1, config.num_reels):
            sym = board[r][line[r]]
            if sym == first or sym == config.wild or first == config.wild:
                count += 1
                positions.append({"reel": r, "row": line[r]})
            else:
                break
        if count >= 3:
            # choose real symbol for payout: if first is wild, find next non-wild in positions
            pay_sym = first
            if pay_sym == config.wild:
                # find first non-wild in positions, if none -> skip
                for pos in positions:
                    s = board[pos["reel"]][pos["row"]]
                    if s != config.wild:
                        pay_sym = s
                        break
            payout = config.paytable.get(pay_sym, {}).get(count, 0)
            if payout > 0:
                wins.append({"symbol": pay_sym, "kind": count, "win": payout, "positions": positions})
                total += payout
    return {"totalWin": total, "wins": wins}
