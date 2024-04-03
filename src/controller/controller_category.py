from datetime import datetime
from src.utils.util_mapper import UtilMapper
class ControllerCategory:
    current_time = datetime.utcnow()
    mapper = UtilMapper()

    def __init__(self):
        pass


    def createCategory(self, mongo, data):
        # channel = connection.channel()
        # channel.queue_declare(queue="PRODUCT-ROLE", passive=True, durable=True)
        #
        # def callback(ch, method, properties, body):
        #     data = json.loads(body)
        #     print(data)
        #     mongo.db.categories.insert_one({
        #         'title': data["title"],
        #         'description': data["description"],
        #         'thumbs': data["thumbs"],
        #         'products': [],
        #         'createdAt': self.current_time,
        #         'updatedAt': self.current_time
        #     })
        #
        # channel.basic_consume(queue="PRODUCT-ROLE", on_message_callback=callback, auto_ack=True)
        #
        # print(' [*] Waiting for messages. To exit press CTRL+C')
        # channel.start_consuming()
        # connection.close()

        data = self.mapper.conert_data_to_json(data)
        print(data)
        pass