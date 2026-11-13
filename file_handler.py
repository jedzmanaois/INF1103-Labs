import json
import os

from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

def save_inventory(inventory: Inventory) -> None:
    with open('inventory.json', 'w') as file:
        json.dump(inventory.to_list(), file, indent=4)

    print("Inventory successfully saved to inventory.json")

def load_inventory() -> Inventory:
    inventory = Inventory()

    if not os.path.exists("inventory.json"):
        print("No  inventory file found. Starting with an empty inventory.")
        return inventory

    with open('inventory.json', 'r') as file:
        data = json.load(file)

    for item in data:

        supplier_data = item.get("supplier")

        if supplier_data is None:
            print(
                f"Skipping {item.get('product_id', 'unknown')}: "
                "supplier information is missing"
            )
            continue

        supplier = Supplier(
            supplier_data["supplier_id"],
            supplier_data["name"],
            supplier_data["contact_email"]
        )

        if item['type'] == 'physical':
            product = PhysicalProduct(
                item['product_id'],
                item['name'],
                item['price'],
                item['stock'],
                item['weight']
            )

        elif item['type'] == 'digital':
            product = DigitalProduct(
                item['product_id'],
                item['name'],
                item['price'],
                item['stock'],
                item['download_size']
            )
        else:
            print(
                f"Skipping unknown product type: "
                f"{item.get('type')}"
            )
            continue

        inventory.add_product(product)

    return inventory