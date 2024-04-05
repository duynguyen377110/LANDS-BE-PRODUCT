from flask_pymongo import ObjectId
from src.utils.util_db import UtilDb
from datetime import datetime
class ServiceCategory:

    collection = "categories"
    current_time = datetime.utcnow()
    util_db = UtilDb()

    def __init__(self):
        pass

    # CREATE CATEGORY
    def create_category(self, payload):
        try:
            category = self.util_db.open_connect(self.collection).insert_one({
                'title': payload["title"],
                'description': payload["description"],
                'thumbs': payload["thumbs"],
                'products': [],
                'createdAt': self.current_time,
                'updatedAt': self.current_time
            })
            self.util_db.close_connect()

            if not category:
                return {'status': False, 'message': 'Create category unsucess'}
            return {'status': True, 'message': 'Create category sucess'}

        except Exception as e:
            return {"status": False, "message": e}

    # CREATE ASSOCIATION PRODUCT
    def create_association_product(self, payload):
        try:
            result = self.util_db.open_connect(self.collection).update_one({
                "_id": ObjectId(payload["category"])
                },
                {'$push': {
                    'products': ObjectId(payload["product"])
                    }
                })
            self.util_db.close_connect()

            return result.modified_count > 0 if True else False

        except Exception as e:
            return {"status": False, "message": e}

    # UPDATE CATEGORY
    def update_category(self, payload):
        try:
            id = ObjectId(payload["id"])
            result = self.util_db.open_connect(self.collection).update_one({
                    '_id': id
                },
                {
                    '$set': {
                        "title": payload["title"],
                        "description": payload["description"],
                    },
                    "$push": {'thumbs': {'$each': payload["thumbs"]}}
                })
            self.util_db.close_connect()

            if result.modified_count != 1:
                return {'status': False, 'message': 'Update category unsucess'}
            return {'status': True, 'message': 'Update category sucess'}

        except Exception as e:
            return {"status": False, "message": e}


    # DELETE CATEGORY
    def delete_category(self, payload):
        try:
            id = ObjectId(payload["id"])
            category = self.util_db.open_connect(self.collection).find_one_and_delete({"_id": id})
            self.util_db.close_connect()

            if not category:
                return {'status': False, 'message': 'Delete category unsucess', "thumbs": []}
            return {'status': True, 'message': 'Delete category success', "thumbs": category['thumbs']}

        except Exception as e:
            return {"status": False, "message": e}

    # DELETE ASSOCIATION PRODUCT
    def remove_association_product(self, payload):
        try:
            result = self.util_db.open_connect(self.collection).update_one({
                "_id": ObjectId(payload["category"])
                },
                {
                    '$pull': {
                        'products': ObjectId(payload["product"])
                    }
                })
            self.util_db.close_connect()

            return result.modified_count > 0 if True else False
        except Exception as e:
            return {"status": False, "message": e}