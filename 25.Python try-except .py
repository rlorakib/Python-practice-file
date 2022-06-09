#Python try/except

try:
    print(x)

except:
    print("An exception occurred")

try:
    print(x)

except NameError:
    print("Variable x is not defined")

except:
    ('Something else went wrong')

try:
    print('Hello world')

except:
    print('Something went wrong')

else:
    print('Nothing went wrong')

x = ()
try:
    print(x)
except:
    ('Something went wrong')
finally:
    print("The 'try except' is finished")




try:
    f = open("15.Python lambda.py")
    try:
        f.write("Lorum Ipsum")
    except:
        print('Something went wrong when writing to the file')
    finally:
        f.close
except:
    print('Something went wrong when opening the file')



x = -1

if x < 0:
    raise Exception('Sorry, no numbers below zero')

x = 'hello'

if not type(x) is int:
    raise TypeError('Only allowed interger')