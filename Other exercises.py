# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:19:23 2023

@author: Daniel Sandoval
"""

#person = input('What is your name?')
#greeting = f"Hello {person}"
#print(greeting)

verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
for verb in verbs:
    x = verb + "ing"
    ing.append(x)
    print(x)
print(ing)


numbs = [5, 10, 15, 20, 25]
nums = []

for num in numbs:
    x = num + 5
    nums.append(x)
    print(x)
    print(nums)


numbs = [5, 10, 15, 20, 25]
nums = []
for numb in numbs:
    num = numb + 5
    nums += [num]
numbs = nums
print(numbs)

output = ""
for i in range(35):
    x = "a"
    output = output + x
print(output)
