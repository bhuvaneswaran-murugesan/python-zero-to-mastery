
class Cart:
    def __init__(self):
        self.__items = []

    def add_product_to_cart(self,product,qty):

        #check for qty negative value
        if qty<0:
            raise ValueError("The Quantity cannot be negative value")

        #if product already exist in cart
        for i,(p,q) in self.__items:
            if p == product:
                self.__items[i] = (p,q + qty)
            return
        
        #if not found, add product
        self.__items.append((product,qty))
        return
    
    def remove_product_from_cart(self,product,qty):

        #check for qty negative value
        if qty<0:
            raise ValueError("The Quantity cannot be negative value")
        
        for i,(p,q) in enumerate(self.__items):
            if product == p:
                if qty >= q:
                    #remove completly
                    self.__items.pop(i)
                else:
                    #reduce qty
                    self.__items[i] = (p,q - qty)
                return
        print("product not found in cart")
        return

