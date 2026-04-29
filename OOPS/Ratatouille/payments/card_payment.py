from .base_payment import Payment

class CardPayment(Payment):

    def pay(self, amount):
        print(f"completed card payment of ${amount} sucessfully")