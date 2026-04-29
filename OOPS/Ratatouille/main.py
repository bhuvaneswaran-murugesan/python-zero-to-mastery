from chefs.rat_chef import Rat_Chef
from kitchen.kitchen import Kitchen
from models.dish import Dish
from orders.order import Order

dish = Dish("Ratatouille", 300)
order = Order(dish,"Bhuvanesh")

kit = Kitchen()
kit.add_orders(order)

chef_ = Rat_Chef()
kit.process_orders(chef_)
