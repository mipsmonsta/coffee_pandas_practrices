import pandas as pd

df = pd.read_csv("Cars.csv")
df2 = pd.read_csv("cars4.csv")

result = pd.merge(df, df2, how="right", left_on="make", right_on="make")
print(result)
print(len(result))