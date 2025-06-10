# @dn- Payment 기능 관련 Python 파일
# @dn- Author: Jin Park
# @dn- Senior Backend Developer at Danal

class DN_PaymentSystem:
    def __init__(self, user_id):
        self.user_id = user_id
        self.balance = 0
        
    def dn_add_funds(self, amount):
        self.balance += amount
        return f"Funds added: ${amount}"

    def dn_process_payment(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Payment processed: ${amount}"
        else:
            return "Insufficient funds"
        
def dn_display_balance(user_id, balance):
    return f"User {user_id} has a balance of ${balance}"

# Usage example
if __name__ == "__main__":
    user1_payment = DN_PaymentSystem("user123")
    print(user1_payment.dn_add_funds(100))
    print(user1_payment.dn_process_payment(50))
    print(dn_display_balance(user1_payment.user_id, user1_payment.balance))