from product import Product
from shipping_interface import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print("Weight:", self.__weight, "kg")

    def get_fulfillment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return 5 + (self.__weight * 2)

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data