import pandas as pd

df = pd.read_csv("Cars.csv")
df2 = pd.read_csv("cars4.csv")

result = pd.merge(df, df2, how="outer", indicator=True)
print(result)
print(result.loc[2, "_merge"])