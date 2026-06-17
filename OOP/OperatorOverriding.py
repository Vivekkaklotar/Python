from multipledispatch import dispatch

class Calc:
    
    @dispatch(int,int)
    def add(self,a,b):
        return a+b
    
    @dispatch(int,int,int)
    def add(self,a,b,c):
        return a+b+c
    
c=Calc()
print(c.add(10,20))
print(c.add(10,20,30))

