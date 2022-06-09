#Python Inheritance 

from unicodedata import name


class Person:
    def __init__(self,fname,lname):
        self.firstname = fname 
        self.lastname = lname

    def printname(self):
        print('My name is : ',self.firstname,self.lastname)

x = Person('Rakib','Hossen')
x.printname()

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname 
        self.lastname = lname

    def name(self):
        print('My name is:',self.firstname,self.lastname)

class Student(Person):
    pass

a = Student('rakib','hossen')
a.name()

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def name(self):
        print(self.fname,self.lname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

a = Student('rakib','hossen')
a.name()

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def name(self):
        print(self.fname,self.lname)

class Student(Person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print('Welcome',self.fname,self.lname," to the class of",self.graduationyear)

x = Student('Asif','Khan',2019)
print(x.graduationyear)
x.name()
x.welcome()