import os
from src.config.config import GameConfig
from src.calculations import lines, ways, cluster, scatter

def run_single_game(game: str, sims: int = 10, target_rtp: float = 0.96, books_path=None, lookup_path=None):
    """
    Uruchamia symulacje dla jednej gry, zapisuje wyniki do books i lookup tables.
    """
    # wybór klasy gry
    if game == "lines":
        GameClass = lines.LinesGame
    elif game == "ways":
        GameClass = ways.WaysGame
    elif game == "cluster":
        GameClass = cluster.ClusterGame
    elif game == "scatter":
        GameClass = scatter.ScatterGame
    else:
        raise ValueError(f"Nieznany typ gry '{game}'")

    # konfiguracja gry z target_rtp
    config = GameConfig(game, target_rtp=target_rtp)

    # przygotowanie katalogów
    if books_path:
        os.makedirs(books_path, exist_ok=True)
    if lookup_path:
        os.makedirs(lookup_path, exist_ok=True)

    # instancja gry
    game_instance = GameClass(config=config)

    results = []
    for sim_index in range(sims):
        res = game_instance.play_once(sim_index)
        results.append(res)
        if (sim_index + 1) % 100000 == 0:
            print(f"Completed {sim_index + 1} / {sims} spins...")

    # Możesz tu dodać zapis do JSONL / CSV
    return results
