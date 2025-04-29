import pandas as pd

df = pd.read_csv("Cars.csv")

df = df.filter(regex="-")
count = len(df.columns)
print(count)