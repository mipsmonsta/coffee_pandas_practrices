import pandas as pd

df = pd.read_csv("Cars.csv")

selection = df.sort_values(by="engine-size")
result = selection.index.to_list()[0]

print(result)