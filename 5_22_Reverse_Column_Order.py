import pandas as pd

df = pd.read_csv("Cars.csv")

a = df.columns.to_list()[0] # first column title
df = df.loc[:, ::-1] # all rows, reverse column order
b = df.columns.to_list()[0]

print(a)
print(b)
print(a == b)

