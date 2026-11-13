from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier
    ):
        self.__product_id: str = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.supplier: Supplier = supplier
        
    @property
    def price(self) -> float:
         return self.__price
    
    def get_product_id(self) -> str:
        return self.__product_id

    def update_stock(self, new_stock: int) -> None:
        self.__stock = new_stock

    def display_information(self) -> None:
            print("Product ID:", self.__product_id)
            print("Name:", self.__name)
            print(f"Price: ${self.__price:.2f}")
            print("Stock:", self.__stock)

    def display_supplier(self) -> None:
         self.supplier.display_information()

    @abstractmethod
    def get_fulfilment_method(self):
        pass

    def to_dict(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.supplier.to_dict()
        }