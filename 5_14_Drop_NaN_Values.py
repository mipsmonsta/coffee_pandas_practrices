import pandas as pd

df = pd.read_csv("Cars.csv")

selection1 = df.dropna(subset=["price"])
selection2 = df.dropna()
print(len(selection1), len(selection2))

