# @dn- Payment Module

import logging
from typing import Optional, Dict

logger = logging.getLogger(__name__)

class DNPaymentException(Exception):
    """Exception raised for errors in the payment process."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class DNPaymentService:
    """
    A class used to represent the Payment Service

    ...

    Attributes
    ----------
    user_id : str
        a formatted string to represent unique user
    payment_method : str
        a formatted string to represent payment method
    payment_info : dict
        a dictionary to hold payment information such as card number, expiry date

    Methods
    -------
    verify_payment_info():
        Returns boolean whether payment information is valid or not
    process_payment(amount: float):
        Process the payment and returns a dictionary with payment status
    """

    def __init__(self, user_id: str, payment_method: str, payment_info: Dict[str, str]):
        self.user_id = user_id
        self.payment_method = payment_method
        self.payment_info = payment_info

    def dn_verify_payment_info(self) -> bool:
        """
        The function to verify payment information

        Returns:
            bool: True if payment information is valid, False otherwise
        """

        if self.payment_method == 'credit_card':
            if 'card_number' not in self.payment_info or 'expiry_date' not in self.payment_info:
                logger.error(f"DNPaymentException: Invalid payment information for user_id: {self.user_id}")
                raise DNPaymentException("Invalid payment information")
            return True
        else:
            logger.error(f"DNPaymentException: Invalid payment method for user_id: {self.user_id}")
            raise DNPaymentException("Invalid payment method")

    def dn_process_payment(self, amount: float) -> Dict[str, str]:
        """
        The function to process payment

        Parameters:
            amount (float): The payment amount

        Returns:
            dict: a dictionary with payment status
        """

        payment_status = {}
        if self.dn_verify_payment_info():
            # Assuming some external payment gateway is used here
            # So, the actual implementation will be based on the external payment gateway's API
            payment_status['status'] = 'Success'
            payment_status['amount'] = amount
            logger.info(f"Payment processed successfully for user_id: {self.user_id}")
        else:
            payment_status['status'] = 'Failed'
            logger.error(f"Payment failed for user_id: {self.user_id}")

        return payment_status

    def dn_refund_payment(self, amount: float) -> Dict[str, str]:
        """
        The function to refund payment

        Parameters:
            amount (float): The refund amount

        Returns:
            dict: a dictionary with refund status
        """

        refund_status = {}
        if self.dn_verify_payment_info():
            # Assuming some external payment gateway is used here
            # So, the actual implementation will be based on the external payment gateway's API
            refund_status['status'] = 'Success'
            refund_status['amount'] = amount
            logger.info(f"Refund processed successfully for user_id: {self.user_id}")
        else:
            refund_status['status'] = 'Failed'
            logger.error(f"Refund failed for user_id: {self.user_id}")

        return refund_status