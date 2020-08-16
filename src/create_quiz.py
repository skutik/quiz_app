import json
from voluptuous.error import MultipleInvalid
from voluptuous import ALLOW_EXTRA, Schema, Optional, Range, All, Required, Length

from src.mongo_interface import MongoInterface


class CreateQuiz:
    def __init__(self, data, debug=False):
        self.data = data
        self.mongo_client = MongoInterface(debug=debug)
        self.post_data_schema = Schema({
            Required("name"): str,
            Required("created_by"): str,
            Required("question_limit"): int,
            Required("randomize_answers"): bool,
            Required("questions"):  [All({
                Required("title"): str,
                Required("answers"): All([int, float, str], Length(min=2, max=4)),
                Required("correct_answer"): int
            }, Length(min=1, max=10))]
        })

    def create_quiz(self):
        if "question_limit" not in self.data:
            self.data["question_limit"] = 30

        try:
            self.post_data_schema(self.data)
        except MultipleInvalid:
            return "failed"

        return "ok"