from src.utils.util_mapper import UtilMapper
from src.service.service_category import ServiceCategory
from src.config.config_queue import config_queue
import pika
from flask import json
import copy

class ControllerCategory:

    serviceCategory = ServiceCategory()
    mapper = UtilMapper()

    def __init__(self):
        pass

    def create_category(self, consumer, producer):
        consumer_queue = config_queue['CATEGORY']['NEW']['CONSUMER']
        producer_queue = config_queue['CATEGORY']['NEW']['REFLY']

        def callback(ch, method, properties, body):
            print("Received message:", body)

            producer(
                producer_queue,
                {"status": True, "message": "Create category success"}
            )
        consumer(consumer_queue, callback, True)

    # UPDATE CATEGORY
    def update_category(self, data):
        category_json = self.mapper.conert_data_to_json(data)
        return self.serviceCategory.update_category(category_json)

    # DELETE CATEGORY BY ID
    def delete_category(self, data):
        category_json = self.mapper.conert_data_to_json(data)
        return self.serviceCategory.delete_category(category_json)

    # CREATE ASSOCIAION CATEGORY - PRODUCT
    def create_association_product(self, data):
        return self.serviceCategory.create_association_product(data)

    # DELET ASSOCIAION CATEGORY - PRODUCT
    def remove_association_product(self, data):
        return self.serviceCategory.remove_association_product(data)