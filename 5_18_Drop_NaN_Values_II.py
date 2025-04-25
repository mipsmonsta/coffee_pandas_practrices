import pandas as pd

df = pd.read_csv("Cars.csv")

df.drop([0, 1, 2], inplace=True) # drop rows
print(df)

df.reset_index(inplace=True)
result = df.index.to_list()

print(df)

print(result)
