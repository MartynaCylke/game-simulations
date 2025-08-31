# run.py
import argparse
from src.executables.game_executables import LinesGameExecutable, WaysGameExecutable, ClusterGameExecutable, ScatterGameExecutable

GAME_MAP = {
    "lines": LinesGameExecutable,
    "ways": WaysGameExecutable,
    "cluster": ClusterGameExecutable,
    "scatter": ScatterGameExecutable,
}

def print_board(board):
    """Wyświetla planszę w terminalu w czytelnej formie."""
    if not board:
        return
    rows = len(board[0])
    cols = len(board)
    for r in range(rows):
        row_symbols = [board[c][r] if board[c][r] is not None else "." for c in range(cols)]
        print(" | ".join(row_symbols))
    print("-" * (cols * 4 - 1))

def main():
    parser = argparse.ArgumentParser(description="Run game simulations")
    parser.add_argument("--game", type=str, required=True, help="Game type: lines, ways, cluster, scatter")
    parser.add_argument("--sims", type=int, default=10, help="Number of simulations")
    args = parser.parse_args()

    if args.game not in GAME_MAP:
        print(f"Error: invalid game type '{args.game}'. Choose from {list(GAME_MAP.keys())}")
        return

    GameClass = GAME_MAP[args.game]
    game = GameClass()

    num_sims = args.sims
    print(f"Running {num_sims} simulations for '{args.game}' game...\n")

    for sim_index in range(num_sims):
        result = game.play_once(sim_index)
        board = result.get("board", [])
        payout = result.get("payout", 0)
        wins = result.get("clusters", []) or result.get("lines", [])
        
        print(f"Sim {sim_index + 1}/{num_sims}: payout {payout}")
        print_board(board)
        print(f"Wins: {wins}\n")

    print(f"Finished. Books: {game.books_file} Lookup: {game.lookup_file}")

if __name__ == "__main__":
    main()
