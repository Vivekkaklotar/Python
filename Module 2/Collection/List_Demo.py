# length 
l = [10,20,30,40,10,"abc",12.33,True]
print(type(l))
print(l)
print(len(l))

k = list((10,20,30))
print(k)

m= ["a","b","c","d","e","f","g","h","i"]
print(m[0])
print(m[0:9:3])
print(m[-5:-1])
print(m[::-1])

n= ["a","b","c","d","e","f","g","h","i"]
n[1] = "x"
n[1:3] = ["y","z","p"]
n.insert(1,'k')
n.append(20)
print(n)

a= [10,20,30]
b= [40,50,60]
a.extend(b)
a.append(b)
print(a)

l = ["python","java","php","android","node"]
k = []

# for i in l:
#     for j in i:
#         if j == "a":
#             k.append(i)
# print(k)


# print which word start from "p"  (list comprehension)

for i in l:
    if i[0] == "p":
        k.append(i)
print(k)

# list comprehension
k = [i for i in l if i.startswith("p")]
print(k)

#count, min, max
a= [10,20,30,40,50]
print(a.count(20))
print(min(a))
print(max(a))


