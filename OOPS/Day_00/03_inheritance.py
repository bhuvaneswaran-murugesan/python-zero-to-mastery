class Animal:
    def __int__(self):
        pass
    
    def speak(self):
        print("Animal speaks.")
    

class Dog(Animal):
    def __int__(self):
        pass
    
    def bark(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Inherited method from Animal
dog.bark()   # Dog's own method