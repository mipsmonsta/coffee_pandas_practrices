import pandas as pd

df = pd.read_csv("Cars.csv")

for label in df.columns.values:
    s = df[label].isna().sum()
    if s > 0:
        print(label, s)