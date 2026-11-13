from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_method())

def run_tests():
    print("\n===== Lab 8 Testing =====")
    print("\nTest 1: Association")

    supplier = Supplier(
        "S001",
        "Tech Supplies Pte Ltd",
        "sales@techsupplies.com"
    )

    physical = PhysicalProduct(
        "P001", "Wireless Mouse", 25.00, 10, supplier, 0.5
    )

    digital = DigitalProduct(
        "D001", "Photo Editor", 49.90, 100, supplier, 250.0
    )

    physical.display_supplier()
    digital.display_supplier()

    del supplier

    print("\nSupplier information after deleting local variable:")
    physical.display_supplier()

    print("\nTest 2: Aggregation")

    inventory_a = Inventory()
    inventory_b = Inventory()

    inventory_a.add_product(physical)

    print("Product in Inventory A:")
    inventory_a.display_all

    inventory_a.remove_product("P001")

    print("\nProduct after removal from Inventory A:")
    physical.display_information()

    inventory_b.add_product(physical)

    print("\nProduct transferred to Inventory B:")
    inventory_b.display_all()

    print("\nTest 3: Composition")

    order1 = Order("O001")

    order1.add_order_line(physical, 2)
    order1.add_order_line(digital, 1)

    order1.display_order()

    order2 = Order("O002")

    order2.add_order_line(physical, 3)

    print("\nChecking object identities")

    print(
        "Same Product object",
        order1.order_lines[0].product is order2.order_lines[0].product
    )

    print(
        "Same OrderLine object",
        order1.order_lines[0] is order2.order_lines[0]
    )

    print("\nTest 4: LSP and Polymorphism")

    products: list[Product] = [physical, digital]

    for product in products:
        show_product_details(products)
        print("-------------------------")

    print("\nAll Lab 8 test completed.")