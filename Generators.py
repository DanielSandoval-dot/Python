# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 15:41:42 2023

@author: Daniel Sandoval and a lot of help from Google
"""
#%%
def fib():
    for cur in (0,1):
        last = cur
        yield cur
    while True:
        yield cur
        Last, cur = cur, last+cur

#%%

# 1. Write a Python program that creates a generator function 
# that yields cubes of numbers from 1 to n. Accept n from the user.

def cube_generator(n):
    for i in range(1, n+1):
        yield i**3

n = int(input("Input a number: "))

cubes = cube_generator(n)

for num in cubes:
    print(num)
    
#%%
# 2. Write a Python program to implement 
# a generator that generates random numbers within a given range.
import random

def random_generator(start, end):
    while True:
        yield random.randint(start, end)
        
start = int(input("Input the start value: "))
end = int(input("Input the end value"))

random_numbers = random_generator(start, end)

n = int(input("How many random numbers?"))
for x in range(n):
    print(next(random_numbers))
    
#%%

# 3. Write a Python program that creates a generator function that generates
# all prime numbers between two given numbers.
# DIFFICULT EXERCISE, Relatively hard without generators.
upper_x = int(input("Input maximum value: "))

def prime_check(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x ==0:
            return False
    return True


def prime_generator():
    n = 2
    while True:
        if prime_check(n):
            yield(n)
        n += 1

prime_numbers = prime_generator()
print(next(prime_numbers))

#%%

# 5. Write a Python program to implement a generator function 
# that generates all permutations of a given list of elements.
# To facilitate comprehension, generator that generates how many permitations 
# are possible in a number of companies  that consists of number of stocks 

#CALCULATE NUMBER OF POSSIBLE PERMUTATIONS
    
n = int(input("Amount of first group?"))
m = int(input("Amount of second group?"))
fact = 1
fact2 = 1
 
for i in range(1, n+1):
    fact = fact * i

for i in range(1, n+1):
    for j in range(1, m+1):
        if i==j:
            fact2 = fact2*1
        else:
            fact2 *= (i-j)
print(fact)
print(fact2)
print(fact/fact2)

#%% Combinations

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

if r > n:
    print("Invalid input: r should be less than or equal to n.")
else:
    combinations = nCr(n, r)
    print(f"Number of combinations (C({n}, {r})) is: {combinations}")
    
#%% Permutations

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def nPr(n, r):
    return factorial(n) / factorial(n - r)

n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))

if r > n:
    print("Invalid input: r should be less than or equal to n.")
else:
    permutations = nPr(n, r)
    print(f"Number of permutations (P({n}, {r})) is: {permutations}")
    
#%%
