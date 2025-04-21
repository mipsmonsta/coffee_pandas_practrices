import pandas as pd

df = pd.read_csv("Cars.csv")

selection = df.tail(2)
result = selection.index.to_list()
print(result)