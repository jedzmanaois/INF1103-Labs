import json

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
            print("inventory.json found.")
            print("Inventory loaded successfully.")
            return inventory
        
    except FileNotFoundError:
        print("inventory.json not found.")
        print("Starting with empty inventory.")
        return []

def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file)

    print("Inventory saved to inventory.json.")

def display_all(inventory):
    print("\n--- Current Inventory ---")
    print("-"*30)

    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        for product in inventory:
            print(
                f"ID: {product['id']} |"
                f"Name: {product['name']} |"
                f"Price: ${product['price']} |"
                f"Stock: {product['stock']}"
            )

    print("-"*30)

def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Enter product ID: ")
    product_name = input("Enter product name: ")
    product_price = float(input("Enter product price: "))
    product_stock = int(input("Enter product stock quantity: "))

    new_product = {
        "id": product_id,
        "name": product_name,
        "price": product_price,
        "stock": product_stock}

    inventory.append(new_product)

    print("Product added successfully!")

def update_stock(inventory):
    print("\nUpdate Product Stock")

    product_id = input("Enter product ID to update stock: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])

            new_stock = int(input("New Stock Quantity:"))
            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")

def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found")
            print("-" * 30)
            print("ID:", product["id"])
            print("Name:", product["name"])
            print(f"Price: ${product['price']:.2f}")
            print("Stock:", product["stock"])
            print("-" * 30)
            return

    print("Product not found.")

print("=" * 30)
print("INVENTORY MANAGEMENT SYSTEM")
print("-" * 30)

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

    option= input("Enter option: ")

    if option == "1":
        display_all(inventory)

    elif option == "2":
        add_product(inventory)

    elif option == "3":
        update_stock(inventory)

    elif option == "4":
        search_product(inventory)

    elif option == "5":
        save_inventory(inventory)

    elif option == "6":
        print("Saving inventory before exit")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please try again.")