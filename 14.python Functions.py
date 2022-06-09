#PYthon functions

def myfunc():
    print('Hello World')
myfunc()

def myfunc(fname):
    print('My name is :',fname + " Refsnes")

myfunc('Emil')
myfunc('Tobias')
myfunc('Linus')

def name(fname, lname):
    print('My name is:',fname + " " + lname)

name('Rakib','hossen')
name('sakhib','khan')

def name (*kids):
    print('My kids name:'+ kids[1])

name('rakib','sakib','sumon')

def my_function(child3,child2,child1):
    print('The youngest child is :' + child3)

my_function(child1='Emil', child2='Sajib', child3='Rana')

def my_function(**kid):
    print("His Last name is " + str(kid))

my_function(fname='Sornaly',lname='Sanjida')

def country(country='Norway'):
    print('I am from ' + country)

country('Sweden')
country('Bangladesh')
country()
country('Brazil')


def function(food):
    for x in food:
        print(x)

fruits = ['apple','banana','chips']
function(fruits)

def my(x):
    return x * 3

print(my(5))
print(my(7))
print(my(29))

def tri_recursion(k):
    if (k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(0)