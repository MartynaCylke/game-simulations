from src.state.win_manager import WinManager

class GeneralGameState:
    def __init__(self, config):
        self.config = config
        self.win_manager = WinManager("base", "free")
        self.board = []
        self.book = {"events": []}

    def reset_book(self):
        self.board = []
        self.book = {"events": []}
