# tests/test_integration.py
import os
import pytest
from src.executables.game_executables import run_game_simulation

GAMES = ["lines", "ways", "cluster", "scatter"]

def test_game_integration(tmp_path):
    """
    Integration test: Run each game type for a few sims, check books and lookup tables.
    Uses a temporary directory so nie nadpisuje istniejących plików.
    """
    # Prepare temporary library paths
    books_dir = tmp_path / "books"
    lookup_dir = tmp_path / "lookup_tables"
    books_dir.mkdir()
    lookup_dir.mkdir()

    for game_name in GAMES:
        result = run_game_simulation(
            game=game_name,
            sims=3,
            books_path=str(books_dir),
            lookup_path=str(lookup_dir),
        )

        # Check that files were created
        book_file = books_dir / f"books_{game_name}.jsonl"
        lookup_file = lookup_dir / f"lookUpTable_{game_name}.csv"

        assert book_file.exists(), f"Books file missing for {game_name}"
        assert lookup_file.exists(), f"Lookup table missing for {game_name}"

        # Check that files are not empty
        assert book_file.stat().st_size > 0, f"Books file empty for {game_name}"
        assert lookup_file.stat().st_size > 0, f"Lookup table empty for {game_name}"
