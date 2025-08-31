# src/config/config.py

class GameConfig:
    def __init__(self, game_name: str):
        self.game_name = game_name

        # Common board settings
        self.num_reels = 5
        self.num_rows = 5
        self.symbol_pool = ["A", "B", "C", "D", "E", "F", "G"]
        self.symbols = self.symbol_pool  # alias dla gier typu ways

        # Lines game configuration
        self.paylines = [
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4],
            [0, 1, 2, 3, 4],
            [4, 3, 2, 1, 0],
        ]
        self.symbol_values = {sym: (i + 1) * 10 for i, sym in enumerate(self.symbol_pool)}
        self.min_line_length = 3

        # Cluster / Scatter / Ways game settings
        self.min_cluster = 5

        # Scatter settings
        self.scatter = {
            "symbols": ["S"],   # symbol scatter
            "value": 50         # przykładowa wartość scatter
        }

        # Paytable for ways game: symbol -> {matched_reels: payout}
        self.paytable = {sym: {self.num_reels: (i + 1) * 50} for i, sym in enumerate(self.symbol_pool)}

        # Default output directories (można nadpisać)
        self.BOOKS_DIR = "library/books"
        self.LOOKUP_DIR = "library/lookup_tables"
