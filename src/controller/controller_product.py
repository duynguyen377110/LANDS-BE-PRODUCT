from flask import json
from datetime import datetime
from flask_pymongo import ObjectId

from src.utils.util_mapper import UtilMapper
from src.controller.controller_category import ControllerCategory
from src.service.service_product import ServiceProduct
from src.config.config_queue import config_queue

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
    def create_product(self, consumer, producer):
        consumer_queue = config_queue['PRODUCT']['NEW']['CONSUMER']
        producer_queue = config_queue['PRODUCT']['NEW']['REFLY']

        def callback(ch, method, properties, body):
            data = json.loads(body.decode("utf-8"))

            payload = self.serviceProduct.create_product(data)
            producer(producer_queue, payload)

        consumer(consumer_queue, callback, False)

    # UPDATE PRODUCT
    def update_product(self, consumer, producer):
        consumer_queue = config_queue['PRODUCT']['UPDATE']['CONSUMER']
        producer_queue = config_queue['PRODUCT']['UPDATE']['REFLY']

        def callback(ch, method, properties, body):
            data = json.loads(body.decode("utf-8"))

            payload = self.serviceProduct.update_product(data)
            producer(producer_queue, payload)

        consumer(consumer_queue, callback, False)


    # DELETE PRODUCT
    def delete_product(self, consumer, producer):
        consumer_queue = config_queue['PRODUCT']['DELETE']['CONSUMER']
        producer_queue = config_queue['PRODUCT']['DELETE']['REFLY']

        def callback(ch, method, properties, body):
            data = json.loads(body.decode("utf-8"))

            payload = self.serviceProduct.delete_product(data)
            producer(producer_queue, payload)

        consumer(consumer_queue, callback, True)

