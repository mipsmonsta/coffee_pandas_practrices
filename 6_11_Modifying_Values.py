import pandas as pd
df = pd.read_csv("Cars.csv")

df["aspiration"] = df["aspiration"].map({"std": "Standard", "turbo":"Turbo"})
print(df)

print(set(df["aspiration"]))