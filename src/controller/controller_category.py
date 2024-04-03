from datetime import datetime
from flask import jsonify
from src.utils.util_mapper import UtilMapper

class ControllerCategory:
    current_time = datetime.utcnow()
    mapper = UtilMapper()

    def __init__(self):
        pass


    def createCategory(self, mongo, data):
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