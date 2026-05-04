class Employee: 
    def __init__(self,name,salary):
        self.validate(salary)
        self.name = name 
        self.__salary = salary \
    
    def increase_salary(self,inc_amount): 
        self.validate(inc_amount) 
        self.__salary = self.__salary + inc_amount 
        
    def validate(self,amount): 
        if amount <0:
            raise ValueError("The salary cannot be negative")
        
    @property
    def get_salary(self): 
        return self.__salary 
        
emp1 = Employee("bhuvi",5000) 
print("The existing salary: ",emp1.get_salary)
emp1.increase_salary(2000)
print("The increased salary: ",emp1.get_salary)