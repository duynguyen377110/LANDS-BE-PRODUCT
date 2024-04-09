import pika
from flask import json
from src.config.config import Config
from src.controller.controller_category import ControllerCategory
from src.controller.controller_product import ControllerProduct
import copy

class ShareConnect:

    connect = None
    config = Config()
    controllerCategory = ControllerCategory()
    controllerProduct = ControllerProduct()

    def __init__(self):
        url = pika.URLParameters(self.config.urlQueue)
        self.connect = pika.BlockingConnection(url)


    @classmethod
    def instance(cls):
        return cls()


    def consumer(self, queue, fn, end=False):
        channel = self.connect.channel()
        channel.queue_declare(queue=queue, durable=True)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=queue, on_message_callback=fn, auto_ack=True)
        if end:
            channel.start_consuming()

    def producer(self, queue, payload):
        properties = pika.BasicProperties(delivery_mode=2, expiration="1500")

        channel = self.connect.channel()
        channel.queue_declare(queue=queue, durable=True)  # Ensure the queue exists
        channel.basic_publish(
            exchange='',
            routing_key=queue,
            body=json.dumps(payload),
            properties=properties
        )

    def construction(self):
        # CATEGORY
        self.controllerCategory.create_category(self.consumer, self.producer)
        self.controllerCategory.update_category(self.consumer, self.producer)
        self.controllerCategory.delete_category(self.consumer, self.producer)

        # PRODUCT
        self.controllerProduct.create_product(self.consumer, self.producer)
        self.controllerProduct.update_product(self.consumer, self.producer)
        self.controllerProduct.delete_product(self.consumer, self.producer)
