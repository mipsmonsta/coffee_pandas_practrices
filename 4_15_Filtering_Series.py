import pandas as pd

xs = pd.Series([5, 1, 4, 2, 3])
xs.where(xs > 2, inplace=True)

print(xs)
result = xs.hasnans

print(result)
