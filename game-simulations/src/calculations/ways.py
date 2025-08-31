# src/calculations/ways.py
import random
from typing import List, Dict, Any

class WaysGame:
    def __init__(self, config):
        self.config = config

    def draw_board(self):
        pool = self.config.symbol_pool
        board = []
        for _ in range(self.config.num_reels):
            col = [random.choice(pool) for _ in range(self.config.num_rows)]
            board.append(col)
        return board

    def evaluate_ways(self, board):
        # simplified: for each symbol that appears at least once in each reel, compute product of counts
        total_win = 0
        cols = len(board)
        from collections import Counter
        counts_per_reel = [Counter(reel) for reel in board]
        # check each base symbol
        for sym in self.config.symbols:
            ways = 1
            present_all = True
            for c in counts_per_reel:
                cnt = c.get(sym, 0)
                if cnt == 0:
                    present_all = False
                    break
                ways *= cnt
            if present_all:
                # payout take paytable for full-reel match (kind = num_reels)
                payout = self.config.paytable.get(sym, {}).get(len(board), 0)
                total_win += payout * ways
        return {"totalWin": total_win, "wins": []}

    def play_once(self, sim_index:int):
        board = self.draw_board()
        ways = self.evaluate_ways(board)
        return {"board": board, "lines": ways}
