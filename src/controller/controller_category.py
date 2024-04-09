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
            data = json.loads(body.decode("utf-8"))

            payload = self.serviceCategory.create_category(data)
            producer(producer_queue, payload)

        consumer(consumer_queue, callback, False)

    # UPDATE CATEGORY
    def update_category(self, data):
        category_json = self.mapper.conert_data_to_json(data)
        return self.serviceCategory.update_category(category_json)

    # DELETE CATEGORY BY ID
    def delete_category(self, consumer, producer):
        consumer_queue = config_queue['CATEGORY']['DELETE']['CONSUMER']
        producer_queue = config_queue['CATEGORY']['DELETE']['REFLY']

        def callback(ch, method, properties, body):
            data = json.loads(body.decode("utf-8"))

            payload = self.serviceCategory.delete_category(data)
            producer(producer_queue, payload)

        consumer(consumer_queue, callback, True)

    # CREATE ASSOCIAION CATEGORY - PRODUCT
    def create_association_product(self, data):
        return self.serviceCategory.create_association_product(data)

    # DELET ASSOCIAION CATEGORY - PRODUCT
    def remove_association_product(self, data):
        return self.serviceCategory.remove_association_product(data)