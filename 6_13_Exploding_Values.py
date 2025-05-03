import pandas as pd

df = pd.read_csv("cars.csv")
df = df.groupby("fuel").agg(list)
print(df)
result = df["make"].explode().count()

print(result)