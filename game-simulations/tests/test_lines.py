# tests/test_lines.py
from src.calculations.lines import evaluate_lines_helper

def make_board(sym):
    return [[sym,sym,sym] for _ in range(5)]

def test_5_of_kind():
    board = make_board("red")
    class C: pass
    cfg = C()
    cfg.num_reels = 5
    cfg.num_rows = 3
    cfg.paylines = {0:[0,0,0,0,0]}
    cfg.paytable = {"red": {3:10,4:50,5:200}}
    cfg.wild = "WILD"
    res = evaluate_lines_helper(board, cfg)
    assert res["totalWin"] == 200
    assert len(res["wins"]) == 1
