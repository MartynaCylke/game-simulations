#!/usr/bin/env python3
import argparse
from src.executables.game_executables import run_game_simulation

def main():
    parser = argparse.ArgumentParser(description="Run game simulations")
    parser.add_argument("--game", type=str, required=True, choices=["lines", "ways", "cluster", "scatter"],
                        help="Type of game to simulate")
    parser.add_argument("--sims", type=int, default=10, help="Number of simulations to run")
    parser.add_argument("--rtp", type=float, default=0.96, help="Target RTP (Return To Player) as decimal, e.g., 0.96")
    args = parser.parse_args()

    print(f"Running {args.sims} simulations for '{args.game}' with target RTP {args.rtp*100:.2f}%...")

    result = run_game_simulation(game=args.game, sims=args.sims, target_rtp=args.rtp)

    print("Simulation finished.")
    print(f"Results saved to Books and Lookup Tables.")

if __name__ == "__main__":
    main()
