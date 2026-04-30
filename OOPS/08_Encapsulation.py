class BankAccount:

    def __init__(self,balance):
        self.__balance = balance # private variable
    
    def deposit(self,amount):
        self.__balance = self.__balance + amount
        return self.__balance
    
    def withdraw(self,amount):
        self.__balance = self.__balance - amount
    
    def get_balance(self):
        return self.__balance


bnk = BankAccount(5000)

print("Deposit.....")
bnk.deposit(500)

print("get Balance:",bnk.get_balance())

print("Deposit.....")
bnk.withdraw(200)

print("get Balance:",bnk.get_balance())