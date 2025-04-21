import pandas as pd

xs = pd.Series([2, 0, 1])
xs.sort_values().sort_index() # inplace not set, so method chaining allowed

print(xs)