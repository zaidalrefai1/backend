game_state = {
    "player": {
        "location": "hub"
    },
    "base_counts": {
        "A": 5,
        "C": 5,
        "G": 5,
        "T": 5
    },
    "bases": [],
    "completed": False,
    "level": 1,
    "streak": 0
}

def reset_game():
    game_state["player"]["location"] = "hub"
    game_state["bases"] = []
    game_state["completed"] = False
    game_state["level"] = 1
    game_state["streak"] = 0

def update_location(new_location):
    game_state["player"]["location"] = new_location
