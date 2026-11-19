from supplier import Supplier
from inventory import Inventory
from order import Order

from product_factory import ProductFactory
from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)

from file_handler import load_products

def get_positive_float(prompt: str) -> float:

    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a number greaterthan zero.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

def get_positive_integer(prompt: str) -> int:

    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Please enter a number greater than zero.")
                continue

            return value

        except ValueError:
            print("Please enter a valid whole number.")

def get_nonnegative_integer(prompt: str) -> int:

    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("Stock cannot be negative.")
                continue

            return value

        except ValueError:
            print("Please enter a valid whole number.")

def add_product(inventory: Inventory, supplier: Supplier) -> None:

    try:
        product_type = input(
            "Enter product type (physical/digital): "
        ).lower().strip()

        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")

        price = get_positive_float("Enter Price: ")

        stock = get_nonnegative_integer("Enter Stock Quantity: ")

        product = ProductFactory.create(
            product_type,
            product_id,
            name,
            price,
            stock,
            supplier
        )

        if inventory.add_product(product):
            print("Product added successfully.")

    except ValueError as error:
        print("Unable to add product:", error)

def create_order(inventory: Inventory) -> None:

    order_id = input("Enter Order ID: ")

    discount_choice = input(
        "Choose discount (none/percentage/bulk/student): "
    ).lower().strip()

    try:
        if discount_choice == "none":
            discount = NoDiscount()

        elif discount_choice == "percentage":
            percentage = get_positive_float(
                "Enter discountp percentage: "
            )

            discount = PercentageDiscount(percentage)

        elif discount_choice == "bulk":
            threshold = get_positive_float(
                "Enter minimum order amount: "
            )

            amount = get_positive_float(
                "Enter discount amount: "
            )

            discount = BulkDiscount(threshold, amount)

        elif discount_choice == "student":
            discount = StudentDiscount()

        else:
            raise ValueError("Unknown discount type.")

        order = Order(order_id, discount)

        while True:
            product_id = input(
                "Enter Product ID (or quit to finish): "
            )

            if product_id.lower() == "quit":
                break

            product = inventory.find_product(product_id)

            if product is None:
                print("Product not found")
                continue

            quantity = get_positive_integer(
                "Enter Quantity: "
            )

            try:
                order.add_order_line(product, quantity)
                print("Product added to order.")

            except ValueError as error:
                print("Unable to add order line:", error)

        order.display_order()

    except ValueError as error:
        print("Unable to create order:", error)

def main():

    inventory = Inventory()

    supplier = Supplier(
        "S001",
        "Tech Supplies Pte Ltd",
        "sales@techsupplies.com"
    )

    load_products("products.csv", inventory, supplier)

    while True:
        print("---------- MENU ----------")
        print("1. Display Inventory")
        print("2. Add Product")
        print("3. Create Order")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product(inventory, supplier)

        elif choice == "3":
            create_order(inventory)

        elif choice == "4":
            print("Exiting Inventory Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()