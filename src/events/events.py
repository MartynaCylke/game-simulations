# src/events/events.py
import copy

def reveal_event(gamestate):
    ev = {"index": len(gamestate["events"]) if "events" in gamestate else 0, "type":"reveal", "board": copy.deepcopy(gamestate.get("board"))}
    gamestate.setdefault("events", []).append(ev)
