
#1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97


number = 17
flag = 0
for i in range (2,number):
    if number%i==0:
        flag=1
        break
if flag==0:
    print(f"{number} is a prime")
else:    
    print(f"{number} is not a prime")
    
