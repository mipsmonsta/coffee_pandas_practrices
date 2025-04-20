import pandas as pd

s = pd.Series(range(0, 100, 50))
t = s > 50
result = t.any()
print(result)