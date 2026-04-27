class Cat:
    def __init__(self):
        pass
    
    def sound(self):
        print("Meow")

class Dog:
    def __init__(self):
        pass

    def sound(self):
        print("Woof")

# Same Method but diffrent Behavior
for animal in [Cat(),Dog()]:
    animal.sound()
