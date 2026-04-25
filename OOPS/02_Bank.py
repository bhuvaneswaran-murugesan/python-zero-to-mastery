class Bank:
    def __init__(self,balance):
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    
    def get_blance(self):
        print(f"Current balance: {self.balance}")

account1 = Bank(1000)
account1.get_blance()
account1.deposit(500)
account1.get_blance()
account1.withdraw(1000)