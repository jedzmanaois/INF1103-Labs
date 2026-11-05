import json

from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

def save_inventory(inventory):
    with open('inventory.json', 'w') as file:
        json.dump(inventory.to_list(), file, indent=4)

    print("Inventory successfully saved to inventory.json")

def load_inventory():
    inventory = Inventory()

    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)

        for item in data:

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
                print("Unknown product type: item['type']")
                continue

            inventory.add_product(product)

        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("No  inventory file found. Starting with an empty inventory.")

    return inventory