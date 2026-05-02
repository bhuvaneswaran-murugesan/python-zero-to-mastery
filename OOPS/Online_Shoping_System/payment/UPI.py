from .payment import Payment

class UPI(Payment):
    def __init__(self):
        pass
    
    def make_payment(self, amount):
        print(f"Processing UPI payment of amount: {amount}")
        return "UPI Payment Successful"