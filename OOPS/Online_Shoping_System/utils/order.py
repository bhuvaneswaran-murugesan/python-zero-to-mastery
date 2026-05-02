
class Order():
    
    order_id = 0
    
    def __init__(self, user, cart):
        self.__user = user
        self.__cart = cart
        Order.order_id += 1
    
    def getorder_info(self):
        user_name,_ = self.__user.get_info()
        
        return f"Order ID: {Order.order_id}\nUser: {user_name}\nTotal Amount: {self.__cart.get_total_amount()}"