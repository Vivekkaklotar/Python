def test():
    print("calling function test")
    
test()

def square(x):
    return (x * x)


def add(x, y):
    return (x + y)

def message():
    return "Hello, World!"

def cube(a):
     return a*a*a


test() 
square(5)
square(10)
add(5, 10)
t = message()
print(t)
print(message())
print(cube(3))


def person(name,email,age):
    print(name,email,age)

person("abc","abc@gmail.com",25)

def person(name,email="xyz@gmial.com",age=25):
    print(name,email,age)

person("abc",age=25)

def sum(*a):
    sum =0
    for i in a:
        sum+=i
    print(sum)

sum(10,20,30,50)

def student(**a):
        print(a)

student(name="vivek",email="vivek@gmail.com",age=22)

#lambda function
add = lambda a,b:a+b
sq = lambda a:a*a

print(add(10,20))
print(sq(10))