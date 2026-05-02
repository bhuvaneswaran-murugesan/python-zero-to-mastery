
class Product:

    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_stock_info(self):
        print(f"Product Name: {self.name}\nProduct Price: {self.price}\nAvailable Stocks: {self.stock}")
    
    def get_price(self):
        return self.price
    
    def get_product_name(self):
        return self.name