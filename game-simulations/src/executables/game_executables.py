from src.executables.executables import run_single_game

def run_game_simulation(game: str, sims: int = 10, target_rtp: float = 0.96):
    """
    Uruchamia symulację danej gry.
    :param game: "lines", "ways", "cluster" lub "scatter"
    :param sims: liczba symulacji
    :param target_rtp: docelowe RTP (0.96 = 96%)
    """
    return run_single_game(game=game, sims=sims, target_rtp=target_rtp)
