from flask_pymongo import ObjectId
from datetime import datetime
from src.utils.util_db import UtilDb
from src.service.service_category import ServiceCategory

class ServiceProduct:

    collection = "products"
    current_time = datetime.utcnow()
    util_db = UtilDb()
    serviceCategory = ServiceCategory()

    def __init__(self):
        pass

    def find_product_by_id(self, id):
        product = self.util_db.open_connect(self.collection).find_one({"_id": ObjectId(id)})
        self.util_db.close_connect()
        return product

    # CREATE PRODUCT
    def create_product(self, payload):

        product = self.util_db.open_connect(self.collection).insert_one({
            'productOwner': payload["productOwner"],
            'address': payload["address"],
            'contact': payload["contact"],
            'landArea': payload["landArea"],
            'price': payload["price"],
            'categories': ObjectId(payload["category"]),
            'thumbs': payload["thumbs"],
            'createdAt': self.current_time,
            'updatedAt': self.current_time
        })
        self.util_db.close_connect()

        if product == None:
            return {'status': False, 'message': 'Create product unsucess'}

        result = self.serviceCategory.create_association_product({"category": payload["category"], "product": str(product.inserted_id)})

        if result:
            return {'status': True, 'message': 'Create product sucess'}
        return {'status': False, 'message': 'Create product unsucess'}


    # UPDATE CATEGORY
    def update_product(self, payload):
        product = self.find_product_by_id(payload['id'])

        if not product:
            return {"status": False, "message": "Not found product"}

        infor = {
            'productOwner': payload["productOwner"],
            'address': payload["address"],
            'contact': payload["contact"],
            'landArea': payload["landArea"],
            'price': payload["price"],
            'updatedAt': self.current_time
        }

        if str(product["categories"]) != payload['category']:

            remove_association = self.serviceCategory.remove_association_product({"category": str(product["categories"]), "product": payload['id']})
            if remove_association:
                create_association = self.serviceCategory.create_association_product({"category": payload['category'], "product": payload['id']})

                if create_association:
                    infor = {
                        'productOwner': payload["productOwner"],
                        'address': payload["address"],
                        'contact': payload["contact"],
                        'landArea': payload["landArea"],
                        'price': payload["price"],
                        'categories': ObjectId(payload["category"]),
                        'updatedAt': self.current_time
                    }
                else:
                    return {'status': False, 'message': 'Update unsucess'}
            else:
                return {'status': False, 'message': 'Update unsucess'}

        result = self.util_db.open_connect(self.collection).update_one({'_id': product["_id"]},
            {
                '$set': infor,
                "$push": {'thumbs': {'$each': payload["thumbs"]}}
            })

        self.util_db.close_connect()

        if result.modified_count != 1:
            return {'status': False, 'message': 'Update product unsucess'}
        return {'status': True, 'message': 'Update product sucess'}

    # DELETE PRODUCT
    def delete_product(self, payload):
        product = self.find_product_by_id(payload["id"])

        if not product:
            return {"status": False, "message": "Not found product"}

        remove_association = self.serviceCategory.remove_association_product({"category": str(product["categories"]), "product": payload["id"]})

        if remove_association:
            delete = self.util_db.open_connect(self.collection).delete_one({"_id": product["_id"]})
            self.util_db.close_connect()

            if delete.deleted_count <= 0:
                return {'status': False, 'message': 'Delete unsuccess', "thumbs": []}
            return {'status': True, 'message': 'Delete success', "thumbs": product["thumbs"]}

        return {'status': False, 'message': 'Delete unsuccess', "thumbs": []}