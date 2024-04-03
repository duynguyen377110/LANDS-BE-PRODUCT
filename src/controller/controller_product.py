from datetime import datetime
from flask import jsonify
from flask_pymongo import ObjectId
from src.utils.util_mapper import UtilMapper

class ControllerProduct:
    current_time = datetime.utcnow()
    mapper = UtilMapper()

    def __init__(self):
        pass

    # CREATE PRODUCT
    def create_product(self, mongo, data):
        pass

    # UPDATE PRODUCT
    def update_product(self, mong, data):
        pass

    # DELETE PRODUCT
    def delete_product(self, mongo, data):
        pass