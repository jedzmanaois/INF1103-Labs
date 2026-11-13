from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from file_handler import load_inventory, save_inventory

def get_valid_integer(prompt: str) -> int:
    while True:
        value = input(prompt)

        if value.isdigit():
            return int(value)

        print("Error: Please enter a valid integer.")

def get_valid_price(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if value >= 0:
                return value

            print("Price cannot be negative. Please enter a valid price.")

        except ValueError:
            print("Error: Please enter a valid price.")

def get_valid_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("Value must be greater than zero. Please enter a valid number.")

        except ValueError:
            print("Error: Please enter a valid number.")

def add_product(inventory: Inventory, supplier: Supplier) -> None:
    print("\nAdd Product")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Choose product type: ")

    product_id = input("Enter product ID: ").strip()
    name = input("Enter product name: ").strip()

    if not product_id or not name:
        print("Product ID and name cannot be empty.")
        return

    price = get_valid_price("Price: $")
    stock = get_valid_integer("Stock quantity: ")

    if product_type == "1":
        weight = get_valid_positive_float("Weight (kg): ")
        product = PhysicalProduct(
            product_id, name, price, stock, weight, supplier
        )

    elif product_type == "2":
        download_size = get_valid_positive_float("Download size (MB): ")
        product = DigitalProduct(
            product_id, name, price, stock, download_size, supplier
        )

    else:
        print("Invalid product type.")
        return

    if inventory.add_product(product):
        print("Product added successfully.")

    else:
        print("Error: Product ID already exists.")


def update_stock(inventory: Inventory) -> None:
    product_id = input("Enter Product ID: ").strip()

    product = inventory.find_product(product_id)

    if product is not None:
        product.display_information()

        new_stock = get_valid_integer(
            "Enter new stock quantity: "
        )

        product.update_stock(new_stock)
        print("Stock updated successfully.")

    else:
        print("Product not found.")

def search_product(inventory: Inventory) -> None:
    product_id = input("Enter Product ID: ").strip()

    product = inventory.find_product(product_id)

    if product is not None:
        print("\nProduct Found")
        product.display_information()

        print("Fulfilment:", product.get_fulfilment_method())

        print("\nSupplier Information:")
        product.display_supplier()

    else:
        print("Product not found.")

def remove_product(inventory: Inventory) -> None:
    product_id = input("Enter Product ID to remove: ").strip()

    if inventory.remove_product(product_id):
        print("Product removed from inventory")

    else:
        print("Product not found.")

def create_order(inventory: Inventory) -> None:
    order_id = input("Enter Order ID: ").strip()

    if not order_id:
        print("Order ID cannot be empty.")
        return

    order = Order(order_id)

    while True:
        product_id = input(
            "Enter Product ID to order (or 'done'): "
        ).strip()

        if product_id.lower() == "done":
            break

        product = inventory.find_product(product_id)

        if product is None:
            print("Product not found.")
            continue

        quantity = get_valid_integer("Enter quantity: ")

        order.add_order_line(product, quantity)
        print("Product added to order.")

    order.display_order()

def main() -> None:

    print("=" * 40)
    print("Welcome to the Inventory Management System")
    print("=" * 40)

    supplier = Supplier(
        "S001",
        "Tech Supplies Pte Ltd",
        "sales@techsupplies.com"
    )

    inventory = load_inventory()

    while True:
        print("---------- MENU ----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Remove Product")
        print("6. Save Inventory")
        print("7. Create Order")
        print("8. Exit")
        print("--------------------------")

        option = input("Enter option: ")

        if option == "1":
            inventory.display_all()

        elif option == "2":
            add_product(inventory, supplier)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            remove_product(inventory)

        elif option == "6":
            save_inventory(inventory)

        elif option == "7":
            create_order(inventory)

        elif option == "8":
            save_inventory(inventory)
            print("\nExiting the program...")
            print("Thank you for using the Inventory Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()