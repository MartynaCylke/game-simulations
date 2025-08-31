# src/executables/executables.py
import os
import csv
import json
from src.calculations import lines, ways, cluster, scatter
from src.config import config

def run_single_game(game: str, sims: int = 10, books_path=None, lookup_path=None):
    """
    Runs a simulation for the given game type.
    Saves the books (JSONL) and lookup tables (CSV) in the specified directories.
    """
    if books_path is None:
        books_path = config.BOOKS_DIR
    if lookup_path is None:
        lookup_path = config.LOOKUP_DIR

    os.makedirs(books_path, exist_ok=True)
    os.makedirs(lookup_path, exist_ok=True)

    # Select game class based on input
    if game == "lines":
        GameClass = lines.LinesGame
    elif game == "ways":
        GameClass = ways.WaysGame
    elif game == "cluster":
        GameClass = cluster.ClusterGame
    elif game == "scatter":
        GameClass = scatter.ScatterGame
    else:
        raise ValueError(f"Unknown game type '{game}'")

    # Dummy configuration (replace with real config if needed)
    game_config = config.GameConfig(game)
    game_instance = GameClass(game_config)

    books_file = os.path.join(books_path, f"books_{game}.jsonl")
    lookup_file = os.path.join(lookup_path, f"lookUpTable_{game}.csv")

    book_entries = []
    lookup_entries = []

    for sim_index in range(1, sims + 1):
        if game in ["lines", "ways"]:
            result = game_instance.play_once(sim_index)
            payout = result.get("payout", 0)
            book_entries.append({"sim": sim_index, "payout": payout})
            # Example line wins
            lookup_entries.append({"sim": sim_index, "lines": result.get("lines", 0)})
            print(f"Sim {sim_index}/{sims}: payout {payout} lines {result.get('lines',0)}")
        elif game == "cluster":
            result = game_instance.play_once(sim_index)
            clusters = result.get("clusters", [])
            total = sum(len(c["positions"]) for c in clusters)
            book_entries.append({"sim": sim_index, "total_cluster_symbols": total})
            lookup_entries.append({"sim": sim_index, "clusters": len(clusters)})
            print(f"Sim {sim_index}/{sims}: clusters {len(clusters)} total symbols {total}")
        elif game == "scatter":
            result = game_instance.play_once(sim_index)
            scatters = result.get("scatters", 0)
            payout = result.get("payout", 0)
            book_entries.append({"sim": sim_index, "payout": payout})
            lookup_entries.append({"sim": sim_index, "scatters": scatters})
            print(f"Sim {sim_index}/{sims}: payout {payout} scatters {scatters}")

    # Save JSONL (books)
    with open(books_file, "w") as f:
        for entry in book_entries:
            f.write(json.dumps(entry) + "\n")

    # Save CSV (lookup table)
    if lookup_entries:
        keys = lookup_entries[0].keys()
        with open(lookup_file, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(lookup_entries)

    print(f"Finished. Books: {books_file} Lookup: {lookup_file}")
    return {"books_file": books_file, "lookup_file": lookup_file}
