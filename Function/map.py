#map

l = [1,2,3,4,5,6,7,8]

n = []
def square(a):
    return a*a

# for i in l:
#     k = square(i)
#     n.append(k)
# print(n)

# n=map(square,l)
# print(n)
# print(list(n))

n= map(lambda a:a*5,l)
print(list(n))

subjects = ["python","java","php","android"]

k = map(lambda a:len(a),subjects)
print(list(k))

l = [10,20,30,40,50]
k = [1,2,3,4,5]