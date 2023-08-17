# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 09:34:55 2023

@author: Daniel Sandoval
"""
output = []
for x in range(10):
    output.append(x**2)
print(output)

#List comprehension style
output2 = [x**2 for x in range(10)]
print(output2)


#with for loop
import random
scores = []
for i in range(5):
    scores.append(random.randint(i,10))
print(scores)

#with list comprenhension

scores2 =[random.randint(i, 10) for i in range(5)]
print("scores2 is: " + str(scores2))

#Filter a sequence

caps = []
for letter in "Henry Honey":
    if letter.isupper():
        caps.append(letter)
print(caps)

caps1 = [letter for letter in "Henry Honey" if letter.isupper()]
print(caps1)


#example1
string1 = []
for letter in "Daniel Sandoval":
    if letter.isalpha():
        string1.append(letter)
print(string1)

string2 = [i.upper() for i in "Daniel Sandoval" if i.isalpha()]
print(string2)



