# tests/test_tumble_cluster.py
import pytest
from src.calculations.cluster import find_clusters
from src.calculations.tumble import remove_positions, tumble_reels

def test_tumble_cluster_mechanics():
    # plansza 5x5 z kilkoma klastrami "A"
    reels = [
        ["A", "A", "A", "B", "C"],
        ["B", "C", "A", "B", "C"],
        ["A", "A", "A", "B", "C"],
        ["D", "E", "F", "G", "H"],
        ["A", "A", "A", "B", "C"],
    ]

    # znajdowanie klastrów na planszy (deterministycznie)
    wins = find_clusters(reels, min_cluster=3)
    assert any(w["symbol"] == "A" for w in wins), "Powinien być klaster A"
    
    # przygotowanie pozycji do usunięcia (wszystkie znalezione klastry)
    positions_to_remove = []
    for cluster in wins:
        positions_to_remove.extend(cluster["positions"])
    
    # usuń symbole klastra
    new_reels = remove_positions(reels, positions_to_remove)
    
    # symulacja tumble (uzupełnienie pustych miejsc losowymi symbolami)
    symbol_pool = ["A","B","C","D"]
    tumbled_reels = tumble_reels(new_reels, symbol_pool=symbol_pool)

    # testy długości planszy
    assert len(tumbled_reels) == len(reels)
    assert all(len(col) == len(reels[0]) for col in tumbled_reels)
    # test zmiany planszy
    assert tumbled_reels != reels, "Po tumble plansza powinna się zmienić"
