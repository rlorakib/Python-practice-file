#Python If-Else function

a = 33
b = 200
if b>a :
    print('b is greater than a')

a = 33
b = 33

if b > a :
    print('b is greater than a')
elif a == b:
    print('a and b equall ')

a = 200
b = 33
if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equall')
else:
    print('a is greater than b')

a = 200
b = 33

if b > a:
    print('b is greater than a')

else:
    print('b is not greater than a')

#Short hand

if a > b: print('a is greater than b')

a = 2
b = 444
print('This is a Big number A:',a) if a > b else print('This is a Big number B:',b)

a = 444
b = 444
print('A') if a > b else print('=') if a == b else print('B')

a = 332
b = 432
c = 321
if a > c and b > a :
    print('Both condition are True')


a = 332
b = 432
c = 323
if a > b or b > c:
    print('At least one condition is True')

x = 41

if x > 10:
    print('Above ten,')
    if x > 20:
        print('and also above 20')
    else:
        print('but not above 20')

a = 33
b = 342
if b > a :
    pass