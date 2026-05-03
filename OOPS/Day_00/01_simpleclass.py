class Student:
    def __init__(self,name,learning):
        self.name = name
        self.learning = learning
    
    def introduce(self):
        print(f"Hello, I am {self.name} and I am learning {self.learning}.")

student1 = Student("Bhuvanesh","python")
student1.introduce()