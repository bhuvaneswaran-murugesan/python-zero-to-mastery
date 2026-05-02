from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass