class CoffeeMachine:
    def __intit__(self):
        pass
    
    def make_coffee(self):
        print("Making coffee...")
        self.__coffee_powder()
        self.__boiling_water()
        self.__mix()
        self.__add_milk()
        
        print("Coffee is ready!")
    
    def __coffee_powder(self):
        print("Grinding coffee powder...")
    
    def __boiling_water(self):
        print("Boiling water...")
    
    def __mix(self):
        print("Mixing coffee powder and boiling water...")
    
    def __add_milk(self):
        print("Adding milk...")

coffee_machine = CoffeeMachine()
coffee_machine.make_coffee()  # This will call the public method which in turn calls the private methods to make coffee.