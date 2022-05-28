#Multiline strings 
from re import X


a = """Hi name is Amir
and I am 17 years old 
and I am from from Uzbekistan"""
print(a)
#or you can use '''...'''

#strings are arrays 
b = "hi there :D"
print(b[1])  #will print i becouse h is on array 0 and i is on array 1

#looping through a string 
for c in "Audi":
    print(c)    #since strings are arrays

#string length
x = "Hi there :D"
print(len(x))   #will print how much length of a string

#check string 
txt = "My favirate car is BMW I8"
print("car" in txt)   #I ask 'is the string car on on the string txt?'
#will print true becouse strign car is on string txt
#if the string is not on the string it will return false
#or you can write 
if "car" in txt:
    print("Yes, 'car' is present. ")


#string format 
age = 17
name = "My name is Amir and I am {}"
print(name.format(age))   #will print My name is Amir and I am 17

quantity = 4
itemno = 475
price = 39.90
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))



#boolean functions 
def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")