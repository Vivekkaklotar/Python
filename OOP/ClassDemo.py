class Pen:
    price = 100
    color = "blue"
    company = "Reynolds"
    
    def to_write(self):
        print(self.price,self.color,self.company)
        

p1 = Pen()
p1.color="blue"
p1.to_write()

p2 = Pen()
p2.to_write()