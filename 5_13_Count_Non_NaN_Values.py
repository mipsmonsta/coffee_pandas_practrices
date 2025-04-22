import pandas as pd

df = pd.read_csv("Cars.csv")

result = df.count()[5]
print(result)