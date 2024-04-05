from pymongo import MongoClient
from src.config.config import Config

class UtilDb:
    config = Config()
    client = None
    def __init__(self):
        pass

    def open_connect(self, collection_name):
        self.client = MongoClient(self.config.urlDB)
        db = self.client["lands-store"]
        return db[collection_name]

    def close_connect(self):
        self.client.close()
