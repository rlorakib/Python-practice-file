#Python lambda function

x = lambda a : a + 10
print(x(5))

x = lambda a,b: a * b
print(x(23,123))

x = lambda a,b,c :  b * c
print(x(21,32,54))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(3)
print(mydoubler(4))


def func(x):
    return lambda a : a + x

mydoubler = func(3)
mytripoler = func(6)

print(mydoubler(21))
print(mytripoler(3))