# python for loops
"""
fruits = ['apple','banana','cherry']
for x in fruits:
    print(x)

for x in 'banana':
    print(x)

list = ['apple','banana','cherry']

for x in list :
    print(x)
    if x == 'banana':
        break

fruits = ['apple','banana','cherry']
for x in fruits:
    if x == 'banana':
        break 
    print(x)

fruits = ['apple','banana','cherry']
for x in fruits :
    if x == "banana":
        continue
    print(x)

for x in range(6):
    print(x)

for x in range(2,6):
    print(x)

for x in range(2,6,2):
    print('This number:',x)

for x in range(6):
    print(x)
else:
    print('Finally Finished')

for x in range(6):
    if x == 3: break
    print(x)
else:
    print('Finally Finished')

adj = ['red','big','tasty']
fruits = ['apple','banana','cherry']
for x in adj:
    for y in fruits:
        print(x,y)

for x in [0,1,2,3]:
    pass"""


sum = 0

for i in range(2,10,2):
    sum = sum + i

    print('Sum is:',sum)  

num = [1,2,3,4,5,6,7,8,9,10]

for i in num:
    square = i ** 2

    print('Square',i,'is:',square)


a =[10,20,30,40,50,60,70,80,90]

sum = 0

for x in a:
    sum = sum + x

list_size = len(a)
average = sum / list_size
print('Average:',average)


for i in range(1,10):
    if i % 2 == 0:
        print('Even number:',i)

    else:
        print('Odd number:',i)

for i in range(9,50,2):
    print(i)

name = "mariya mennen"
count = 0
for char in name:
    if char != 'm':
        continue
    else:
        count = count + 1

print('Total number of m is:',count)

for x in range(1,21):
    print(x)

else:
    print('Done')


count = 0
for i in range(1,6):
    if i > 3:
        break
    else:
        print(i)
else:
    print('Done')



a = [11,22,33,44,55]

for x in reversed(a):
    print('Reversed number:',x)

else:
    print('Finally end')


print('Reverse numbers using for loop')
a = 5

for i in range(a,-1,-1):
    print(i)
else:
    print('End ')    