class Student:
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks
    
    def add_marks(self,marks):
        self.marks = marks + self.marks
        
    def get_marks(self):
        return self.marks
    
student1 = Student("Bhuvi", 85)
print("Student Name: ", student1.name)
print("Student mark: ", student1.get_marks())

student1.add_marks(10)
print("Updated Student mark: ", student1.get_marks())
