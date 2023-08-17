# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 20:47:46 2023

@author: Daniel Sandoval
"""

# Dictionaries map keys to values.

#%% Creating dictionaries

Student = dict(Name="Henry", Age= 16)
print(Student)

dictionary2 = dict([["Name", "Henry"],["Age",16]])
print(dictionary2)

dictionary3 = {'Name':'Henry','Age':16}
print(dictionary3)

# Accesing Dictionary Data

print(Student['Age'])

Student['grade'] = 'A'
print(Student)

a = Student.get('Age')
print(a)

#%% Dictionary Views

student = {'name':'Sparky', 'age':'27','major':'Basketweaving'}
a = student.keys() #keys
b = student.values() #key values
c = student.items() #key value pairs

print(a)
print(b)
print(c)


'name' in student.keys()
for key, value in student.items():
    print(key, value)
    
#%% Sets - unordered, immutable collection of unique objects.

s= set("aaaaabbbbbbcccccc")
s2= set("bbbddd")
print(s)

#Adding to a set
s.add('d')
s.pop('d')

print(s.isdisjoint(s2))# as they share many
print(s2.issubset(s)) # s has all the values from s2

print(s2.union(s))
print(s2.intersection(s))
print(s2.difference(s))
