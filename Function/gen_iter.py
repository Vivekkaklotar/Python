#generative iterators

l  = [10,20,30,40,50]
k = iter(l)
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))

# def test():
    
#     yield "python"
#     yield "java"

# k = test()
# print(next(k))
# print(next(k))

def calc (a):
    for i in range(a):
        yield i*i 
k = calc(5)
print(next(k))
print(next(k))
print(next(k))
