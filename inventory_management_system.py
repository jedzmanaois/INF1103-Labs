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
            data["id"],
            data["name"],
            data["price"],
            data["stock"]
        )


class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):

        if self.search_product(product.get_product_id()) is not None:
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


def load_inventory():

    try:
        with open("inventory.json", "r") as file:

            data = json.load(file)

            inventory = Inventory()

            for item in data:
                product = Product.from_dict(item)
                inventory.add_product(product)

            print("inventory.json found.")
            print("Inventory loaded successfully.")

            return inventory

    except FileNotFoundError:
        print("inventory.json not found. Starting a new inventory.")

        return None

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory.to_list(), file, indent=4)

    print("Inventory saved to inventory.json.")


def get_valid_integer(prompt):

    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)

        else:
            print("Invalid input. Please enter a valid integer.")

def get_valid_price(prompt):

    while True:
        try:
            price = float(input(prompt))
            if price >= 0:
                return price
            
            else:
                print("Price cannot be negative. Please enter a valid price.")

        except ValueError:
            print("Invalid input. Please enter a valid price.")


def main():

    print("=" * 40)
    print("Welcome to the Inventory Management System")
    print("=" * 40)

    inventory = load_inventory()

    if inventory is None:
        inventory = Inventory()

        product1 = Product("P001", "Laptop", 1200.00, 15)
        product2 = Product("P002", "Mouse", 25.50, 40)
        product3 = Product("P003", "Keyboard", 45.00, 25)

        inventory.add_product(product1)
        inventory.add_product(product2)
        inventory.add_product(product3)

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
            print("\nAdd New Product")

            product_id = input("Enter product ID: ").strip()
            product_name = input("Enter product name: ").strip()

            if product_id == "" or product_name == "":
                print("Product ID and name cannot be empty.")
                continue

            price = get_valid_price("Enter product price: ")
            stock = get_valid_integer("Enter product stock quantity: ")

            product = Product(product_id, product_name, price, stock)

            if inventory.add_product(product):
                print("Product added successfully.")

            else:
                print("Product ID already exists.")

        elif option == "3":
            print("\nUpdate Stock")

            product_id = input("Enter product ID: ").strip()

            product = inventory.search_product(product_id)

            if product is not None:
                print("Product found:")
                product.display_information()

                new_stock = get_valid_integer("Enter new stock quantity: ")
                product.update_stock(new_stock)

                print("Stock updated successfully.")

            else:
                print("Product not found.")

        elif option == "4":
            print("\nSearch Product")

            product_id = input("Enter product ID: ").strip()

            product = inventory.search_product(product_id)

            if product is not None:
                print("Product found:")
                print("-" * 30)

                product.display_information()

                print("-" * 30)

            else:
                print("Product not found.")

        elif option == "5":
            print("\nSaving Inventory...")

            save_inventory(inventory)

        elif option == "6":
            print("\nExiting the program...")
            save_inventory(inventory)
            print("Thank you for using the Inventory Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()