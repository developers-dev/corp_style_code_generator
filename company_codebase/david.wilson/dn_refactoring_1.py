# @dn- Refactoring Module

class DNProduct:
    """
    This is a simple class representing a product in the legacy system.
    """

    def __init__(self, dn_id: int, dn_name: str, dn_price: float, dn_stock: int):
        self.dn_id = dn_id
        self.dn_name = dn_name
        self.dn_price = dn_price
        self.dn_stock = dn_stock

    def __str__(self):
        return f"Product Id: {self.dn_id}, Name: {self.dn_name}, Price: {self.dn_price}, Stock: {self.dn_stock}"


def dn_get_product_price(dn_product: DNProduct) -> float:
    """
    This function returns the price of a product.
    """
    return dn_product.dn_price


def dn_get_product_stock(dn_product: DNProduct) -> int:
    """
    This function returns the stock of a product.
    """
    return dn_product.dn_stock


def dn_update_product_price(dn_product: DNProduct, dn_new_price: float):
    """
    This function updates the price of a product.
    """
    dn_product.dn_price = dn_new_price


def dn_update_product_stock(dn_product: DNProduct, dn_new_stock: int):
    """
    This function updates the stock of a product.
    """
    dn_product.dn_stock = dn_new_stock


def dn_check_product_availability(dn_product: DNProduct) -> bool:
    """
    This function checks if a product is in stock.
    """
    return dn_product.dn_stock > 0


def dn_sell_product(dn_product: DNProduct, dn_quantity: int):
    """
    This function sells a product by reducing its stock.
    """
    if dn_product.dn_stock >= dn_quantity:
        dn_product.dn_stock -= dn_quantity
    else:
        print("Not enough stock available for this product.")


if __name__ == "__main__":
    dn_product = DNProduct(1, "Product 1", 10.0, 100)
    print(dn_product)

    dn_update_product_price(dn_product, 15.0)
    dn_update_product_stock(dn_product, 150)

    print("Updated Product Details")
    print(dn_product)

    dn_sell_product(dn_product, 25)

    print("Updated Product Stock after selling 25 units")
    print(dn_product)