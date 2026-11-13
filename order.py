from product import Product
from order_line import OrderLine

class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id

        self.order_lines: list[OrderLine] = []

    def add_order_line(
            self,
            product: Product,
            quantity: int
    ) -> None:

        order_line = OrderLine(product, quantity)

        self.order_lines.append(order_line)

    def remove_order_line(self, index: int) -> bool:
        if 0 <= index < len(self.order_lines):
            self.order_lines.pop(index)
            return True

        return False

    def calculate_total(self) -> float:
        total = 0.0

        for line in self.order_lines:
            total += line.calculate_subtotal()

        return total

    def display_order(self) -> None:
        print("\n===== ORDER DETAILS =====")
        print("Order ID:", self.order_id)

        if not self.order_lines:
            print("This order is empty.")
            return

        for line in self.order_lines:
            line.display_information()
            print("-------------------------")

        print(f"Order Total: ${self.calculate_total():.2f}")