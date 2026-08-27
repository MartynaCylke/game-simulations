# src/calculations/statistics.py
import random
from typing import Dict, Any

def get_random_outcome(probabilities: Dict[Any,float]):
    if not probabilities:
        return None
    r = random.random()
    cum = 0.0
    for outcome, p in probabilities.items():
        cum += p
        if r <= cum:
            return outcome
    return list(probabilities.keys())[-1]
