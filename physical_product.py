from product import Product
from shipping_interface import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier,
        weight: float
    ):
        super().__init__(
            product_id,
            name,
            price,
            stock,
            supplier
        )
        
        self.__weight = weight

    def display_information(self) -> None:
        super().display_information()
        print("Weight:", self.__weight, "kg")

    def get_fulfilment_method(self) -> None:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return 5 + (self.__weight * 2)

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data