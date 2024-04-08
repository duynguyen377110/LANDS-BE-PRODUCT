import pika
from flask import json
from src.config.config import Config
from src.controller.controller_category import ControllerCategory

class ShareConnect:

    connect = None
    config = Config()
    controllerCategory = ControllerCategory()

    def __init__(self):
        url = pika.URLParameters(self.config.urlQueue)
        self.connect = pika.BlockingConnection(url)


    @classmethod
    def instance(cls):
        return cls()


    def consumer(self, queue, fn):
        channel = self.connect.channel()
        channel.queue_declare(queue=queue, durable=True)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=queue, on_message_callback=fn)

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
        self.controllerCategory.modify_category(self.consumer, self.producer)