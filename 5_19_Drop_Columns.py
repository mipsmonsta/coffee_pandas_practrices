import pandas as pd

df = pd.read_csv("Cars.csv")

df.drop("fuel", axis=1, inplace=True) # drop the whole column with axis=1
result = df.columns[1]
print(df)
print(result)