import pandas as pd

df = pd.read_csv("Cars.csv")
df2 = pd.read_csv("Cars2.csv")

df3 = pd.concat([df, df2], axis=0) # concat by rows; ignore _index=True attribute not included
result = sum(df3.index)
print(result)