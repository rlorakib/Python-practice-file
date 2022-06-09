# python for loops

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
    pass