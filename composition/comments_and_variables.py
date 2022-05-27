#Comments
#this is the commet 
from ast import Global
from tkinter import N


print("Hi there :D")
""""This is a comment written 
in more than just on line"""


#Variables 
x = 895
y = "Amiriddin"
print(x)    #it will print only number 5
print(y)    #it will print only name Amiriddin
print(type(x))   #it will print which data type is it for this is int
print(type(y))   #it will print which data type is it for this is str

#many values to multiple variable 
print("many values to multiple variables")
a, b, c = "Ford", "BMW", "Mercedes-Benz"
print(a)
print(b)
print(c)

#and you can assign the same value to multiple variable in one line
print("One value to multiple variables")
k = l = m = "Audi"
print(k)
print(l)
print(m)

#python allows you to extract the values into variable
print("unpack a collection")
mobile_phone_brend = ["apple", "samsung", "oneplus"]
A, B, C = mobile_phone_brend
print("mobile phone brend: ", A)
print("mobile phone brend: ", B)
print("mobile phone brend: ", C)

#output varial=bles 
print("Output varial=bles")
X = "My"
Y = "name"
Z = "is Amir"
print(X, Y, Z)
#can also use the + operatorto output multiple variables

K = 194984
L = 194651
print("The answer for ", K, " + ", L, " is ", K + L)

M = 17
N = "Amiriddin"
print("My name is ", N, "and I am ", M, "years old")
