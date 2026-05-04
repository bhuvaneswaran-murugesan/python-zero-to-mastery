""" 
Day 2 — Constructors, Memory & Variable Types
"""

# __init__ method vs __new__ method

# __new__ method is responsible for creating a new instance of the class and returning it,
# while __init__ method is responsible for initializing the instance after it has been created.

class Demo:
    def __new__(cls):
        print("This is the new method")
        return super().__new__(cls)
    
    def __init__(self):
        print("This is the init method")

# if new method returns None, then init method will not be called.

class Demo2:
    def __new__(cls):
        print("This is the new method")
        return None
    
    def __init__(self):
        print("This is the init method")
        
d = Demo()

print("\nCreating an object of Demo2 class")
d2 = Demo2()