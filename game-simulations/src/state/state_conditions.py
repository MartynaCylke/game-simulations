# src/state/state_conditions.py
def check_freespin_trigger(count:int, triggers:dict):
    for k in sorted(triggers.keys(), reverse=True):
        if count >= k:
            return triggers[k]
    return 0
