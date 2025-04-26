import pandas as pd

df = pd.read_csv("Cars.csv")

df = df.loc[::-1] # reverse rows order
i = df.index.to_list()[0]
print(i)