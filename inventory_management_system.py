import json

class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print("Product ID:", self.__product_id)
        print("Name:", self.__name)
        print(f"Price: ${self.__price:.2f}")
        print("Stock: self.__stock")

    def to_dict(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["product_id"],
            data["name"],
            data["price"],
            data["stock"]
        )

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):

        if self.searchproduct(product.get_product_id()) is not None:
            print("Product with this ID already exists.")
            return False

        self.__products.append(product)
        return True

    def search_product(self, product_id):

        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
            
        return None

    def display_all(self):

        print("\Current Inventory:")
        print("-" * 50)

        if len(self.__products) == 0:
            print("Inventory is empty.")
            return

        else:
            for product in self.__products:
                product.display_information()
                print("-" * 50)

    def to_list(self):
        return [product.to_dict() for product in self.__products]