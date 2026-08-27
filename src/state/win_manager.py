# src/state/win_manager.py
class WinManager:
    def __init__(self, base_mode="base", free_mode="free"):
        self.base_mode = base_mode
        self.free_mode = free_mode
        self.total_cumulative_wins = 0.0
        self.cumulative_base_wins = 0.0
        self.cumulative_free_wins = 0.0
        self.running_bet_win = 0.0
        self.basegame_wins = 0.0
        self.freegame_wins = 0.0
        self.spin_win = 0.0
        self.tumble_win = 0.0

    def set_spinwin(self, amount):
        self.spin_win = amount

    def add_to_running(self):
        self.running_bet_win += self.spin_win
        self.spin_win = 0.0

    def commit_round(self):
        self.total_cumulative_wins += self.running_bet_win
        self.running_bet_win = 0.0
