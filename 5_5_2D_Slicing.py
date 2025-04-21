import pandas as pd

df = pd.read_csv("Cars.csv")

result = df.loc[0:2, "price"].max()
print(result)