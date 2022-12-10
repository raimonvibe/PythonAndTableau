import pandas
import json
import numpy # Used for Arrays
import matplotlib .pyplot as pyplot

# Method 1 to read json data.

json_file = open('loan_data_json.json')
data = json.load(json_file)

# Method 2 to load json data.

with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
# Transform to DataFrame

loandata = pandas.DataFrame(data)

# Finding unique values for the purpose column

loandata['purpose'].unique()

# Describing the data

loandata.describe()

# Describe the data for specific column

loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

# Using exp() to get the annual income

income = numpy.exp(loandata['log.annual.inc'])

loandata['annualincome'] = income

# Working with arrays


# 1D array
array = numpy.array([1, 2, 3, 4])

# 0D array
array = numpy.array(43)

# 2D array
array = numpy.array([[1, 2, 3], [4, 5, 6]])


# fico score

# fico: The FICO credit score of the borrower. 
# - 300 - 400: Very Poor
# - 401 - 600: Poor
# - 601 - 660: Fair
# - 661 - 780: Good
# - 781 - 850: Excellent

fico = 250

if fico >= 300 and fico < 400:
    ficocaat = 'Very poor'
elif fico >= 400 and fico < 600:
    ficocaat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocaat = 'Fair'
elif fico >= 660 and fico < 700:
    ficocaat = 'Good'
elif fico >= 700:
    ficocaat = 'Excellent'
else:
    ficocaat = 'Unknown'
print(ficocaat)


# For loops

fruits = ['apple', 'pear', 'banana', 'cherry']

for item in fruits:
    print(item)
    item2 = item + ' fruit'
    print(item2)
   
# in range doesn't include last number    
for item in range(0, 4):
    item2 = fruits[item] + ' for sale'
    print(item2)
    
# Applying for loops to loan data

# Using first 10
length = len(loandata)
ficocat = []
for item in range(0, length):
    category = loandata['fico'][item]
    
    try:
        
        if category >= 300 and category < 400:
            cat = 'Very poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
    ficocat.append(cat)
    
ficocat = pandas.Series(ficocat)

loandata['fico.category'] = ficocat


# df.loc as conditional statements
# df.loc[df[columnName] condition, newColumnName] = 'value if the condition is met'

# For interests rates, a new column is wanted, if the rate > 0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'



# Number of loans/rows by fico category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'pink', width = 0.1)
pyplot.show()
purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'pink', width= 0.5 )
pyplot.show()

# Scatter plots

ypoint = loandata['annualincome']
xpoint = loandata['dti']
pyplot.scatter(xpoint, ypoint, color = 'pink')
pyplot.show()

# Writing to csv
loandata.to_csv('loan_cleaned.csv', index = True)





    
    









 
 
 
 
    
    
    
