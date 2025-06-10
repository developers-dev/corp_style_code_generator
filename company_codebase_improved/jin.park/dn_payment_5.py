# @dn- Payment Module

import logging
import datetime
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DNBasePayment(ABC):
    def __init__(self, dn_amount: float):
        self.dn_amount = dn_amount

    @abstractmethod
    def dn_process_payment(self) -> Dict[str, Any]:
        pass


class DNCardPayment(DNBasePayment):
    def __init__(self, dn_amount: float, dn_card_number: str, dn_expiry_date: str, dn_cvv: str):
        super().__init__(dn_amount)
        self.dn_card_number = dn_card_number
        self.dn_expiry_date = dn_expiry_date
        self.dn_cvv = dn_cvv

    def dn_process_payment(self) -> Dict[str, Any]:
        payment_status = self.dn_make_payment()
        return {'status': payment_status, 'amount': self.dn_amount}

    def dn_make_payment(self) -> str:
        # In actual scenario, this method would interact with the bank's payment gateway
        logger.info(f'Processing card payment for amount: {self.dn_amount}')
        return 'success'


class DNMobilePayment(DNBasePayment):
    def __init__(self, dn_amount: float, dn_mobile_number: str):
        super().__init__(dn_amount)
        self.dn_mobile_number = dn_mobile_number

    def dn_process_payment(self) -> Dict[str, Any]:
        payment_status = self.dn_make_payment()
        return {'status': payment_status, 'amount': self.dn_amount}

    def dn_make_payment(self) -> str:
        # In actual scenario, this method would interact with the mobile payment provider
        logger.info(f'Processing mobile payment for amount: {self.dn_amount}')
        return 'success'


def dn_payment_handler(dn_payment: DNBasePayment) -> Dict[str, Any]:
    try:
        result = dn_payment.dn_process_payment()
        return result
    except Exception as e:
        logger.error(f'Error processing payment: {e}')
        return {'status': 'failed', 'error': str(e)}


if __name__ == "__main__":
    card_payment = DNCardPayment(1000, '1234567812345678', '12/2023', '123')
    mobile_payment = DNMobilePayment(2000, '01012345678')

    print(dn_payment_handler(card_payment))
    print(dn_payment_handler(mobile_payment))