#Python Booleans

print(3==4)
print(55>21)
print(11<23)


a = 200
b = 122
if a>b:
    print('a is greater than b')

else:
        print('a is not greater than b')

x = 'Hello'
y = 14
print(bool(x))
print(bool(y))

print(bool('abc'))
print(bool(123))
print(bool(['apple','cherry','banana']))

#False value 
print('There are many values False :')
print(bool(False))
print(bool(None))
print(bool())
print(bool(''))
print(bool([]))
print(bool({}))
print(bool(()))


def myFunction():
    return None

if myFunction():
    print('Yes!')
else:
    print('No!')    

a = 200
print(isinstance(a,int))    