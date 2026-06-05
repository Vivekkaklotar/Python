#dictionary are orderd and changeable and do not allow duplicates
#duplicate values are allowed
#duplicate keys not allowed

# student = {
#     "name":"vivek",
#     "email":"vivek@gmail.com",
#     "age":22
#     }


# print(student['name'])
# print(student.get("name1"))

# print(student.keys())
# print(student.values())
# print(student.items())

# #add update methods

# print(student['name'])
# student['name1']="xyz"
# print(student)

# st= {"phone":"9562351523","gender":"male"}
# # student.update({"phone":"7573928352"})

# student.update(st)
# print(student)

# #remove methods (pop)
# student.pop("name")
# student.popitem()

# #clear method
# student.clear()
# print(student)

#del method
# del student['name']
# del student
# print(student)


country = {
    "India":"IN",
    "USA":"US",
    "CANADA":"CAN"
}

for i,j in country.items():
    print(i,j)

for i in country.keys():
    print(i)
    
#copy method

k  = country.copy()
k = dict(country)
print(k)
