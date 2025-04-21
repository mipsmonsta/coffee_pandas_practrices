import pandas as pd

df = pd.read_csv("Cars.csv")

df = df.add_prefix("tbl_")
df = df.add_suffix("_1")

print(df.columns[1])