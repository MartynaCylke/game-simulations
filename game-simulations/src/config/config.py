# src/config/config.py

class GameConfig:
    def __init__(self, game_type, target_rtp=0.96):
        self.game_type = game_type
        self.target_rtp = target_rtp

        # wspólne pola
        self.symbols = ["A", "B", "C", "D", "E", "F", "G"]
        self.symbol_values = {
            "A": 10,
            "B": 5,
            "C": 5,
            "D": 2,
            "E": 2,
            "F": 1,
            "G": 1,
            "S": 0  # Scatter ma osobny payout
        }

        # minimalna długość linii dla wygranej
        self.min_line_length = 3

        if game_type == "lines":
            self.num_reels = 5
            self.num_rows = 3
            self.symbol_pool = self.symbols
            self.paylines = [
                [0,0,0,0,0],
                [1,1,1,1,1],
                [2,2,2,2,2],
                [0,1,2,1,0],
                [2,1,0,1,2]
            ]
            self.paytable = {
                "A": {3: 10, 4: 50, 5: 200},
                "B": {3: 5, 4: 20, 5: 100},
                "C": {3: 5, 4: 20, 5: 100},
                "D": {3: 2, 4: 10, 5: 50},
                "E": {3: 2, 4: 10, 5: 50},
                "F": {3: 1, 4: 5, 5: 20},
                "G": {3: 1, 4: 5, 5: 20},
            }

        elif game_type == "ways":
            self.num_reels = 5
            self.num_rows = 3
            self.symbol_pool = self.symbols
            self.paytable = {
                "A": {3: 5, 4: 20, 5: 100},
                "B": {3: 5, 4: 20, 5: 100},
                "C": {3: 2, 4: 10, 5: 50},
                "D": {3: 2, 4: 10, 5: 50},
                "E": {3: 1, 4: 5, 5: 20},
                "F": {3: 1, 4: 5, 5: 20},
                "G": {3: 1, 4: 5, 5: 20},
            }

        elif game_type == "cluster":
            self.num_reels = 5
            self.num_rows = 5
            self.symbol_pool = self.symbols
            self.paytable = {
                "A": {3: 10, 4: 50, 5: 200},
                "B": {3: 5, 4: 20, 5: 100},
                "C": {3: 5, 4: 20, 5: 100},
                "D": {3: 2, 4: 10, 5: 50},
                "E": {3: 2, 4: 10, 5: 50},
                "F": {3: 1, 4: 5, 5: 20},
                "G": {3: 1, 4: 5, 5: 20},
            }
            self.cluster_size_min = 3

        elif game_type == "scatter":
            self.num_reels = 5
            self.num_rows = 3
            self.symbol_pool = self.symbols + ["S"]
            self.paytable = {
                "A": {3: 5, 4: 20, 5: 100},
                "B": {3: 5, 4: 20, 5: 100},
                "C": {3: 2, 4: 10, 5: 50},
                "D": {3: 2, 4: 10, 5: 50},
                "E": {3: 1, 4: 5, 5: 20},
                "F": {3: 1, 4: 5, 5: 20},
                "G": {3: 1, 4: 5, 5: 20},
                "S": {3: 2, 4: 10, 5: 50}
            }
            self.scatter = {"S": {3: 2, 4: 10, 5: 50}}
            self.paylines = [
                [0,0,0,0,0],
                [1,1,1,1,1],
                [2,2,2,2,2],
                [0,1,2,1,0],
                [2,1,0,1,2]
            ]

        else:
            raise ValueError(f"Unknown game type: {game_type}")
