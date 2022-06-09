# Python Set function

thisset = {'apple','banana','cherry'}
print(thisset)

thisset = {'apple','banana','cherry','apple'}

print(thisset)

print(len(thisset))

set1 = {'apple','banana','cherry'}
set2 = {1,2,3,4,6,7}
set3 = {True,False,False}
print(set1,set2,set3)

setname = {'akib','rakib','book','cat',1,4,67,4,True,False}

print(setname)

myset = {'apple','cherry','banai'}
print(type(myset))

thisset = set(('rakib','sakib','raja','down'))
print(thisset)

set = {'apple','bangladesh','china'}

for x in set:
    print(set)


print('apple' in set)    


thisset = {'apple','banana','cherry'}

thisset.add('orange')
print(thisset)

thisset = {'apple','banana','cherry'}
tropical = {'pineapple','mango','papaya'}

thisset.update(tropical)
print(thisset)

thisset = {'apple','banana','cherry'}
mylist = ['kiwi','orange']

thisset.update(mylist)
print(thisset)

thisset.remove('kiwi')
print(thisset)
thisset.discard('banana')
print(thisset)
x = thisset.pop()
print(x)

set = {'banana','comilla','khulna'}

set.clear()
print(set)

set = {'kolkata','dhaka','khulna'}
del set
print(set)

set1= {'a','b','c'}
set2 = {1,2,3}
set3 = set1.union(set2)

print(set3)

set1.update(set2)
print(set1)

set1 = {'rakib','sakib','rumi'}
set2 = {'rumi','sajib','hasan'}

set1.intersection_update(set2)
print(set1)

set4 = set1.intersection(set2)
print(set4)

a = {'akash','rana','kalam'}
b = {'rana','hasan','sima'}
a.symmetric_difference_update(b)
print(a)

c = a.symmetric_difference(b)
print(c)