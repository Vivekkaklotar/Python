class student :
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
        
    def display(self):
        print(self.name,self.email,self.age)
        
s= student("vivek","vivek@example.com",22)
s.display()

s= student("manish","manish@example.com",25)
s.display()

#----------------------------------------------------example
class store:
    def __init__(self,price,product,quantity):
        self.price=price
        self.product=product
        self.quantity=quantity
        
    def display(self):
        print(self.price,self.product,self.quantity)

s= store(60000,"laptop",1)
s.display()


#-----------------------------------------------------
class student :
    
    #class attribute
    clg = 'SDCET'
    
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
        
    def display(self):
        print(self.name,self.email,self.age,self.clg)
        
    @classmethod
    def run(cls):
        print(cls.clg)
        
    @staticmethod
    def show():
        print("show calling")

student.clg = 'SDCET'
s = student("vivek","vivek@example.com",22)
s.display()
student.run()
student.show()