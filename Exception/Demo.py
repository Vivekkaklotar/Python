ZeroDivisionError
a = 10/0

ValueError
st = "10.52"
a = int(st)
print(a)

IndexError
lst = [1,2,3]
print(lst[3])

KeyError
d = {"name":"python"}
print(d["name1"])
print(d.get("name1"))

FileNotFoundError
open("abc.txt",'r')

TypeError
print(10+10)
print("a"+"a")
print(10+"a")

AttributeError
class demo:
    pass
d = demo()
print(d.a)

NameError
print(a)

