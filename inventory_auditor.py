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

def display_inventory(inventory):
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