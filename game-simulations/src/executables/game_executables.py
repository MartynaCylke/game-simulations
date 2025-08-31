# src/executables/game_executables.py
import csv
import json
import os
from typing import Any
from src.config.game_config import GameConfig
from src.executables.executables import Executables
from src.calculations.lines import LinesGame
from src.calculations.scatter import ScatterGame
from src.calculations.cluster import ClusterGame
from src.calculations.ways import WaysGame  # we'll define ways below
from src.state.win_manager import WinManager

GAME_MAP = {
    "lines": LinesGame,
    "scatter": ScatterGame,
    "cluster": ClusterGame,
    "ways": None  # placeholder; will be set when WaysGame defined
}

def run_game(game_name: str, sims: int, clear: bool=False):
    cfg = GameConfig()
    # clear outputs if requested
    if clear:
        for p in (cfg.get_books_path(), cfg.get_lookup_path()):
            for f in os.listdir(p):
                os.remove(os.path.join(p,f))
    # lazy set of ways class (import circular avoidance)
    from src.calculations.ways import WaysGame as WG
    GAME_MAP["ways"] = WG

    GameClass = GAME_MAP.get(game_name)
    if GameClass is None:
        raise ValueError("Unknown game")

    # open files for writing (append)
    books_file = os.path.join(cfg.get_books_path(), f"books_{game_name}.jsonl")
    lookup_file = os.path.join(cfg.get_lookup_path(), f"lookUpTable_{game_name}.csv")

    # ensure files exist
    open(books_file,"a").close()
    open(lookup_file,"a").close()

    sim = GameClass(cfg)
    for i in range(sims):
        # seed RNG and run one round
        sim_result = sim.play_once(i)
        # Build book structure minimal required fields
        book = {
            "id": i+1,
            "payoutMultiplier": int(sim_result.get("lines",{}).get("totalWin",0) + sim_result.get("scatters",0)*0), # simplified
            "events": [],
            "criteria": "basegame",
            "baseGameWins": sim_result.get("lines",{}).get("totalWin",0),
            "freeGameWins": 0.0
        }
        # attach reveal event board
        book["events"].append({"index":0,"type":"reveal","board": sim_result.get("board")})
        # if lines info present
        if "lines" in sim_result:
            lw = sim_result["lines"]
            book["events"].append({"index":1,"type":"winInfo","totalWin": lw["totalWin"], "wins": lw["wins"]})
        if "scatters" in sim_result and sim_result["scatters"] >= 3:
            book["events"].append({"index":2,"type":"fsTrigger","scatters": sim_result["scatters"], "spins": sim_result["fs_awarded"]})
        # write book line
        with open(books_file, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(book) + "\n")
        # write lookup (id, weight(1), payout)
        with open(lookup_file, "a", encoding="utf-8", newline="") as cf:
            writer = csv.writer(cf)
            writer.writerow([book["id"], 1, book["payoutMultiplier"]])
        # print summary
        print(f"Sim {i+1}/{sims}: payout {book['payoutMultiplier']} lines {book['baseGameWins']}")
    print("Finished. Books:", books_file, "Lookup:", lookup_file)
