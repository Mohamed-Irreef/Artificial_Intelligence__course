import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("leave.csv")

# print(df.head())

# 1. line plot
# sns.lineplot(data=df, x="Month",y="Name",hue="Day")
# plt.show()

# 2. Bar Plot
# new_df= df.groupby("Month").count()
# print(new_df)
# sns.barplot(data=new_df, x="Month",y="Date")
# plt.show()

# 3. Histogram - seperate into the bins & see the distribution
# sns.histplot(data=df, x="Date", bins=3, kde=True) # kernel Density Estimator -> to understand the distribution
# plt.show()

# 4. Scatter plot -  scater distribution
# sns.scatterplot(data=df, x="Date", y="Name", hue="Month")
# plt.show()

# 5. Box Plot - helps in outlier direction (Jan,1000,Tuesday,Men Function - outlyer data)
# sns.boxplot(data=df)
# plt.show()

# 6. Violin Plot (Mixed of data distribution in hostogram and the otlyer distribuition in the box plot. the white line in the box plot is the "Median")
# sns.violinplot(data=df)
# plt.show()

# 7. Heat Map (Display data correlation)
# print(df.corr(numeric_only=True))
# sns.heatmap(df.corr(numeric_only=True), annot=True)
# plt.show()

# 8. Joint plot (Data distributioon + bar plot)
# sns.jointplot(data=df,x="Month",y="Day")
# plt.show()

# 9. pairplot (Data distributioon + bar plot)
# sns.pairplot(data=df)
# plt.show()