import csv
import json
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

    books_path = books_path or os.path.join("library", "books")
    lookup_path = lookup_path or os.path.join("library", "lookup_tables")
    os.makedirs(books_path, exist_ok=True)
    os.makedirs(lookup_path, exist_ok=True)

    # instancja gry
    game_instance = GameClass(config=config)

    results = []
    for sim_index in range(sims):
        res = game_instance.play_once(sim_index)
        results.append(res)
        if (sim_index + 1) % 100000 == 0:
            print(f"Completed {sim_index + 1} / {sims} spins...")

    book_file = os.path.join(books_path, f"books_{game}.jsonl")
    with open(book_file, "w", encoding="utf-8") as output:
        for result in results:
            output.write(json.dumps(result) + "\n")

    lookup_file = os.path.join(lookup_path, f"lookUpTable_{game}.csv")
    with open(lookup_file, "w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=["spin_index", "total_win"])
        writer.writeheader()
        for spin_index, result in enumerate(results):
            total_win = result.get("total", 0)
            if isinstance(result.get("lines"), dict):
                total_win = result["lines"].get("totalWin", result["lines"].get("total", total_win))
            writer.writerow({"spin_index": spin_index, "total_win": total_win})

    return results
