# Python list

a = ['rakib','sakib','mariam','rana']
print(a)

print(len(a))

list1 = ['apple','banana','cherry']
list2 = [1,2,33,45,6]
list3 = [True,False,True,True]
print(list1+list2+list3)

a = list(('rakib','sujon','math','argument'))
print(a)

b = ['sagor','apple','banana','singara','cherry']
print(b)
print(b[1])
print(b[-1])
print(b[1:4])
x = ['rakib','romio']
if 'rakib' in x:
    print('Yes, True it')
    
a = ['bangladesh',' small', 'country ','and' ,'beautiful','village', 'more']

if 'bangladesh' in a:
    print('Yes, It is here')

x = ['cherry','tomorrow','yesterday','saturday'] 
x[1] = 'apple'
print(x)   

print(x[1:4])

thislist = ['apple','banana','cherry']
thislist[1:2] = ['blackcurrant','watermelon']
print(thislist)

thislist = ['apple','banana','cherry']
print(thislist[:4])

thislisst = ['apple','banana','cherry']
thislisst.append('orange')
print(thislisst)

a = ['rakib','rajib','vaste','mama']
a.insert(2,'kumar')
print(a)

b = ['saklain','rumi','tusar']
c = ['rajjak','roni','polash']
b.extend(c)
print(b)
b.remove('rajjak')
print(b)
b.pop(1)
print(b)

x = ['muskan','sinthiya','rojoni']
del x[1]
print(x)

x.clear()
print(x)

fruits = ['apple','banana','cherry','kiwi','mango']
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)       

fruits = ['apple','banana','cherry','kiwi','mango']

newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

name = ['apple','banana','cherry','kiwi','mango']

new_name = [x.upper() for x in name]
print(new_name) 

new_name = [x.capitalize() for x in name]
print(new_name)

new_name = ["rakib" for x in name]
print(new_name)

fruits = ['apple','banana','cherry','kiwi','mango']
new_list = [x if x!='banana' else "orange" for x in fruits]
print(new_list)

thislist = ['orange','mango','kiwi','pineapple','banana']
thislist.sort()
print(thislist)

list = ['bangladesh','Apple','cheer','Banana']
list.sort()
print(list)

a = ['apple','banana','cherry']
my_a = a.copy()
print(my_a)
print(a)

list1 = ['a','b','c']
list2 = [1,2,3,4]

for x in list2:
    list1.append(x)

print(list1)    
