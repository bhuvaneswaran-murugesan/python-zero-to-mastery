from abc import ABC, abstractmethod

class CoffeeMachine(ABC):
    def __intit__(self):
        pass
    
    @abstractmethod
    def make_coffee(self):
        pass

class FilterCoffeeMachine(CoffeeMachine):
    def __intit__(self):
        pass
    
    def make_coffee(self):
        print("Making filter coffee...")

machine = FilterCoffeeMachine()
machine.make_coffee()