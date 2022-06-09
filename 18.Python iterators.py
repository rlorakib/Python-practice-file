#Python iterators

tuple = ('apple','banana','cherry')
mytuple = iter(tuple)

print(next(mytuple))
print(next(mytuple))
print(next(mytuple))


mystr = 'banana'
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ('apple','banana','cherry')

for x in mytuple:
    print(x)


mystr = 'apple'

for x in mystr:
    print(x)


class Mynumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = Mynumber()
liter = iter(myclass)

print(next(liter))
print(next(liter))


class number:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x

        else:
            raise StopIteration

name = number()
iter = iter(name)

for x in iter:
    print(x)