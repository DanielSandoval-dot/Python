# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 10:01:24 2023

@author: Daniel Sandoval
"""

#   x!=y ; x is not equal to y
#   x>y ; x is greater than y
#   x<y ; x is less than y
#   x>=y ; x is greater than or equal to y
#   x<=y ; x is less than or equal to y

import random

list1 = [random.randint(0,500) for i in range(5)]
print(list1)

list2 =[]
for i in range(5):
    list2.append(random.randint(0,500))
print(list2)

for x in list1:
    if x%2 ==0:
        print(x, "is even")
    else:
        print(x, "is odd")
        

        

