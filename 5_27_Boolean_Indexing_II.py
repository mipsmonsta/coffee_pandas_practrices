import pandas as pd

df = pd.read_csv("Cars.csv")

result = df[(df["price"]>20000) | (df["price"] < 15000)]
result=result.index.to_list()

print(result)