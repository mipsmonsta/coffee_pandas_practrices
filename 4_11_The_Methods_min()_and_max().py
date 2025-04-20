import pandas as pd

xs = pd.Series(range(100))
result = xs.max() + min(xs)

print(result)