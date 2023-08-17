# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:47:51 2023

@author: Daniel Sandoval
"""
import pandas as pd 
file_to_view = r"https://raw.githubusercontent.com/DanielSandoval-dot/practical-statistics-for-data-scientists/master/data/state.csv"
dat = pd.read_csv(file_to_view)
print(dat)

# view the DataFrame
print(dat.describe())
print(dat.head())
print(dat.tail())
# select columns by name and by .loc and iloc
print(dat.loc[0:10,'Population'])
print(dat.iloc[0:3,1])

# Creating mask with boolean operators

# Add rows
new_data = {'State':'BogotaYork','Population':9000000,'Murder.Rate':50.00,'Abbreviation':'BY'}
new_pd = pd.DataFrame([new_data]) # adding [] to the new data 
dat2 = dat.append(new_pd)
dat2.reset_index(inplace = True)
print(dat2.tail())

# Add columns

dat2.loc[:,'Dangerous?'] = dat['Murder.Rate'] > 5
print(dat2)

# Update value by index column and row .iloc
dat2.loc[0:1, 'Murder.Rate'] = 5.0 # There is a slight difference between using == and =.
#with == it becomes a boolean and the result is True or False, with = it updates the value. 
print(dat2)

# Update with math operations
dat2['Murder.Rate'] = dat2['Murder.Rate'] + 100
print(dat2)
# Update using replace method

dat2 = dat2.replace(True, "Yes")
print(dat2)
#Rename column

# Set column datatype

# Concatenate and create new column

# Rename columns 