#Python RegEx 

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)

if x:
    print('We have a match!')
else:
    print('No match')

import re 

txt = "The rain in Spain"
x = re.findall("ai",txt)
print(x)


txt = "The rain in Spain"
y = re.findall('Portugal',txt)
print(y)


txt= "The rain in Spain"
a = re.search('\s',txt)
print("The first white-space character is located in position:",a.start())

text = "The rain in Spain"
b = re.search('Portugal',text)
print(b)


txt = "The rain in Spain"
a = re.split('\s',txt)
print(a)



import re
txt = 'The rain in Spain '
x = re.split('\s',txt,1)
print(x)

txt = "The rain in Spain"
a = re.sub('\s','$',txt)
print(a)

bak = "The rain in Spain"
x = re.sub('\s','@',txt,2)
print(x)

a = re.search('ai',bak)
print(a)

txt = "The rain in Spain"
a = re.search(r"\bS\w+",txt)
print(a.span())
a = re.search(r"\bS\w+",txt)
print(a.string)

print(a.group())