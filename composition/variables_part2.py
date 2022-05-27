#Global Variables 
print("Global variables")
x =  "awesome"
def myFuncion():
    print("Python is " + x)

myFuncion()

#if you create a variable with the same name inside a function this  varible will be local and can only be used indside the function
X = "Mira"
def myfunc():
    X = "Amiriddin"
    print("My first name is " + X)

myfunc()

print("My nickename is " + X)

def myfuncion():
    global y
    y = "cool"

myfuncion()

print("You're ", y)

Y = "cool"
def myfun():
    global Y
    Y = "good"

myfun()

print("You're looking ", Y)