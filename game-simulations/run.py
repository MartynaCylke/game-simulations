# run.py
import argparse
from src.executables.game_executables import run_game

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--game", type=str, default="lines", choices=["lines","ways","scatter","cluster"], help="Game type")
    parser.add_argument("--sims", type=int, default=100, help="Simulations")
    parser.add_argument("--clear", action="store_true", help="Clear library output")
    args = parser.parse_args()

    run_game(args.game, args.sims, clear=args.clear)

if __name__ == "__main__":
    main()
