from flask import Flask, jsonify, request

from src.create_quiz import CreateQuiz

app = Flask("__name__")


@app.route("/")
def index_page():
    return jsonify({})


@app.route("/ping", methods=["GET"])
def pong():
    return jsonify({"ping": "pong"}), 200


@app.route("/create_quiz", methods=["POST"])
def create_game():
    data = request.get_json()
    if not data:
        return jsonify({"status": "failed", "message": "missing data"})
    quiz = CreateQuiz(data, debug=app.config["DEBUG"])
    result = quiz.create_quiz()
    print(result)

    return jsonify({"status": "ok", "message": "quiz created"}), 201


@app.route("/status", methods=["GET"])
def get_status():
    return jsonify({
        "data": {}
    }), 200


@app.errorhandler(405)
def method_not_allowed(*_):
    return jsonify({"message", "Request method not allowed"}), 405
