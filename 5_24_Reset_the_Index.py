import pandas as pd

df = pd.read_csv("Cars.csv")

a = df.index.to_list()[0]
df = df.loc[::-1].reset_index(drop=True)
b = df.index.to_list()[0]
print(a == b)