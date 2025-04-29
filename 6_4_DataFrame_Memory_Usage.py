import pandas as pd

df = pd.read_csv("Cars.csv")

result = df.memory_usage(deep=True)
print(result)