from shipping_interface import CanBeShipped

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        for existing_product in self.__products:
            if existing_product.get_product_id() == product.get_product_id():
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
        print("\nCurrent Inventory:")
        print("-" * 30)
        
        if len(self.__products) == 0:
            print("Inventory is empty.")

        else:
            for product in self.__products:
                product.display_information()
                print("Fulfilment:", product.get_fulfilment_method())

                if isinstance(product, CanBeShipped):
                    print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
                
                print("-" * 30)

    def to_list(self):
        return [product.to_dict() for product in self.__products]