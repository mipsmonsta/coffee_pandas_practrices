import pandas as pd

df = pd.read_csv("Cars.csv")
df.fillna(2.0, inplace=True)
result = df["engine-size"].sum()
print(result)