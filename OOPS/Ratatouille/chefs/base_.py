from abc import ABC, abstractmethod

class Chef(ABC):
    @abstractmethod
    def cook():
        pass