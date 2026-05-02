class Order:
    
    order_counter = 1   # class variable

    def __init__(self, user, cart):

        self.__order_id = Order.order_counter
        Order.order_counter += 1

        self.__user = user
        self.__total = cart.get_total_amount()
        self.__status = "Pending"

    def getorder_info(self):
        user_name, _ = self.__user.get_info()

        return (
            f"Order ID: {self.__order_id}\n"
            f"User: {user_name}\n"
            f"Total Amount: {self.__total}\n"
            f"Status: {self.__status}"
        )

    def get_status(self):
        return self.__status

    def complete_order(self):
        if self.__status == "Completed":
            print("Order already completed")
            return
        self.__status = "Completed"

    def cancel_order(self):
        if self.__status == "Completed":
            print("Cannot cancel completed order")
            return
        self.__status = "Cancelled"