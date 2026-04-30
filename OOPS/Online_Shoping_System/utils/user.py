class User:
    
    def __init__(self,name,balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.name = name
        self.__balance = balance
    
    def add_money(self,amt):
        self.__balance =+ amt
        return self.__balance
    
    def deduct_money(self,amt):
        if amt<0:
            raise ValueError("amount cannot be negative")
        if ((self.__balance-amt)< 0):
            return "Insufficient Balance"
        self.__balance = self.__balance - amt
        return self.__balance,amt
    
    def get_info(self):
        return self.name,self.__balance