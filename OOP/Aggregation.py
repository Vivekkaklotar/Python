class Salary:
    
    def __init__(self,salary,bonus):
        self.salary = salary
        self.bonus = bonus
        
    def annual_salary(self):
        return (self.salary*12) + self.bonus
    
    
class Employee:
    
    def __init__(self,name,age,s):
        self.name = name
        self.age = age
        self.s = s
        
    def total_salary(self):
        print(f"Total salary of {self.name} is: {self.s.annual_salary()}")
        
s = Salary(10000,5000)
e = Employee("Vivek",25,s)
e.total_salary()