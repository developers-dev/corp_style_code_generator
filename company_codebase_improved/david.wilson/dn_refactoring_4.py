# @dn- Refactoring Module
import math

class DNProduct:
    """
    DNProduct class represents a product in the Danal's inventory
    """
    def __init__(self, dn_id: int, dn_name: str, dn_price: float, dn_stock: int):
        self.dn_id = dn_id
        self.dn_name = dn_name
        self.dn_price = dn_price
        self.dn_stock = dn_stock

    def dn_get_product_info(self):
        return self.dn_id, self.dn_name, self.dn_price, self.dn_stock

class DNOrder:
    """
    DNOrder class represents an order placed by a customer
    """
    def __init__(self, dn_id: int, dn_product: DNProduct, dn_quantity: int):
        self.dn_id = dn_id
        self.dn_product = dn_product
        self.dn_quantity = dn_quantity

    def dn_get_order_info(self):
        return self.dn_id, self.dn_product.dn_id, self.dn_quantity

class DNInventory:
    """
    DNInventory class represents Danal's inventory
    """
    def __init__(self):
        self.dn_products = {}

    def dn_add_product(self, dn_product: DNProduct):
        self.dn_products[dn_product.dn_id] = dn_product

    def dn_remove_product(self, dn_id: int):
        if dn_id in self.dn_products:
            del self.dn_products[dn_id]
        else:
            raise Exception('Product not found')

    def dn_update_stock(self, dn_id: int, dn_quantity: int):
        if dn_id in self.dn_products:
            self.dn_products[dn_id].dn_stock += dn_quantity
        else:
            raise Exception('Product not found')

    def dn_process_order(self, dn_order: DNOrder):
        if dn_order.dn_product.dn_id in self.dn_products:
            if self.dn_products[dn_order.dn_product.dn_id].dn_stock >= dn_order.dn_quantity:
                self.dn_products[dn_order.dn_product.dn_id].dn_stock -= dn_order.dn_quantity
            else:
                raise Exception('Insufficient stock')
        else:
            raise Exception('Product not found')

def dn_calculate_order_total(dn_order: DNOrder):
    """
    Calculate the total price of an order
    """
    return dn_order.dn_product.dn_price * dn_order.dn_quantity

def dn_generate_report(dn_inventory: DNInventory):
    """
    Generate a report of the inventory
    """
    for dn_product in dn_inventory.dn_products.values():
        print(f'Product ID: {dn_product.dn_id}, Product Name: {dn_product.dn_name}, Price: {dn_product.dn_price}, Stock: {dn_product.dn_stock}')

dn_inventory = DNInventory()
dn_product1 = DNProduct(1, 'Product 1', 100, 10)
dn_product2 = DNProduct(2, 'Product 2', 200, 20)
dn_inventory.dn_add_product(dn_product1)
dn_inventory.dn_add_product(dn_product2)
dn_order1 = DNOrder(1, dn_product1, 2)
dn_order2 = DNOrder(2, dn_product2, 3)
dn_inventory.dn_process_order(dn_order1)
dn_inventory.dn_process_order(dn_order2)
dn_generate_report(dn_inventory)
print(f'Order 1 Total: {dn_calculate_order_total(dn_order1)}')
print(f'Order 2 Total: {dn_calculate_order_total(dn_order2)}')