import pandas as pd

bools = pd.Series([True, False, True, True])
result = bools.all() | bools.any()
print(result)