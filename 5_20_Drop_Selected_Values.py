import pandas as pd

df = pd.read_csv("Cars.csv")

drop_idx = df[df["fuel"] == "gas"].index
df.drop(drop_idx, inplace=True)
result = df.index.to_list()
print(result)