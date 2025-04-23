import pandas as pd

df = pd.read_csv("Cars.csv")

selection = df[df["aspiration"] == "turbo"]["body-style"].values
result = list(selection)
print(result)