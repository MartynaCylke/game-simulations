import pytest
from src.calculations.cluster import calculate_cluster_wins

def test_single_cluster():
    # plansza 5x5 z dużym klastrem "A"
    reels = [
        ["A", "A", "A", "B", "C"],
        ["A", "B", "A", "B", "C"],
        ["A", "A", "A", "B", "C"],
        ["D", "E", "F", "G", "H"],
        ["A", "A", "A", "B", "C"],
    ]

    wins = calculate_cluster_wins(reels)
    assert isinstance(wins, list)
    assert any(w["symbol"] == "A" for w in wins), "Powinien być klaster A"
    assert sum(w["size"] for w in wins) >= 5, "Powinien mieć co najmniej 5 symboli"

def test_no_clusters():
    # plansza 5x5 bez żadnych klastrów (tylko pojedyncze litery)
    reels = [
        ["A", "B", "C", "D", "E"],
        ["F", "G", "H", "I", "J"],
        ["K", "L", "M", "N", "O"],
        ["P", "Q", "R", "S", "T"],
        ["U", "V", "W", "X", "Y"],
    ]

    wins = calculate_cluster_wins(reels)
    assert wins == [], "Nie powinno być klastrów"
def calculate_cluster_wins(board):
    game = ClusterGame(config=DummyConfig())
    result = game.play_once(sim_index=0)
    return result["clusters"]

# DummyConfig potrzebne do uruchomienia funkcji samodzielnie
class DummyConfig:
    symbol_pool = ["A","B","C","D"]
    num_reels = 6
    num_rows = 5
