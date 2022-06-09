#Python scope

def myfunc():
    x = 300
    print(x)

myfunc()


def func():
    x = 200
    def innerfunc():
        print(x)

    innerfunc()

func()


x = 333
def num():
    print(x)

num()
print(x)

a = 3433

def number():
    a = 323 
    print(a)

number()
print(a)

def rakib():
    global x
    x = 322
    

rakib()
print(x)


a = 233

def name():
    global a
    a = 344

name()
print(a)