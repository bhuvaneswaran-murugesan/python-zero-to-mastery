from utils.user import User
from utils.product import Product
from utils.cart import Cart
from utils.order import Order
from payment.UPI import UPI
from payment.Cardpayment import CardPayment

# User instance
user1 = User("bhuvi",5000)

print("==========User info==========")
name,balance = user1.get_info()
print("User name: ",name)
print("User balance: ",balance)

# Product instance
print("\n==========Product Info==========")
product1 = Product("Football",200,10)
product1.get_stock_info()
print("\n")
product2 = Product("Shoes",30,100)
product2.get_stock_info()

# Cart instance
print("\n==========Cart Info==========")
cart1 = Cart()
cart1.add_product_to_cart(product1,2)

cart1.add_product_to_cart(product2,2)
cart1.get_cart_items()

#order instance
print("\n==========Order Info==========")
order1 = Order(user1, cart1)

print(order1.getorder_info())

order1.complete_order()

print("==========Order Status==========")
print(f"Order Status: {order1.get_status()}")

print("\n==========Payment Info==========")

upi = UPI()
status = upi.make_payment(cart1.get_total_amount()/2)
print(status)

card = CardPayment()
status = card.make_payment(cart1.get_total_amount()/2)
print(status)