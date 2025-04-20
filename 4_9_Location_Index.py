import pandas as pd

xs = pd.Series(range(7))
bs = [False, False, True, False, True, False, True]
result = xs.loc[bs].sum()
print(result)