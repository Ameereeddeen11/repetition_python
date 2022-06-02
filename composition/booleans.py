#booleans represent one of two values True or False
print(10 > 96)

#for exemple
a = 450 
b = 8471

if b > a:
    print("number b is bigger than number a")
else:
    print("number b is not bigger than number a")


#Evaluate Values and Variables 
"""most values are true: almost any value is evaluated to true if it has some sort of content
                            any string is true except empty string
                            any number is true except 0
                            any list, tuple, set, and dictionary are true except empty ones"""

print(bool("Amir"))
print(bool(145))
print(bool(["Audi", "BMW", "Mersedense-Benz"]))

#there are values are false becouse do not meet the conditions
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

