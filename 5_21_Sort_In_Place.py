import pandas as pd

df = pd.read_csv("Cars.csv")

df.sort_values(by="price")
first = df.index.to_list()
df.sort_values(by="price", inplace=True)
second = df.index.to_list()
print(first == second)