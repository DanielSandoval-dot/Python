# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 23:00:58 2023

@author: Daniel Sandoval
"""
#%% Create a DataFrame in Pandas 

import pandas as pd

data = {'Name':['Carl','Carol','Cas'],
        'Age':[43, 23, 30],
        'Score':[123, 168, 14]}

data2 = [['Carl', 43, 123], ['Carol', 23, 168], ['Cas', 30, 14]]
df = pd.DataFrame(data2)

df2 = pd.DataFrame(data2, columns=['Name', 'Age', 'Score']) 

print("This is before: \n", df)

print("This is after: \n", df2)

#%% Viewing the DataFrame

file_to_view = r"https://raw.githubusercontent.com/DanielSandoval-dot/practical-statistics-for-data-scientists/master/data/state.csv"
dat3 = pd.read_csv(file_to_view)
# print(dat3)

# dat3_dict = dict(dat3)
# print(dat3_dict)

print(dat3.head())  # prints the first five rows
print(dat3.tail()) # prints the last five rows
print(dat3.describe())
print(dat3.min())
print(dat3.std())

print(dat3['State'])    # One way of selecting a column
print(dat3.State)       # Second way of selecting a column

print(dat3.iloc[0:3, 1]) # Selecting based on rows, columns
print(dat3.loc [1:3, ['State','Population']])

#%% Selecting Data using boolean mask
file_to_view2 = r"https://raw.githubusercontent.com/DanielSandoval-dot/practical-statistics-for-data-scientists/master/data/house_sales.csv"
dataf = pd.read_csv(file_to_view2, sep = '\t')

dataf_subset = dataf[['PropertyID','Bathrooms','Bedrooms']]
print(dataf_subset.head())

# Creating a mask
# In boolean operations and Pandas, a mask refers to a boolean array 
# or a boolean Series that is used to filter or select elements 
# from another array or Series based on some condition. 
# It's a way to specify which elements satisfy a particular condition and which don't.

mask = dataf_subset.loc[:,'Bathrooms'] > dataf_subset.loc[:,'Bedrooms']
print(mask)
print(dataf_subset[mask])

# The mask helps us identify which row meet the critaria Bathroom > Bedroom, only 1078 rows do and we can filter them. 

## Boolean operators and(&), or (|), not(~) can be used to 
mask2 = (dataf_subset.loc[:,'Bathrooms'] > 2) | (dataf_subset.loc[:,'Bedrooms'] == 3)
print(mask2)
print(dataf_subset[mask2])

##Creating a new column

dataf_subset.loc[:'Bathroom/Bedroom ratio'] = dataf_subset.loc[:'Bathrooms'/int('Bedrooms')]
print(dataf_subset)


## Using unique()

#%% More exercises on selecting data

import pandas as pd
import numpy as np
import random

num_rows = 100
colors = ['Red', 'Blue', 'Green']

df = pd.DataFrame( {'color': [colors[random.randint(0,2)] for _ in range(num_rows)],
                    'integers': [random.randint(0,15) for _ in range(num_rows)],
                    'floats': [random.random() for _ in range(num_rows)]})

df.loc[:,'Is it red?'] = df['color'] == 'Red' #Creating a column that check if the value is 

print(df)

#%% Update DataFrames


import pandas as pd 

data = {'first':['Carl','Francis','Sam'],'last':['Po','Nyguen','Smith'],'age':['32','45','22'],'CH_count':[12,14,39]}
clients = pd.DataFrame(data)

# Add rows
new_data = {'first':['Sue','Boya'], 'last':['Rankler', 'Maple'],'age':[93, 12], 'CH_count':[22, 1]}
new_clients = pd.DataFrame(new_data)
clients = clients.append(new_clients)
print(clients)

 
# Update to specific value. Based on .loc(row index, header)
clients.loc[1, 'first'] = 'Frankie'
print(clients)

#Update values from two colums by slicing (row indexes, hearder)
clients.loc[0:1, 'CH_count'] = -1
print(clients)


# Update using math operations
clients.CH_count = clients.CH_count -1 # Using update statement to actually change the table
print(clients)


clients. CH_count -=3  # in place, actually making the change
print(clients)

# Updating using replace method
clients.replace(-4, 0)
print(clients)

#%% Manipulating Pandas DataFrames

# Rename a column
import pandas as pd
data={'first': ['Carl', 'Francis', 'Sam'],'last':['Po', 'Nyguen', 'Smith'],'age':['32', '45', '22']}
clients = pd.DataFrame(data)
print(clients)

clients.rename(columns={'first':'First Name', 'last':'Last Name'}, inplace = True) # to update the actual DataFrame, add ", inplace =True")

#To go back to inital values,
clients.reset_index(inplace=True)

clients.rename(index={0:'a', 1:'b', 2:'c'})

# Drop columns
clients.drop(columns='First Name')

# Drop rows 
clients.drop(index=0)

# Set column data types
clients.age
clients.age.astype(int)


data={'first': ['Carl', 'Francis', 'Sam'],'last':['Po', 'Nyguen', 'Smith'],'age':['32', '45', '22']}
clients = pd.DataFrame(data)

# Concatenate 
clients['Name'] = clients['first'] + [" "] + clients['last']
print(clients)
