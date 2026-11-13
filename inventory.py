from shipping_interface import CanBeShipped
from product import Product

class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    @property
    def products(self) -> list[Product]:
        return list(self.__products)

    def add_product(self, product: Product) -> bool:
        for existing_product in self.__products:
            if ( 
                existing_product.get_product_id() == product.get_product_id()
            ):
                print("Product with this ID already exists.")
                return False

        self.__products.append(product)
        return True

    def remove_product(self, product_id: str) -> bool:
        for product in self.products:
            if product.get_product_id() == product_id:
                self.products.remove(product)
                return True

        return False

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_product_id() == product_id:
                return product

        return None

    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def display_all(self):
        if not self.products:
            print("Inventory is empty.")
            return
        
        print("\nCurrent Inventory:")
        print("-" * 30)

        for product in self.products:
            product.display_information()

            print(
                "Fulfilment:", product.get_fulfilment_method()
            )

            if isinstance(product, CanBeShipped):
                    print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
                
            print("-" * 30)

    def to_list(self) -> list[dict]:
        return [product.to_dict() for product in self.__products]