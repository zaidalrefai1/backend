from flask import Flask, jsonify, request
from game_logic import Game
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can access this API

game = Game()

@app.route("/api/state", methods=["GET"])
def get_state():
    return jsonify(game.get_state())

@app.route("/api/action", methods=["POST"])
def perform_action():
    data = request.get_json()
    action = data.get("action")
    game.handle_action(action)
    return jsonify(success=True)

if __name__ == "__main__":
    app.run(debug=True)
