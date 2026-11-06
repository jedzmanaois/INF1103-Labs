from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from file_handler import load_inventory, save_inventory

def get_valid_integer(prompt):
    while True:
        value = input(prompt)

        if value.isdigit():
            return int(value)

        print("Error: Please enter a valid integer.")

def get_valid_price(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value >= 0:
                return value

            print("Price cannot be negative. Please enter a valid price.")

        except ValueError:
            print("Error: Please enter a valid price.")

def get_valid_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("Value must be greater than zero. Please enter a valid number.")

        except ValueError:
            print("Error: Please enter a valid number.")

def add_product(inventory):
    print("\nAdd Product")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Choose product type: ")

    product_id = input("Enter product ID: ").strip()
    name = input("Enter product name: ").strip()

    if product_id == "" or name == "":
        print("Product ID and name cannot be empty.")
        return

    price = get_valid_price("Price: $")
    stock = get_valid_integer("Stock quantity: ")

    if product_type == "1":
        weight = get_valid_positive_float("Weight (kg): ")
        product = PhysicalProduct(product_id, name, price, stock, weight)

    elif product_type == "2":
        download_size = get_valid_positive_float("Download size (MB): ")
        product = DigitalProduct(product_id, name, price, stock, download_size)

    else:
        print("Invalid product type.")
        return

    if inventory.add_product(product):
        print("Product added successfully.")

    else:
        print("Error: Product ID already exists.")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is not None:
        product.display_information()
        new_stock = get_valid_integer("Enter new stock quantity: ")
        product.update_stock(new_stock)
        print("Stock updated successfully.")
    else:
        print("Product not found.")

def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is not None:
        print("\nProduct Found")
        product.display_information()
        print("Fulfilment:", product.get_fulfilment_method())

    else:
        print("Product not found.")

def main():

    print("=" * 40)
    print("Welcome to the Inventory Management System")
    print("=" * 40)

    inventory = load_inventory()

    while True:
        print("---------- MENU ----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("--------------------------")

        option = input("Enter option: ")

        if option == "1":
            inventory.display_all()

        elif option == "2":
            add_product(inventory)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            search_product(inventory)

        elif option == "5":
            save_inventory(inventory)

        elif option == "6":
            save_inventory(inventory)
            print("\nExiting the program...")
            print("Thank you for using the Inventory Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()