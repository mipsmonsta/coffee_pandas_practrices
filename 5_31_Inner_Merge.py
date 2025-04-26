import pandas as pd

df = pd.read_csv("cars.csv")
df2 = pd.read_csv("cars4.csv")

result = pd.merge(df, df2, how="inner", left_on="make", right_on="make")
print(result)
print(result.iloc[0, 0])