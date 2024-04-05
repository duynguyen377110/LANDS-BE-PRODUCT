from src.utils.util_mapper import UtilMapper
from src.service.service_category import ServiceCategory

class ControllerCategory:

    serviceCategory = ServiceCategory()
    mapper = UtilMapper()

    def __init__(self):
        pass

    # CREATE CATEGORY
    def create_category(self, data):
        category_json = self.mapper.conert_data_to_json(data)
        return self.serviceCategory.create_category(category_json)

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