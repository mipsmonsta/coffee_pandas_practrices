import pandas as pd

df = pd.read_csv("Cars.csv")
df2 = pd.read_csv("Cars4.csv")

result = pd.merge(df2, df, how="left", left_on="make", right_on="make")
print(len(result["fuel"]))
print(result["fuel"].count())