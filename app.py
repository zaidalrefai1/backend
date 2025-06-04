from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

STATE_FILE = 'game_state.json'

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {
        "scene": "hub",
        "level": 1,
        "streak": 0,
        "completed": False,
        "base_counts": {"A": 5, "T": 5, "C": 5, "G": 5},
        "bases": []
    }

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f)

@app.route("/game-state")
def get_state():
    return jsonify(load_state())

@app.route("/update-location", methods=["POST"])
def update_location():
    data = request.get_json()
    state = load_state()
    state["scene"] = data.get("location", "hub")
    save_state(state)
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
