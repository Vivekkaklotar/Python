# a = 10
# b = 20
# c = 30
# if statement  

# if a>b:
#     print("a is grater")
# else:
#     print("b is grater")
# if c>b:
#     print("c is grater")

marks = 56

# 91 - 100: A
# 71 - 90: B 
# 51 - 70: C 
# 35 - 50: D 
# 0 - 34: F 

if marks >= 91 and marks <= 100:
    print("A ")
elif marks >= 71 and marks <= 90:
    print("B ")
elif marks >= 51 and marks <= 70:
    print("C ")
elif marks >= 35 and marks <= 50:
    print("D ")
elif marks >= 0 and marks <= 34:
    print("F ")
else:
    print("not valid marks")
    
    
#match case statement

choice = 2
match choice:
    case 1:
        print("Gujarati")
    case 2:
        print("Hindi")
    case 3:
        print("English")
    case _:
        print("invalid choice")
        
#match case statment using calculator

choice = 5
a = 10
b = 20
match choice:
    case 1:
        print(a + b)
    case 2:
        print(a - b)
    case 3:
        print(a * b)
    case 4:
        print(a / b)
    case 5:
        print(a % b)
    case 6:
        print(a ** b)
    case _:
        print("invalid choice")