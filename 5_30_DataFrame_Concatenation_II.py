import pandas as pd

df = pd.read_csv("cars.csv")
df2 = pd.read_csv("cars3.csv")


try:
    result = pd.concat([df, df2], axis=0, ignore_index=True)
    print(result)
    print("Y")
except Exception:
    print("N")