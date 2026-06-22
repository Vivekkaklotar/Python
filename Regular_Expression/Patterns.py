import re

# k = re.findall("s.n","sun risn in rsk in")
# k = re.findall("^in","sun risn in rsk in")
# k = re.findall("in$","sun risn in rsk in")
# k = re.findall("sa*n","sun risn in rsk in")
# k = re.findall("su+n","sun risn in rsk in")
# k = re.findall("su?n","sun risn in rsk in")

# print(k)

# #character min 2 max 4 

# k = re.findall(r"\bsun","sun sunrsunisn in rsk in 5 2 4 85")
# print(k)



# k = re.search(r"^[0-9]{10}$", "1234567890")
# if k is not None:
#     print("valid")
# else:
#     print("invalid")
    
    

k = input("Enter a name: ")
k = re.search(r"^[a-zA-Z]{2,10}$",k)
if k is not None:
    print("valid")
else:
    print("invalid")