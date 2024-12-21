#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:37:23 2022

@author: raimonbaudoin
"""

import pandas

# file_name = pandas.read_csv('file.csv') <---- format of read_csv

data = pandas.read_csv('transaction.csv')

data = pandas.read_csv('transaction.csv', sep=';')

# Summuray of the Data.
data.info()

# Worrking with calculations

# Working with variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

# Mathemetical operations on Tableau

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem

CostPerTransaction = CostPerItem * NumberOfItemsPurchased

SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased
# variable = dataframe('ColumnName')

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# Adding new Column to Dataframe

data['CostPerTransaction'] = CostPerTransaction

# Sales per transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit per transaction <--- Sales - Cost
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup calculation <--- (Sales - Cost) / Cost
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

# Rounding markup.
RoundMarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'], 2)

# Combining data fields Date

# my_name = 'raimon' + 'coding'

# my_date = 'Day' + '-' + 'Month' + '-' + 'Year' 


# Checking Colums Datatype.

print(data['Day'].dtype) 

# Change colums type.

day = data['Day'].astype(str) 
print(day.dtype) 

my_day = day + '-'

data['Day'] = my_day

year = data['Year'].astype(str) 
print(day.dtype) 

my_year = '-' + year

data['Year'] = my_year

my_month = data['Month']

print(my_day + my_month + my_year)


data['Date']  = my_day + my_month + my_year


# Using ilock to view specific colums and rows

data.iloc[0] # <---- views the row with index zero
data.iloc[0:3] # <---- views the first 3 rows
data.iloc[-5:] # <---- views the last 5 rows

data.head(5) # <---- views the first 5 rows

data.iloc[:,2] # <---- views all rows on 2nd column

data.iloc[4,2] # <---- views the 4th row, 2nd column

# Deleting unwanted colums

# DeleteList=['Day','Month', 'Year']
# print(DeleteList)
# data.drop(DeleteList, axis=1, inplace=True) 

# Using split to split the clients keywords field
# new_var = column.str.split('sep', expand = True)

clientkeywords = data['ClientKeywords'].str.split(',', expand = True)
print(clientkeywords)
print(clientkeywords[0])

# Creating new coloms names for the clientkeywords 

data['ClientAge'] = clientkeywords[0]
data['BusinessType'] = clientkeywords[1]
data['OnboardTime'] = clientkeywords[2]

# Using the replace function to replace [ ] ' with nothing

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['OnboardTime'] = data['OnboardTime'].str.replace(']', '')

data['ClientAge'] = data['ClientAge'].str.replace("'", "")
data['BusinessType'] = data['BusinessType'].str.replace("'", "")
data['OnboardTime'] = data['OnboardTime'].str.replace("'", "")



# Using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

# Using the capatalize function to change first item to uppercase

data['ItemDescription'] = data['ItemDescription'].str.capitalize()


# How to merge files
# Bringing in new dataset

dataSeasons = pandas.read_csv('value_inc_seasons.csv', sep=';')

# Merging files: merge_dataframe = pandas.merge(dataframe_old, dataframe_new, on = 'key')

data = pandas.merge(data, dataSeasons, on = 'Month')


# Dropping columns

# Dataframe = Dataframe.drop('column_name', axis = 1)


DeleteList=['ClientKeywords', 'Day', 'Year', 'Month']
data.drop(DeleteList, axis=1, inplace=True)

# Or delete multiple items like this:
# data.drop(['ClientKeywords', 'Day', 'Year', 'Month'], axis=1)

# Export into CSV

# data.to_csv('valueInc_Cleaned.csv', index = False)


 














