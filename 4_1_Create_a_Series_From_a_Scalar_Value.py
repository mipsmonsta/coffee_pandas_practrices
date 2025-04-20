import pandas as pd

scalar_series = pd.Series(42, index=[0, 1, 2], dtype=float, name='CONST')

result = scalar_series.sum()

print(scalar_series)
print(result)