# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:31:50 2023

@author: Daniel Sandoval
"""

#import os
#os.getcwd()

Bill = "William Byrd"

print("This is the beginning: " +Bill)
a = Bill.capitalize() #capitalizes the first letter of the string but lowercases the others.
print("with .capitalize(): " + a)

b = Bill.lower()
print("with .lower(): "+ b)

c = Bill.upper()
print("with .upper(): " + c)

d = Bill.index('Wi')
print(".index tells you where a certain values ('Wi') is located in the string: " + str(d))

e = Bill.find('da')
print(".find searches a value ('da') and tell you if it exist in the string, if it doesn't, returns -1: "+ str(e))

f = Bill.startswith('L')
print(".startswith tells you if the string start with the value ('L') you introduce: " + str(f))

g= Bill.endswith('d')
print('.endswith tells you if the string ends with the value you provide: ' + str(g))

h = Bill.isalpha()
print(".isalpha tells you if the string is made up of only letters: " + str(h) + "// spaces count as alphanumeric")

i = Bill.isalnum()
print(".isalnum() tell you if the string is alphanumeric: " + str(i))

j = Bill.islower()
print(j)
k = b.islower()
print(k)

l = Bill.isupper()
print(l)
n = Bill.isnumeric()
print(n)


string_count = 5
frets_count = 24

o = f"Noam's banjo {string_count} strings and {frets_count} frets"
print("with f at the beginning of the string and {} is possible to create strings that are updatable: " + o)

ship = " The Yankee Clipper"
a= ship.strip()
print(".strip() gets rid of the initial spaces in the string: " + a)

b = ship.lstrip()
print(".lstrip() gets rid of left space: " +b)

c = ship.rstrip()
print(".rstrip() gets rid of right space: " + b)

Word_string = "Here,Are,Some,Words"
print("Word_string is: "+Word_string)

d= Word_string.split(",")
print("With .split(delimiter in quotes) you can divide a string and make it a list: " + str(d))
print("After splitting, the variable is:" + str(type(Word_string.split(","))))

e = ":".join(d)
print("With delimiter in quotes.join -variable-, it is possible to make a list a string: " + e)
