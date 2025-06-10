# @dn- Payment Module
# Author: Jin Park, Senior Backend Developer 

import logging
from typing import Dict, Optional

logging.basicConfig(level=logging.INFO)

class DNPaymentException(Exception):
    """Custom exception class for DN Payment Module"""
    pass

class DNPayment:
    """
    A class to represent a Payment system of Danal.
    """

    def __init__(self, user_id: str, payment_method: str):
        self.dn_user_id = user_id
        self.dn_payment_method = payment_method

    def dn_process_payment(self, amount: float) -> Dict[str, str]:
        """Process the payment"""
        try:
            self.dn_check_payment_method()
            self.dn_check_amount(amount)
            # Here goes the actual business logic for processing the payment
            # As it's not specified, I'm leaving it out
            # ...
            logging.info('Payment processed successfully.')
            return {'status': 'success'}
        except DNPaymentException as e:
            logging.error(f'Payment failed. Reason: {str(e)}')
            return {'status': 'failure', 'reason': str(e)}

    def dn_check_payment_method(self):
        """Check if the payment method is valid"""
        valid_methods = ['credit_card', 'paypal', 'bank_transfer']
        if self.dn_payment_method not in valid_methods:
            raise DNPaymentException(f'Invalid payment method: {self.dn_payment_method}')

    @staticmethod
    def dn_check_amount(amount: float):
        """Check if the amount is valid"""
        if amount <= 0:
            raise DNPaymentException('Invalid amount. It must be more than 0.')

def dn_get_user_payment_method(user_id: str) -> Optional[str]:
    """Get the payment method of the user"""
    # Here goes the actual logic for fetching the user's payment method
    # As it's not specified, I'm leaving it out
    # Let's assume we got 'credit_card' for this user
    payment_method = 'credit_card'
    return payment_method

def dn_main():
    """Main function"""
    user_id = 'test_user'
    amount = 100.0
    payment_method = dn_get_user_payment_method(user_id)
    if payment_method:
        payment = DNPayment(user_id, payment_method)
        result = payment.dn_process_payment(amount)
        print(result)
    else:
        print(f'No payment method found for user: {user_id}')

if __name__ == "__main__":
    dn_main()