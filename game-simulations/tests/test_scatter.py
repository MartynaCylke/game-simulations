# tests/test_scatter.py
from src.calculations.scatter import count_scatters

def test_scatters_count():
    board = [["SCATTER","A","B"],["A","SCATTER","C"],["D","E","SCATTER"],["X","Y","Z"],["P","Q","R"]]
    count, positions = count_scatters(board, "SCATTER")
    assert count == 3
    assert len(positions) == 3
