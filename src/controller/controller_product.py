from datetime import datetime
from flask import jsonify
from flask_pymongo import ObjectId

from src.utils.util_mapper import UtilMapper
from src.controller.controller_category import ControllerCategory
from src.service.service_product import ServiceProduct

class ControllerProduct:
    current_time = datetime.utcnow()
    mapper = UtilMapper()
    controllerCategory = ControllerCategory()
    serviceProduct = ServiceProduct()

    def __init__(self):
        pass

    def find_product_by_id(self, mongo, id):
        product_id = ObjectId(id)
        return mongo.db.products.find_one({"_id": product_id})


    # CREATE PRODUCT
    def create_product(self, data):
        product_json = self.mapper.conert_data_to_json(data)
        return self.serviceProduct.create_product(product_json)

    # UPDATE PRODUCT
    def update_product(self, data):
        product_json = self.mapper.conert_data_to_json(data)
        return self.serviceProduct.update_product(product_json)


    # DELETE PRODUCT
    def delete_product(self, data):
        product_json = self.mapper.conert_data_to_json(data)
        return self.serviceProduct.delete_product(product_json)

