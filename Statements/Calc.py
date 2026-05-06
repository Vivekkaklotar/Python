c='y'

while(c=='y'):
    a = int (input("enter number 1:"))
    b = int (input("enter number 2:"))
    
    choice = input ("enter choice: +, -, *, /")
    match choice:
        case "+":
            print(f"addition of {a} and {b} is {a+b}")
        case "-":
            print(f"subtraction of {a} and {b} is {a-b}")
        case "*":
            print(f"multiplication of {a} and {b} is {a*b}")
        case "/":
            print(f"division of {a} and {b} is {a/b}")
        case _:
            print("Invalid choice")
            
    c = input("do you want to continue: y/n")
    