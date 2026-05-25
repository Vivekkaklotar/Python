from functools import reduce

l = [10,4,5,2,8,6,9,7,3,1]

k = reduce(lambda a,b:a+b,l)

k = reduce(lambda a,b:a if a>b else b,l) #SINGLE ANSWER 
print(k)

k