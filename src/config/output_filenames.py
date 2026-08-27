import os

class OutputFiles:
    @staticmethod
    def make_path(folder, filename):
        os.makedirs(folder, exist_ok=True)
        return os.path.join(folder, filename)
