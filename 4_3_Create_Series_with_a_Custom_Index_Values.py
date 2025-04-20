import pandas as pd

fibs = [0, 1, 1, 2, 3, 5, 8]
idxs = [0, 1, 2, 3, 4, 5, 6]

fib_series = pd.Series(data=fibs, index=idxs)
print(fib_series)
result = fib_series.shape

print(result)