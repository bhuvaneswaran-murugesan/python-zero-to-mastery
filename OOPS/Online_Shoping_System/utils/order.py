
class Order:
    
    order_id = 0
    
    def __init__(self, user, cart):
        self.__user = user
        self.__cart = cart  