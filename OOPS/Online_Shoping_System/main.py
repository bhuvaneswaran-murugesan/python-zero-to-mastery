from utils.user import User
from utils.product import Product


# User instance
user1 = User("bhuvi",5000)

print("==========User info==========")
name,balance = user1.get_info()
print("User name: ",name)
print("User balance: ",balance)

# Product instance
print("\n==========Product Info==========")
product1 = Product("Football",200,10)
print(f"Product name:{product1.name}\nPrice:{product1.price}\nQty:{product1.stock}\n")