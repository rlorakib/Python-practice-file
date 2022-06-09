#Python datetime

import datetime
from re import A

x = datetime.datetime.now()
print(x)

print(x.strftime("%a"))
print(x.strftime("%w"))
print(x.strftime("%d"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%m"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%H"))
print(x.strftime("%I"))
print(x.strftime("%p"))
print(x.strftime("%M"))
print(x.strftime("%S"))
print(x.strftime("%f"))
print(x.strftime("%z"))
print(x.strftime("%Z"))
print(x.strftime("%j"))
print(x.strftime("%U"))
print(x.strftime("%W"))
print(x.strftime("%c"))
print(x.strftime("%C"))
print(x.strftime("%x"))
print(x.strftime("%X"))


print(x.year)
print(x.strftime("%A"))

import datetime

x = datetime.datetime(2022,6,5)
print(x)

import datetime

x = datetime.datetime(2022,6,5)
print(x.strftime("%B"))