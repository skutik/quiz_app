from flask import Flask, jsonify

app = Flask("__name__")

@app.route("/")
def index_page():
    return jsonify({})

@app.route("/ping", methods=["GET"])
def pong():
    return jsonify({"ping": "pong"}), 200

@app.route("/create_game", methods=["POST"])
def create_game():
    return jsonify({"message": "game created"}), 200

@app.route("/status", methods["GET"])
def get_status():
    return jsonify({
        "data": {}
    }), 200

@app.errorhandler(405)
def method_not_allowed(*_):
    return jsonify({"message", "Request method not allowed"}), 405
