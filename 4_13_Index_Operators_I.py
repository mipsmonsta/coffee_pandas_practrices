import pandas as pd

xs = pd.Series([5,1,4,2,3])
xs.sort_values(inplace=True)
print(xs) # after in-placed sorting
result = xs[0]
print(result)

result2 = xs.iloc[0]
print(result2)