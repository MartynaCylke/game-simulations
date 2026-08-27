import pandas as pd
import os

# -----------------------------
# Pliki lookup tables dla każdej gry
# -----------------------------
files = {
    "lines": "library/lookup_tables/lookUpTable_lines.csv",
    "ways": "library/lookup_tables/lookUpTable_ways.csv",
    "cluster": "library/lookup_tables/lookUpTable_cluster.csv",
    "scatter": "library/lookup_tables/lookUpTable_scatter.csv",
}

target_rtp = 0.96  # 96% RTP
bet_per_spin = 1.0  # stawka za spin

for game, path in files.items():
    if not os.path.exists(path):
        print(f"❌ Brak pliku: {path}")
        continue

    # Wczytanie CSV
    df = pd.read_csv(path, header=None)
    # kolumny: col0 = ID, col1 = waga, col2 = payout

    # Normalizacja wag
    df[1] = df[1] / df[1].sum()

    # Obliczenie skalującego współczynnika
    expected_win = (df[1] * df[2]).sum()
    scaling_factor = target_rtp * bet_per_spin / expected_win

    # Przeskalowanie wypłat
    df[2] = df[2] * scaling_factor

    # Nadpisanie CSV z nowymi wartościami
    df.to_csv(path, header=False, index=False)

    # Sprawdzenie teoretycznego RTP po skalowaniu
    rtp = (df[1] * df[2]).sum() / bet_per_spin * 100
    print(f"✅ {game.capitalize()} -> RTP po skalowaniu = {rtp:.2f}%")
