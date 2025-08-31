# src/config/config.py
import os
from typing import Dict

class Config:
    def __init__(self, project_root: str = None):
        self.project_root = project_root or os.getcwd()
        self.paths: Dict[str,str] = {
            "books": os.path.join(self.project_root, "library", "books"),
            "force_files": os.path.join(self.project_root, "library", "force_files"),
            "lookup_tables": os.path.join(self.project_root, "library", "lookup_tables"),
            "optimization_files": os.path.join(self.project_root, "library", "optimization_files"),
        }
        self.ensure_paths()

    def ensure_paths(self):
        for p in self.paths.values():
            os.makedirs(p, exist_ok=True)

    def get_books_path(self):
        return self.paths["books"]

    def get_lookup_path(self):
        return self.paths["lookup_tables"]
