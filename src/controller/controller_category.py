from datetime import datetime
from flask import jsonify
from flask_pymongo import ObjectId
from src.utils.util_mapper import UtilMapper

class ControllerCategory:
    current_time = datetime.utcnow()
    mapper = UtilMapper()

    def __init__(self):
        pass

    # FIND CATEGORY BY ID
    def find_category_by_id(self, mongo, id):
        category_id = ObjectId(id)
        return mongo.db.categories.find_one({"_id": category_id})

    # CREATE CATEGORY
    def create_category(self, mongo, data):
        data_json = self.mapper.conert_data_to_json(data)

        category = mongo.db.categories.insert_one({
            'title': data_json["title"],
            'description': data_json["description"],
            'thumbs': data_json["thumbs"],
            'products': [],
            'createdAt': self.current_time,
            'updatedAt': self.current_time
        })

        if category == None:
            return jsonify({'status': False, 'message': 'Create category unsucess'})
        return jsonify({'status': True, 'message': 'Create category sucess'})

    # DELETE CATEGORY BY ID
    def delete_category(self, mongo, data):
        data_json = self.mapper.conert_data_to_json(data)
        category = self.find_category_by_id(mongo, data_json["id"])

        if category == None:
            return jsonify({'status': False, 'message': 'Not found category', "thumbs": []})

        category_id = ObjectId(data_json["id"])
        result = mongo.db.categories.delete_one({"_id": category_id})

        if result.deleted_count != 1:
            return jsonify({'status': False, 'message': 'Delete category unsucess', "thumbs": []})
        return jsonify({'status': True, 'message': 'Delete category success', "thumbs": category['thumbs']})
