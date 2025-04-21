import pandas as pd

df = pd.read_csv("Cars.csv")

selection = df.head(2)
result = selection.index.to_list()
print(selection)
print(result)