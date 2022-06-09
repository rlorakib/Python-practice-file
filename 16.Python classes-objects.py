#Python Classes/Objects 

class Myclass:
    x = 5

p1 = Myclass
print(p1.x)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("John",32)

print(p1.name)
print(p1.age)


class Student():
    roll = ''
    gpa = ''

rahim = Student()
rahim.roll = 118702
rahim.gpa = 3.74
print(f"Roll:{rahim.roll},GPA:{rahim.gpa}")

karim = Student()
karim.roll = 118700
karim.gpa = 3.21
print(f"Roll:{karim.roll},GPA:{karim.gpa}")

class Student():
    roll = ""
    gpa = ""

    def _set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll:{self.roll}, GPA:{self.gpa}")

rakib = Student()
rakib._set_value(12035,4.10)
rakib.display()
rakib.roll = 126721
rakib.display()

class Student():
    roll = ''
    gpa = ''

    def __init__(self,roll,gpa):
        self.roll = roll 
        self.gpa = gpa
        print(f"Roll:{self.roll}, GPA:{self.gpa}")

bakka = Student(118704,4.89)

bakka.gpa = 7.12
print(bakka.gpa)
