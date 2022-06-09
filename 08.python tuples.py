#Python tuple() 

thistuple = ('apple','banana','cherry')
print(thistuple)

thistuple = ('apple','banana','cherry')
print(len(thistuple))

tuple1 = ('apple','banana','cherry')
tuple2 = (1,2,3,4)
tuple3 = (True,False,False)
print(tuple1)
print(tuple2)
print(tuple3)

a = ('apple')   #Not a tuple
print(a)

a = ('banana',)  #this is a tuple

thistuple = tuple(('apple','banana','cherry'))
print(thistuple)

name = ('apple','banana','cherry')
if 'apple' in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

x = ('apple','banana','cherry')    
y = list(x)
y[1] = "Kiwi"
x = tuple(y)
print(x)


thistuple = ('apple','banana','cherry')
y = ('orange',)
thistuple += y
print(thistuple)
y = list(thistuple)
y.remove('orange')
thistuple = tuple(y)
print(thistuple)


fruits = ('apple','banana','cherry')
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)

fruits = ('apple','banana','cherry','strawberry','raspberry')

(green,yellow,*red) = fruits
print(green)
print(yellow)
print(red)

# loop function

thistuple = ('apple','banana','cherry')
for x in thistuple:
    print(x)

thistupel = ('apple','bangladesh','china')

for x in range(len(thistupel)):
    print(thistupel[x])    

tuple = (3,5,8,0,2,4)
i = 0
while i < len(tuple):
    print(tuple[i])
    i += 1