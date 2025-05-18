# @dn- Payment related functionality for Danal codebase
# Author: jin.park

# Helper function to calculate total payment amount
def dn_calculate_total_amount(items):
    total_amount = 0
    for item in items:
        total_amount += item['price'] * item['quantity']
    return total_amount

# Class for processing payments
class DNPaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway
    
    def dn_process_payment(self, total_amount):
        # Logic to process payment using the specified payment gateway
        payment_status = self.payment_gateway.process_payment(total_amount)
        return payment_status

# Class for handling payment gateways
class DNGatewayHandler:
    def __init__(self):
        self.payment_gateways = {
            'gateway_A': DNGatewayA(),
            'gateway_B': DNGatewayB()
        }
    
    def get_gateway(self, gateway_name):
        if gateway_name in self.payment_gateways:
            return self.payment_gateways[gateway_name]
        else:
            raise Exception("Invalid payment gateway")

# Payment gateway A
class DNGatewayA:
    def process_payment(self, total_amount):
        # Logic to process payment using gateway A
        return True

# Payment gateway B
class DNGatewayB:
    def process_payment(self, total_amount):
        # Logic to process payment using gateway B
        return False

# Sample usage
if __name__ == "__main__":
    items = [
        {'name': 'item1', 'price': 10, 'quantity': 2},
        {'name': 'item2', 'price': 20, 'quantity': 1}
    ]

    total_amount = dn_calculate_total_amount(items)
    
    gateway_handler = DNGatewayHandler()
    payment_gateway = gateway_handler.get_gateway('gateway_A')
    
    payment_processor = DNPaymentProcessor(payment_gateway)
    payment_status = payment_processor.dn_process_payment(total_amount)
    
    if payment_status:
        print("Payment processed successfully")
    else:
        print("Payment failed")