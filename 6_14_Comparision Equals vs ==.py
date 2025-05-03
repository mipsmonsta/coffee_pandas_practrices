import pandas as pd

df = pd.read_csv("cars.csv")
df ["engine-size_copy"] = df["engine-size"]
check1= (df["engine-size_copy"] == df["engine-size"]).all()

check2= df["engine-size_copy"].equals(df["engine-size"])
print(check1 == check2)