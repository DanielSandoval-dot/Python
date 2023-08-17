# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 22:33:45 2023

@author: Daniel Sandoval
"""

line = "Daniel"
print("Daniel is a name with " + str(len(line)) + " letters") # find the length of the variable with len()
print(line[1]) # the position starts from 0 to the end

print(line.index("e")) # returns the position where e is at.

print(line[0:3]) # add : to call the character from until but not including the last position

line.replace("e","replacement") #replaces a value by another
print(line)


list1 = [10, 20, 30, 40]
print(list1)


a = "I have had an apple on my desk before"
print(a.count("a"))

print(list1)
del list1[1] # deletes a value from the list based on position
print(list1)

list1[1] = 20
print(list1) #updates a value based on position

list1.insert(2, 30) #inserts a value like position, value
print(list1)

list1.sort() # order the values from smalles to largest
print(list1)

list1.reverse() # order values from largest to smallest
print(list1)

list1.remove(20) #removes the value from the 
print(list1)

list1.pop()#removes the last item
print(list1)

visp=["Da Vinci", "Franklin"]
visp.extend("Michelangelo")
print(visp)

