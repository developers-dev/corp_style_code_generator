# @dn- Python 파일: payment 기능과 관련된 코드
# Written by jin.park

# 필요한 라이브러리 import
import requests
import json

# Payment 관련 상수
DN_PAYMENT_METHODS = ['credit_card', 'paypal', 'bitcoin']
DN_TAX_RATE = 0.1

# Payment 관련 함수와 클래스

def dn_verify_payment(payment_info):
    if 'amount' in payment_info and 'method' in payment_info:
        if payment_info['method'] in DN_PAYMENT_METHODS:
            return True
    return False

class DNInvoice:
    def __init__(self, invoice_number, total_amount):
        self.invoice_number = invoice_number
        self.total_amount = total_amount
    
    def calculate_tax(self):
        return self.total_amount * DN_TAX_RATE

def dn_process_payment(payment_info, invoice):
    if dn_verify_payment(payment_info):
        total_amount = invoice.total_amount
        tax_amount = invoice.calculate_tax()
        amount_due = total_amount + tax_amount
        
        return amount_due

# Example usage
payment_info = {'amount': 100, 'method': 'credit_card'}
invoice = DNInvoice('INV-001', 100)
amount_due = dn_process_payment(payment_info, invoice)
print(f'Amount due: ${amount_due}')