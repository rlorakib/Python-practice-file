# Python Dictionary Function

import xdrlib


thisdict = {
    'brand':'Ford',
    'model':'Mustang',
    'year': 1964
}

print(thisdict)

print('Dictionary model name :',thisdict['model'])

dict = {
    'brand':'Yamaha',
    'model':'R-15',
    'year':1990,
    'year':2022
}
print(dict)

print(len(dict))

dict = {
    'brand':'Ford',
    'elecric':False,
    'year':1996,
    'color':['red','white','blue']
}

x = dict['brand']
y = dict.get('year')
print(dict)
print(x)
print(y)

car = {
    'name':'Yamaha',
    'brand': 'Japanes',
    'model': 'R-15',
    'year':1965
}
x = car.keys()
print(x)
car['color']='white'
y = car.values()
print(car)
print(y)
a = car.items()
print(a)

thisdict = {
    'brand':'Ford',
    'model':'Mustang',
    'year':1990
}
if 'model' in thisdict:
    print('Yes,"model" is one of the keys in the thisdict dictionary')

thisdict.update({'brand':'Yamaha'})
print(thisdict)    
thisdict.pop('model')
print(thisdict)

thisdict = {
    'brand':'Ford',
    'model':'Mustang',
    'year':1990
}
thisdict.popitem()
print(thisdict)
thisdict.clear()
print(thisdict)

thisdict = {
    'brand':'Ford',
    'model':'Mustang',
    'year':1990
}
del thisdict['model']
print(thisdict)

thisdict = {
    'brand':'Ford',
    'model':'Mustang',
    'year':1990
}

for x in thisdict:
    print(x)
for x in thisdict:
    print(thisdict[x])
for x in thisdict.values():
    print(x)    

    for x in thisdict.keys():
        print(x)
for x,y in thisdict.items():
    print(x,y)        


thisdict = {
    'brand':'Ford',
    'model':'Mustang',
    'year':1990
}

my_dict = thisdict.copy()
print(my_dict)

'''thisdict = {
    'brand':'Ford',
    'model':'Mustang',
    'year':1990
}
my = dict(thisdict)
print(my)'''


#Nested Dictionary

my_family ={
    "Child1":{
        'name':'Emil',
        'year':2004
    },
    'Child2':{
        'name':'Tobias',
        'year':2006
    },
    'Child3':{
        'name':'Linus',
        'year':2011
    }
}
print(my_family)

Child1 = {
    'name':'rakib',
    'year':2002
}
Child2 = {
    'name':'Saklain',
    'year':1999
}
Child3 = {
    'name':'Rumi',
    'year':2005
}
my_family = {
    'child1':Child1,
    'child2':Child2,
    'child3':Child3
}
print(my_family)