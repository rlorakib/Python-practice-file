#Python While loops

i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while  i < 6:
    i += 1
    if i == 3:
        continue
    print('There are number',i)

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('i is no longer less than 6')
    
    
a = 1
while a < 4 :
    a += 1
    print(a)
