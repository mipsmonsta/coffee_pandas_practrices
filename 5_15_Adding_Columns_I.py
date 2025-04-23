import pandas as pd

df = pd.read_csv("Cars.csv")

df["origin"] = ["Germany", "USA", "Japan", "Germany", "Sweden"]
intermediate = df[df["make"] == "porsche"]["origin"]
print(intermediate)
result = intermediate.values[0]

print(result) # Germany
