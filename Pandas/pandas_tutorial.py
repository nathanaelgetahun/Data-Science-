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

print("")
#one way to creat a data frame is make a python dic, and have the values to be a python list of items 

data ={
  "name": ["Nati", "Yeshi", "Heaven"],
  "age": ["22", "40", "24"]
}

#to make this into a data frame you, 

df = pd.DataFrame(data, index=["Member 1", "Member 2", "Member 3"])

print(df, "\n")

print(df.loc['Member 1'], "\n")

print(df.iloc[1], "\n")

#add a new column
df["Job"] = ["SWE", "CNA", "Dr"]
print(df, "\n")

#add new rows, (create new dataFrame and concatenate it )
new_row = pd.DataFrame([{"name": "Thomas", "age": 22, "Job": "Engineer" },
                        {"name": "Shumet", "age": 34, "Job": "CNA"}],
                       index= ["Member 4", "Member 5"])
df = pd.concat([df, new_row])
print(df, "\n")

#importing
#to read data from a csv file 
csv_df = pd.read_csv("data.csv")
#this prints the first and last 5 rows in data frame
print(csv_df, "\n")

#to print all rows in df
print(csv_df.to_string(), "\n")

#to read data from a json file
json_df = pd.read_json("soccer.json")

print(json_df, "\n")

#Selection 
#selection by column 
print(csv_df["Name"])
#since python by default prints first 5 columns and 5 rows, to print the full version do this
print(json_df["name"].to_string())
#to select multiple columns, use a python list inside and select all the colmns you want to list
print(csv_df[["Height", "Weight", "Legendary"]].to_string())

#Selection by row/s
#selection using the loc property
print(csv_df.loc[1])
# you can set another colmun to serve as the index when you first read the data, lets say name for example since thats easier to look up
csv_df = pd.read_csv("data.csv", index_col = "Name")
print(csv_df.loc["Pikachu"])
#if you dont want all the data when displaying ur row, pass in a 2nd argument using a python list of all the colmns we would like to selct
print(csv_df.loc["Charizard", ["Height", "Weight"]])
#You can also select a range of rows using the slice operator 
print(csv_df.loc["Charizard" : "Blastoise"])
#seecting using iloc, choosing based of integer 
print(csv_df.iloc[0:11]) # this gives you the first 10 rows
print(csv_df.iloc[0:11:2]) #samething but this does by every 2nd row
#as a 2nd arguemnt you can select the indices of the colmns you would like 
print(csv_df.iloc[0:11:2, 0:3])

search_for = input("Who's stats do you want?(by name) ")

try:
  print(csv_df.loc[search_for])
except KeyError:
  print(f"{search_for} not found")

#Filtering = Keeping the rows that match a condition
#create a new data frame that we can strore filtered pokemon into
tall_pokemon = csv_df[csv_df["Height"] >= 2]
print(tall_pokemon)

heavy_pokemon = csv_df[csv_df["Weight"] >= 100]
print(heavy_pokemon)

#use the C style operator for "or", which is |
water_pokemon = csv_df[(csv_df["Type1"] == "Water") | (csv_df["Type2"] == "Water") ]
print(water_pokemon)

#use the C style operator for "and", which is & 
fire_flying_pokemon = csv_df[(csv_df["Type1"] == "Fire") & (csv_df["Type2"] == "Flying") ]
print(fire_flying_pokemon)

#aggregate functions = Reduces a set of values into a single summary value 
#Used to summarize and analyze data
#Often used with the groupby() function

#these functions are for a whole dataframe
print(csv_df.mean(numeric_only=True))
#sum all
print(csv_df.sum(numeric_only=True))
#min
print(csv_df.min(numeric_only=True))
#max
print(csv_df.max(numeric_only=True))
#count
print(csv_df.count())

#these functions are for a single column
print(csv_df["Height"].mean())
#sum all
print(csv_df["Height"].sum())
#min
print(csv_df["Height"].min())
#max
print(csv_df["Height"].max())
#count
print(csv_df["Height"].count())

#to group things based on what they have in column, create a groupby object
group = csv_df.groupby("Type1")
#now after grouping them by colmn name you can do different functions on those types1
print(group["Height"].mean())

#Data Cleaning = the process of fixing/ removing: incomplete, incorrect, or irrelevant data, 
#dropping irrelevent column(Its going to make a new df so you have to assign it to a variable)

df_drop_legend = csv_df.drop(columns = ["Legendary", "No"])
print(df_drop_legend)
#Handle missing data
#example:if row is missing type2, we are going to drop that entire row (dropna.() = drop not available)
df_typetwo = csv_df.dropna(subset= ["Type2"])
print(df_typetwo)

#we can fill in empty slots instead of dropping whole colmn with fillna function(fill any not available values)
df_typetwo_fill = csv_df.fillna({"Type2" : "None"})
print(df_typetwo_fill)

#to change all values of specfic value to a new value, use replace

df_typetwo_fill["Type1"] = df_typetwo_fill["Type1"].replace({"Grass" : "GRASS", "Fire" : "FIRE"})
print(df_typetwo_fill)

#Standardize text
#ex:make all name letters lowercase
df_typetwo_fill["Name"] = df_typetwo_fill["Name"].str.lower()


#Fix/Change data types
#ex: make the 0 and 1's in legendary column true or false;boolean..(using .astype function)
df_typetwo_fill["Legendary"] = df_typetwo_fill["Legendary"].astype(bool)

#Remove duplicate values
df_typetwo_fill = df_typetwo_fill.drop_duplicates()