# src/executables/executables.py
from typing import Any, Dict, List

class Executables:
    def __init__(self, config):
        self.config = config

    def seed_rng(self, sim_index:int):
        import random
        if getattr(self.config, "use_sim_seed", False):
            random.seed(sim_index)
