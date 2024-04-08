from src.utils.util_mapper import UtilMapper
from src.service.service_category import ServiceCategory
from src.config.config_queue import config_queue

class ControllerCategory:

    serviceCategory = ServiceCategory()
    mapper = UtilMapper()

    def __init__(self):
        pass

    # CREATE CATEGORY
    def create_category(self, data):
        category_json = self.mapper.conert_data_to_json(data)
        return self.serviceCategory.create_category(category_json)

    def modify_category(self, consumer, producer):
        consumer_queue = config_queue['CREATE_CATEGORY']['CONSUMER_CATEGORY']
        refly_queue = config_queue['CREATE_CATEGORY']['REFLY_CATEGORY']
        def callback(ch, method, properties, body):
            print("Received message:", body)
            # Perform processing here

            producer(refly_queue, {"status": True, "message": "Hello system"})

            # Acknowledge the message
            ch.basic_ack(delivery_tag=method.delivery_tag)

        consumer(consumer_queue, callback)


    # def callback(self, ch, method, properties, body):
    #     print("Received message:", body)
    #     # Perform processing here
    #
    #     # Acknowledge the message
    #     ch.basic_ack(delivery_tag=method.delivery_tag)

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