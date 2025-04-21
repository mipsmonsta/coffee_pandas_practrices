import pandas as pd

s = pd.Series(range(10))
result = s.cumsum(axis=0)[4]

print(result) # 0 1 3 6, 10, so 10 is the result