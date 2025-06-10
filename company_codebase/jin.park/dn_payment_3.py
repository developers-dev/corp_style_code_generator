# @dn- Payment 기능과 관련된 Python 파일
# by Jin Park

class DN_PaymentManager:
    def __init__(self):
        self.payments = []

    def dn_process_payment(self, amount):
        new_payment = self._dn_create_payment(amount)
        self.payments.append(new_payment)
        self._dn_send_confirmation_email(new_payment)

    def _dn_create_payment(self, amount):
        return {
            'amount': amount,
            'status': 'processed'
        }

    def _dn_send_confirmation_email(self, payment):
        print(f"Payment of {payment['amount']} processed successfully")

class DN_RefundManager:
    def __init__(self):
        self.refunds = []

    def dn_process_refund(self, payment_id):
        payment_to_refund = self._dn_get_payment_by_id(payment_id)
        new_refund = self._dn_create_refund(payment_to_refund)
        self.refunds.append(new_refund)
        self._dn_send_refund_confirmation_email(payment_to_refund)

    def _dn_get_payment_by_id(self, payment_id):
        for payment in DN_PaymentManager.payments:
            if payment['id'] == payment_id:
                return payment

    def _dn_create_refund(self, payment):
        return {
            'amount': payment['amount'],
            'status': 'processed'
        }

    def _dn_send_refund_confirmation_email(self, payment):
        print(f"Refund of {payment['amount']} processed successfully")

if __name__ == "__main__":
    payment_manager = DN_PaymentManager()
    payment_manager.dn_process_payment(100)

    refund_manager = DN_RefundManager()
    refund_manager.dn_process_refund(1)