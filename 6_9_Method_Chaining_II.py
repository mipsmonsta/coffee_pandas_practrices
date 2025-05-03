import pandas as pd

df = pd.read_csv("Cars.csv")

result = df["engine-size"].fillna(1.0).apply(lambda x: x + 1).sum()
print(result)