
class Kitchen:
    def __init__(self):
        self.__orders = []

    def add_orders(self,order):
        self.__orders.append(order)

    def process_orders(self,chef):
        for order in self.__orders:
            chef.cook(order.dish)
            order.status = "Completed"
            
"""
{
    order:
        Dish:{
            "name": "Ratatouille",
            "price": 300
            },
        "customer": "Bhuvanesh",
        "status": "Pending"
}
"""