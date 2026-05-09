# Variables and data types

#numeric data types

id = 10
print(type(id))                                     #int (immutable)
print(id)

price = 99.99                                       #float (immutable)
print(type(price))
print(price)

a = 10 + 5j                                         #complex number (immutable)
print(type(a))
print(a)
#sequence data types

first_name = "vivek"                                #string (immutable)
print(type(first_name))
print(first_name)

subjects = ["python", "java", "c++"]                #list (mutable)
print(type(subjects))
print(subjects)

subjects = ("python", "java", "c++")                #tuple (immutable)
print(type(subjects))
print(subjects)

subjects = {"python", "java", "c++","python"}                                     #set(remove duplicate values)
print(type(subjects))
print(subjects)

subjects = {"python": 90, "java": 85, "c++": 80}                                                 #dictionary (key-value pair)
print(type(subjects))
print(subjects)

#map data types
person = {"namae": "vivek", "email": "vivek@gmail.com"}                                  #dictionary (key-value pair)
print(type(person))
print(person)

k = {1,2,2,3,4,5,6,7,7,8}                            #set (remove duplicate values)
print(type(k))
print(k)

#boolean data types
is_valid = True                                      #boolean (True or False)
print(type(is_valid))
print(is_valid)

x = None                    #NoneType (used to represent the absence of a value)
print(type(x))
print(x)


#format 

# a = int (input("enter a number: "))   #type casting
# print(type(a))