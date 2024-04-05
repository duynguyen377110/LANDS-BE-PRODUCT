from datetime import datetime
from flask import jsonify
from flask_pymongo import ObjectId

from src.utils.util_mapper import UtilMapper
from src.controller.controller_category import ControllerCategory

class ControllerProduct:
    current_time = datetime.utcnow()
    mapper = UtilMapper()
    controllerCategory = ControllerCategory()

    def __init__(self):
        pass

    def find_product_by_id(self, mongo, id):
        product_id = ObjectId(id)
        return mongo.db.products.find_one({"_id": product_id})


    # CREATE PRODUCT
    def create_product(self, mongo, data):
        data_json = self.mapper.conert_data_to_json(data)

        product = mongo.db.products.insert_one({
            'productOwner': data_json["productOwner"],
            'address': data_json["address"],
            'contact': data_json["contact"],
            'landArea': data_json["landArea"],
            'price': data_json["price"],
            'categories': ObjectId(data_json["category"]),
            'thumbs': data_json["thumbs"],
            'createdAt': self.current_time,
            'updatedAt': self.current_time
        })

        if product == None:
            return jsonify({'status': False, 'message': 'Create product unsucess'})

        result = self.controllerCategory.create_association_product({"category": data_json["category"], "product": str(product.inserted_id)})
        if result:
            return jsonify({'status': True, 'message': 'Create product sucess'})
        return jsonify({'status': False, 'message': 'Create product unsucess'})

    # UPDATE PRODUCT
    def update_product(self, mongo, data):
        data_json = self.mapper.conert_data_to_json(data)

        product = self.find_product_by_id(mongo, data_json['id'])

        payload = {
            'productOwner': data_json["productOwner"],
            'address': data_json["address"],
            'contact': data_json["contact"],
            'landArea': data_json["landArea"],
            'price': data_json["price"],
            'updatedAt': self.current_time
        }

        if str(product["categories"]) != data_json['category']:
            status_remove_association = self.controllerCategory.remove_association_product({"category": str(product["categories"]), "product": data_json['id']})
            if status_remove_association:
                status_create_association = self.controllerCategory.create_association_product({"category": data_json['category'], "product": data_json['id']})

                if status_create_association:
                    payload = {
                        'productOwner': data_json["productOwner"],
                        'address': data_json["address"],
                        'contact': data_json["contact"],
                        'landArea': data_json["landArea"],
                        'price': data_json["price"],
                        'categories': ObjectId(data_json["category"]),
                        'updatedAt': self.current_time
                    }
                else:
                    return jsonify({'status': False, 'message': 'Update product unsucess'})
            else:
                return jsonify({'status': False, 'message': 'Update product unsucess'})

        result = mongo.db.products.update_one({
            '_id': ObjectId(data_json['id'])
            },
            {
                '$set': payload,
                "$push": {'thumbs': {'$each': data_json["thumbs"]}}
            })

        if result.modified_count != 1:
            return jsonify({'status': False, 'message': 'Update product unsucess'})
        return jsonify({'status': True, 'message': 'Update product sucess'})


    # DELETE PRODUCT
    def delete_product(self, mongo, data):
        data_json = self.mapper.conert_data_to_json(data)
        product = self.find_product_by_id(mongo, data_json["id"])

        result = self.controllerCategory.remove_association_product({"category": str(product["categories"]), "product": data_json["id"]})
        if result:
            result_delete = mongo.db.products.delete_one({"_id": product["_id"]})
            if result_delete.deleted_count <= 0:
                return jsonify({'status': False, 'message': 'Delete product unsuccess', "thumbs": []})
            return jsonify({'status': True, 'message': 'Delete product success', "thumbs": product["thumbs"]})

        return jsonify({'status': False, 'message': 'Delete unsuccess', "thumbs": []})

