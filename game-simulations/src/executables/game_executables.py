# src/executables/game_executables.py
import os
from src.executables.executables import run_single_game
from src.config import config

def run_game_simulation(game: str, sims: int = 10, books_path=None, lookup_path=None):
    """
    Wrapper to run a game simulation with optional custom paths.
    """
    if books_path is None:
        books_path = config.BOOKS_DIR
    if lookup_path is None:
        lookup_path = config.LOOKUP_DIR

    os.makedirs(books_path, exist_ok=True)
    os.makedirs(lookup_path, exist_ok=True)

    return run_single_game(game=game, sims=sims, books_path=books_path, lookup_path=lookup_path)
