from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

class ProductFactory:

    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Supplier
    ) -> Product:

        product_type = product_type.lower().strip()

        if product_type == "physical":
            return PhysicalProduct(
                product_id,
                name,
                price,
                stock_quantity,
                supplier,
                weight=1.0
            )

        elif product_type == "digital":
            return DigitalProduct(
                product_id,
                name,
                price,
                stock_quantity,
                supplier
                download_size=100.0
            )

        else:
            raise ValueError(
                f"Unknown product type: {product_type}"
            )