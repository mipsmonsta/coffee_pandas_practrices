import pandas as pd

df = pd.read_csv("Cars.csv")

selection = df.iloc[0:3]
result = selection.index.to_list()
print(result)