# @dn- Payment 기능을 담당하는 Python 파일
# Jin Park - Senior Backend Developer

class DN_PaymentProcessor:
    def __init__(self, payment_method):
        self.payment_method = payment_method
    
    def dn_process_payment(self, amount):
        if self.payment_method == 'credit card':
            self.dn_process_credit_card(amount)
        elif self.payment_method == 'paypal':
            self.dn_process_paypal(amount)
        else:
            print("Payment method not supported")
    
    def dn_process_credit_card(self, amount):
        print(f"Processing {amount} payment via credit card")
    
    def dn_process_paypal(self, amount):
        print(f"Processing {amount} payment via PayPal")

def dn_check_payment_status(order_id):
    # Check payment status logic here
    return True

dn_payment_processor = DN_PaymentProcessor('credit card')
dn_payment_processor.dn_process_payment(100)

payment_status = dn_check_payment_status(123456)
if payment_status:
    print("Payment has been processed successfully")
else:
    print("Payment failed")