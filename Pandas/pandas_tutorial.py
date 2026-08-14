import pandas as pd

#bro code
print(pd.__version__)

#Series = one-dimensional. Think of it like a single column of data, a list of values with labels (an index) attached to each one.
data = [100, 102, 104, 200, 202] #using a python list to create a series
series = pd.Series(data, index=["a", "b","c","d","e"]) #can have custom lables using index key word argument 
print(series.loc['a']) #how to accses value based on label, use loc 

#to update a value,you have to accses loc property 
series.loc["c"] = 201
print(series.loc['c'])

#to accses based on intergere postion use iloc
print(series.iloc[1])

#filter by label 
print(series[series < 200])

print("")

#No need to pass in an index, we can use the keys as labels  
calories = {"Day 1": 1750, "Day 2": 2001, "Day 3": 1900}

seriess = pd.Series(calories)

print(seriess)

seriess.loc['Day 3'] += 500

print(f"Updated Day 3 calories: {seriess.loc['Day 3']}")


print(f'where i followed my diet {seriess[seriess < 2000]}')


#DataFrame = two-dimensional. It's a full table, rows and columns, basically like a spreadsheet or a SQL table. 
#And actually, each individual column inside a DataFrame is a Series.


