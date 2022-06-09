#Python JSON 

import json

x = { 
    'name':'Rakib hossen',
    'age':22,
    'village':'Jhenaidah'
}

y = json.dumps(x)

print(y)


import json

x = '{"name":"John","age":30,"city":"New York"}'

y = json.loads(x)
print(y["name"])

print(json.dumps({"name":"john","age":33}))
print(json.dumps(["apple","banana"]))
print(json.dumps(('tuple','cherry')))
print(json.dumps("hello friend"))
print(json.dumps(32))
print(json.dumps(32.43))
print(json.dumps(True))
print(json.dumps(None))
print(json.dumps(False))


import json

x = {
    "name":"Rakib hossen",
    "age":21,
    "married":False,
    "divorced":False,
    'children':("No"),
    "pets":None,
    'cars':[
        {'model':'BMW 230',"mpg":27.5},
        {'model':"Ford Edge","mpg": 24.1}
    ]
}

print(json.dumps(x))

import json

x = {
    "name":'Rakib hossen',
    'age':32,
    "married":False,
    "children":('No my children'),
    'cars':[
        {'model':'BMW','CC':1000},
        {'model':'Kawashaki',"cc":500}
    ]
}

print(json.dumps(x,indent=4))


import json

x = {
    "name":'Rakib hossen',
    'age':32,
    "married":False,
    "children":('No my children'),
    'cars':[
        {'model':'BMW','CC':1000},
        {'model':'Kawashaki',"cc":500}
    ]
}

print(json.dumps(x,indent=4, separators=('.','='), sort_keys=True))