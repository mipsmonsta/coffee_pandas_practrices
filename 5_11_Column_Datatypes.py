import pandas as pd

df = pd.read_csv("Cars.csv")

print(len(df.select_dtypes(include="number").columns))

print(len(df.select_dtypes(include="object").columns))

print(len(df.select_dtypes(include=["datetime", "timedelta"]).columns))

print(df.select_dtypes(include="number"))

# other include = ["int8", "int16", "int32", "int64", "float"]
