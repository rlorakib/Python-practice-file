#Python String

print('hello world') #print function

a = 'hello'
print(a)  #assign string to a variable

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt     #multiline string use double quotes
ut labore et dolore magna aliqua."""
print(a)

#Multiline string use three single quotes.

a = '''Lorem iqsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello World!"
print(a[1])


for x in 'banana':  # for loop
    print(x)


a = "Hello world"

print(len(a))

b = "hello, world!"
print(b[2:5])   # The first character has index 0.

b = "hello, world"
print(b[:5])  #5 not included

print(b[2:])

a = "Hello !gyes"
print(a[-5:-3])   #-5 position is ! and -3 position is y


# string lower and upper case

a = "Hello World!"
print(a.lower())

a = "Hello buddy"
print(a.upper())

#Whitespace remove strip method

a = " bangladesh is beautiful country "
print(a.strip())

b = a.strip()
print(b)

#Replace method

a = "hello Rakib"
print(a.replace("h",'J'))

#Split() method

a = "Beautiful bangldesh"
print(a.split())

#Concatenataion

a = 'hell0'
b = 'world'
c = a + b
print(c)

x = "Hello "
y = "World"
c = a +" "+b
print(c)

#Format method()

age = 36
txt = "My name is Rakib, and I am {}"
print(txt.format(age))

quantity = 3
item = 4
price = 39.5
my_order = "I want {} pieces of item {} for {} dollors."
print(my_order.format(quantity,item,price))

quantity = 4
item = 23
price = 32
myorder ="I want to pay {2} dollors for {0} pieces of item {1}"

print(myorder.format(quantity,item,price))

txt = "We are the\n so-called \"Vikings\" from \\the north."
print(txt)

a = "bangladesh, srilanka, kuet, malaysia,singapore,jesshorE,JhenidaH"
print(a.capitalize())

b = "Bangladesh is a Small country and beautiful"
x = b.casefold()
print(x)

a = "rakib"
print(a.center(34))

x = "Hi, How are you?"
x = x.index('are')
print(x)