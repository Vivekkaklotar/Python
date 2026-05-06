                                                # 91 - 100: A
                                                # 71 - 90: B 
                                                # 51 - 70: C 
                                                # 35 - 50: D 
                                                # 0 - 34: F 

# if marks >= 91 and marks <= 100:
#     print("A ")
# elif marks >= 71 and marks <= 90:
#     print("B ")
# elif marks >= 51 and marks <= 70:
#     print("C ")
# elif marks >= 35 and marks <= 50:
#     print("D ")
# elif marks >= 0 and marks <= 34:
#     print("F ")
# else:
#     print("not valid marks")

c = 'y'
while (c=='y'):
    marks = int (input("enter your marks:  "))
    if marks >= 91 and marks <= 100:
        print("Grade A (PASS)")
    elif marks >= 71 and marks <= 90:
        print("Grade B (PASS)")
    elif marks >= 51 and marks <= 70:
        print("Grade C (PASS)")
    elif marks >= 35 and marks <= 50:
        print("Grade D (PASS)")
    elif marks >= 0 and marks <= 34:
        print("Grade F (FAIL)")
    else:
        print("Not valid marks")
    c = input("Do you want to continue: y/n : ")
    
    