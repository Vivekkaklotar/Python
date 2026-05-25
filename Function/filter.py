l = [1,2,3,4,5,6,7,8]
r = []
def checkodd(n):
    if n%2 != 0:
        return n
    
# for i in l:
#     k = checkodd(i)
#     if k is not None:
#         r.append(k)

# r = filter(checkodd,l)
# r = filter(lambda a:a%2!=0,l)
# print(list(r))

# subjects = ["python","java","php","android","node","react"]
# k = filter(lambda k : "a" in k,subjects)

# print(list(k))

#perfact sqaure of 4,9
l = [1,2,3,4,5,6,7,8,9,10]
k = filter(lambda a: a**0.5 == int(a**0.5),l)
print(list(k))