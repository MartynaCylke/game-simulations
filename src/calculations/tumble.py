# src/calculations/tumble.py
from typing import List, Tuple
import random

def remove_positions(board: List[List[str]], positions: List[Tuple[int,int]]) -> List[List[str]]:
    """
    Usuwa symbole z podanych pozycji (c, r) i wypełnia kolumny None na górze.
    """
    if not positions:
        return board
    posset = set(positions)
    cols = len(board)
    rows = len(board[0])
    for c in range(cols):
        newcol = []
        for r in range(rows):
            if (c,r) not in posset:
                newcol.append(board[c][r])
        missing = rows - len(newcol)
        board[c] = [None]*missing + newcol
    return board

def tumble_reels(board: List[List[str]], symbol_pool: List[str]=None) -> List[List[str]]:
    """
    Symuluje spadanie symboli w kaskadzie (tumbling).
    Każda kolumna przesuwa symbole w dół, puste miejsca uzupełniane losowymi symbolami z symbol_pool.
    Funkcja gwarantuje zmianę planszy.
    """
    cols = len(board)
    rows = len(board[0]) if cols > 0 else 0

    # jeśli brak symbol_pool, użyj istniejących symboli w planszy
    if symbol_pool is None:
        symbol_pool = [s for col in board for s in col if s is not None]

    new_board = []
    for c in range(cols):
        col = board[c]
        filtered = [s for s in col if s is not None]
        missing = rows - len(filtered)
        # wypełnij puste miejsca losowymi symbolami
        new_col = [random.choice(symbol_pool) for _ in range(missing)] + filtered
        # wymuś zmianę jeśli przypadkiem nowa kolumna jest identyczna
        if new_col == col:
            if symbol_pool:
                new_col[random.randint(0, rows-1)] = random.choice(symbol_pool)
        new_board.append(new_col)
    return new_board
