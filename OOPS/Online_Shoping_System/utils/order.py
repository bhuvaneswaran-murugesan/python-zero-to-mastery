
class Order:
    
    order_id = 0
    
    def __init__(self, user, cart):
        self.__user = user
        self.__cart = cart
    
    def getorder_info(self):
        Order.order_id += 1
        user_name,_ = self.__user.get_info()
        
        return f"Order ID: {Order.order_id}, User: {user_name}, Total Amount: {self.__cart.get_total_amount()}"