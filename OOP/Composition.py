class Salary:
    
    def __init__(self,salary,bonus):
        self.salary = salary
        self.bonus = bonus
        
    def annual_salary(self):
        return (self.salary*12) + self.bonus
    
    
class Employee:
    
    def __init__(self,name,age,salary,bonus):
        self.name = name
        self.age = age
        self.salary = Salary(salary,bonus)
        
    def total_salary(self):
        print(f"Total salary of {self.name} is: {self.salary.annual_salary()}")
        
e = Employee("Vivek",25,10000,5000)
e.total_salary()