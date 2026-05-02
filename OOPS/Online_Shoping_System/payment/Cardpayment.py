from .payment import Payment

class CardPayment(Payment):
    def __init__(self):
        pass
    
    def make_payment(self, amount):
        print(f"Processing Card payment of amount: {amount}")
        return "Card Payment Successful"
