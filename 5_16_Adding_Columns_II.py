import pandas as pd

df = pd.read_csv("Cars.csv")
df.loc[df.index.max() + 1] = ["ford", "gas", "std", "sedan", 1000, 2.0]
result = df.index[df["price"] <= 17000].to_list()

print(result)