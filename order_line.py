from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

    def display_information(self) -> None:
        print("Product:", self.product.get_product_id())
        print("Quantity:", self.quantity)
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")