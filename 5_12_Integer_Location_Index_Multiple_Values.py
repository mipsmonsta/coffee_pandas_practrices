import pandas as pd

df = pd.read_csv("Cars.csv")
print(df)

df.sort_values(by="price", ascending=False, inplace=True)

print(df)
result = df.iloc[2,4]

print(result)