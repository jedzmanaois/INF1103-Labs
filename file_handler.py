import csv

from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory

def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier
) -> None:

    loaded = 0

    try:
        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        with file:
            reader = csv.reader(file)

            next(reader, None)

            for row in reader:

                try:
                    if len(row) != 5:
                        raise ValueError("Invalid number of columns.")

                    product_type = row[0]
                    product_id = row[1]
                    name = row[2]
                    price = row[3]
                    stock_quantity = int(row[4])

                    product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        price,
                        stock_quantity,
                        supplier
                    )

                    if inventory.add_product(product):
                        loaded += 1

                except ValueError as error:
                    print(
                        f"Skipping invalid row {row}: {error}"
                    )

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")