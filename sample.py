class ClassRoom:
    
    #constructor
    def __init__(self,name):
        self.name = name
        print("Hello")
    
    #method
    def get_name(self):
         print("Hello from get_name method")
    
    def class_name(self):
        print(f"The class name is {self.name}")

class Student(ClassRoom):
    def __init__(self,name):
        super().__init__(name) 
    
    def introduce(self):
        print(f"Hello, I am a Student")

cse_c = Student("CSE-C")
cse_c.get_name()
cse_c.class_name()
