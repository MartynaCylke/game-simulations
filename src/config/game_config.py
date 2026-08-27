# src/config/game_config.py
from .config import Config
from typing import List, Dict

class GameConfig(Config):
    def __init__(self, project_root: str = None):
        super().__init__(project_root)
        # board: 5 reels x 3 rows
        self.num_reels = 5
        self.num_rows = 3

        # simple symbols (colors)
        self.symbols = ["red","yellow","blue","green","orange","purple","black"]
        self.wild = "WILD"
        self.scatter = "SCATTER"

        # include wild and scatter in symbol pool when drawing
        self.symbol_pool = self.symbols + [self.wild, self.scatter]

        # paytable for lines: payouts (multipliers) for 3,4,5 matches
        self.paytable: Dict[str, Dict[int,int]] = {
            "red":    {3:10,  4:50,  5:200},
            "yellow": {3:8,   4:40,  5:150},
            "blue":   {3:6,   4:30,  5:120},
            "green":  {3:5,   4:25,  5:100},
            "orange": {3:4,   4:20,  5:80},
            "purple": {3:3,   4:15,  5:60},
            "black":  {3:2,   4:10,  5:50},
            # wild doesn't have a direct pay in this simple model
        }

        # paylines: each list is rows for reels 0..4
        self.paylines = {
            0: [0,0,0,0,0],
            1: [1,1,1,1,1],
            2: [2,2,2,2,2],
            3: [0,1,2,1,0],
            4: [2,1,0,1,2],
        }

        # free spins triggers: scatters -> free spins
        self.freespin_triggers = {3:8, 4:10, 5:12}

        # default bet
        self.bet = 1.0

        # whether to seed RNG with sim index
        self.use_sim_seed = True
