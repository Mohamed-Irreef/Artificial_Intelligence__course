import pandas as pd

data = {
    "Name" : ["Arjun","Arun","Kishore"],
    "Age" : [24,22,20]
}

df = pd.DataFrame(data, index=["Employee 1","Employee 2","Employee 3"])
df["Salary"] = [20000,10000,30000] #Adding new column
df1 = pd.DataFrame([{"Name":"Mohamed","Age":20,"Salary":40000}], index=["Employee 4"])
df = pd.concat([df,df1])
print(df)