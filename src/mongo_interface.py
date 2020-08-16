import os

from pymongo import MongoClient

from config.config import *


class MongoInterface:
    def __init__(self, debug=False):
        db_name = PRODUCTION_DATABASE if debug is False else PRODUCTION_DATABASE
        conn_string = f"mongodb+srv://rw_dave:{os.getenv('MONGODB_RW_PASS')}@cluster0-6lpd8.mongodb.net/{db_name}?retryWrites=true&w=majority"
        self.client = MongoClient(conn_string)

    def create_game(self, json_data):
        pass