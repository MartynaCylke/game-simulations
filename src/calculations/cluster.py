from typing import List, Dict, Any
from collections import deque
import random

def find_clusters(board: List[List[str]], min_cluster: int = 5):
    cols = len(board)
    rows = len(board[0]) if cols else 0
    visited = [[False]*cols for _ in range(rows)]
    clusters = []

    def neighbors(r,c):
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0<=nr<rows and 0<=nc<cols:
                yield nr, nc

    for r in range(rows):
        for c in range(cols):
            if visited[r][c]:
                continue
            sym = board[c][r]
            if sym is None:
                continue
            q = deque()
            q.append((r,c))
            comp = []
            visited[r][c] = True
            while q:
                rr, cc = q.popleft()
                comp.append((cc, rr))
                for nr, nc in neighbors(rr,cc):
                    if not visited[nr][nc] and board[nc][nr] == sym:
                        visited[nr][nc] = True
                        q.append((nr,nc))
            if len(comp) >= min_cluster:
                clusters.append({"symbol": sym, "positions": comp, "size": len(comp)})
    return clusters

class ClusterGame:
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
        clusters = find_clusters(board, min_cluster=5)
        return {"board": board, "clusters": clusters}

# Funkcja potrzebna do testów
def calculate_cluster_wins(board):
    result = {"board": board, "clusters": find_clusters(board, min_cluster=5)}
    return result["clusters"]
