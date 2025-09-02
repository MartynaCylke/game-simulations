import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# Pliki lookup tables dla każdej gry
# -----------------------------
files = {
    "lines": "library/lookup_tables/lookUpTable_lines.csv",
    "ways": "library/lookup_tables/lookUpTable_ways.csv",
    "cluster": "library/lookup_tables/lookUpTable_cluster.csv",
    "scatter": "library/lookup_tables/lookUpTable_scatter.csv",
}

bet_per_spin = 1.0          # stawka za jeden spin
num_simulations = 100000    # liczba spinów do symulacji

for game, path in files.items():
    if not os.path.exists(path):
        print(f"❌ Brak pliku: {path}")
        continue

    # -----------------------------
    # Wczytanie CSV
    # -----------------------------
    df = pd.read_csv(path, header=None)
    # kolumny: col0 = ID, col1 = waga, col2 = payout

    # -----------------------------
    # Normalizacja wag, żeby suma = 1
    # -----------------------------
    df[1] = df[1] / df[1].sum()

    # -----------------------------
    # Teoretyczne RTP
    # -----------------------------
    expected_win = (df[1] * df[2]).sum()
    rtp = expected_win / bet_per_spin * 100
    print(f"🎰 {game.capitalize()} -> RTP teoretyczne = {rtp:.2f}%")

    # -----------------------------
    # Symulacja losowych spinów
    # -----------------------------
    payouts = df[2].to_numpy()
    probabilities = df[1].to_numpy()

    rng = np.random.default_rng()
    simulated_spins = rng.choice(payouts, size=num_simulations, p=probabilities)

    cumulative_rtp = np.cumsum(simulated_spins) / np.arange(1, num_simulations + 1) / bet_per_spin * 100

    # -----------------------------
    # Wykres konwergencji RTP
    # -----------------------------
    plt.figure(figsize=(10, 5))
    plt.plot(cumulative_rtp, color='blue')
    plt.axhline(rtp, color='red', linestyle='--', label=f'Teoretyczne RTP ({rtp:.2f}%)')
    plt.title(f"Konwergencja RTP – {game.capitalize()}")
    plt.xlabel("Liczba spinów")
    plt.ylabel("RTP (%)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
