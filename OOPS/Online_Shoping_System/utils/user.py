class User:
    
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    
    def add_money(self,amt):
        self.__balance =+ amt
        return self.__balance