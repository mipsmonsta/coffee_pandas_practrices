import pandas as pd

df = pd.read_csv("cars.csv")

selection = df.iloc[lambda x:x.index % 2 == 0]
print(selection)
result = selection.index.to_list()
print(result)

selection2 = df.iloc[1]
print(selection2)