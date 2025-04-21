import pandas as pd

s = pd.Series(range(0, 10))
t = pd.Series(range(0, 20))
result = (s + t)

print(result[1])
print(result)
print(result.hasnans)