#w3schools syntax exercises:
print("Hello world")

if 5 > 2:
    print("Five is greater than two!")

#w3schools comment exercises:
#This is a comment

'''
This is a comment
written in more
than one line
'''

#w3schools variables exercises:
carname = "Volvo"

x = 50

x = 5
y = 10
print(x + y)

x = 5
y = 10
z = x + y
print(z)

myfirst_name = "John"

x = y = z = "Orange"

def myfunc():
    global x
    x = "fantastic"

#w3schools datatypes exercises:

x = 5
print(type(x))
#it will print "int"

x = "Hello world"
print(type(x))
#it will print "str"

x = 20.5
print(type(x))
#it will print "float"

x = ["apple", "banana" , "cherry"]
print(type(x))
#it will print "list"

x = ("apple", "banana", "cherry")
print(type(x))
#it will print "tuple"

x = {"name" : "John", "age" : 36}
print(type(x))
#it will print "dict"

x = True
print(type(x))
#it will print "bool"

#w3schools numbers exercises

x = 5
x = float(x)

x = 5.5
x = int(x)

x = 5
x = complex(x)

#w3schools strings exercises

x = "Hello world"
print(len(x))

txt = "Hello world"
x = txt[0]

txt = "Hello world"
x = txt[2:5]

txt = " Hello world "
x = txt.strip()

txt = "Hello World"
txt = txt.upper()

txt = "Hello world"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#w3schools boolean exercises

print(10>9)
#it will print "True"

print(10 == 9)
#it will print "False"

print(10 < 9)
#it wll print "False"

print(bool("abc"))
#it will print "True"

print(bool(0))
#it will print "False"

#w3schools operators exercises

print(10*5)

print(10/2)

fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

if 5 != 10:
    print("5 and 10 is not equal")

if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")

#w3schools if...else exercises

a = 50
b = 10
if a > b:
    print("Hello world")

a = 50
b = 10
if a != b:
    print("Hello world")

a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")

a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

if a == b and c == d:
    print("Hello")

if a == b or c == d:
    print("Hello")

if 5 > 2:
    print("Five is greater than two!")

if 5 > 2: print("Five is greater than two!")

print("Yes") if 5 > 2 else print("No")