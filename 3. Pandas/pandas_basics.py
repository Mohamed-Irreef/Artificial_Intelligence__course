import pandas as pd

# There are two data types in the panadas. One is "Series" and another one is "Data Frame"

# 1. Series (1 dimensional labeled data)
# arr1 = pd.Series([1,2,3], index=["x","y","z"])
# print(arr1)

# 2. Dataframe 
# data = {"names":["Arjun","Ram"], "age":[20,30]}
# arr2 = pd.DataFrame(data)
# print(arr2)

# 3. Read the data from csv or excel file
# csv_df = pd.read_csv("file.csv")
# excell_df= pd.read_excel("file.xlsx")

# 4. Save the data as csv or excel file / exporting the df
# df4 = pd.read_csv("file.csv")
# df4.to_csv("give_filenamne.csv", index=False) # it will remove the S.No and save it
# df4.to_excel("give_filenamne.xlsx")

# 5. see rows in the dataframe
import pandas as pd
df5 = pd.read_csv("month.csv")
print(df5.describe())
# print(df5.head()) # display first 5 rows
# print(df5.head(3)) # display first 3 rows
# print(df5.tail()) # display last 5 columns
# print(df5.shape) # display the (rows,columns)
# print(df5.info()) # display the column names, not null counts and data types
# print(df5.describe)
# print(df5.isnull()) # display all the nXm table and display the tru for the null valu and false for the null value
# print(df5.isnull().sum()) # display the number of null values for each column
# print(df5.value_counts("Name")) #display the number of repeation for each "column value"
# print(df5.mean())

# 6. To choose single column
# print(df5["Name"]) #display that particular single column
# print(df5[["Name","Numeric"]]) #display all those entered column datas

# 7. Apply column Condition
# print(df5[df5["Numeric"]>6]) # display all the rows which satisfy this condition

# 8. Iloc to print the specific rows & columns
# print(df5.iloc[:,:]) # iloc[row start:row end, col start : col end]
# print(df5.iloc[:,-1]) # -1 represents the last index of that row/col

# col delete
# df.drop('column_name', axis=1)
# df.drop(columns=['column_name'], inplace=True)

# row delete
# df.drop(index=0) # single row
# df.drop(index=[0, 1, 2] #multiple rows