import pandas as pd

df = pd.read_csv("cars.csv")
df2 = pd.read_csv("cars4.csv")

result = pd.merge(df, df2, how="outer", left_on="make", right_on="make")

print(result)
print(len(result["fuel"]))
print(result["fuel"].count())